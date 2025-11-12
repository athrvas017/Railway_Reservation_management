"""
Admin Routes Module
Handles admin dashboard and management operations
"""

from flask import Blueprint, render_template_string, request, redirect, url_for, session, flash
from app.templates import ADMIN_DASHBOARD_HTML, ADMIN_TRAINS_HTML, ADMIN_BOOKINGS_HTML, ADMIN_REPORTS_HTML, ADMIN_WAITINGLIST_HTML
from app.data import trains, bookings, waiting_lists, admins, users
from datetime import datetime
from app.csv_logger import log_train, log_booking

bp = Blueprint('admin', __name__)

def is_admin():
    """Check if current user is admin"""
    return session.get('is_admin', False)

@bp.route('/admin')
def dashboard():
    """Admin dashboard"""
    if not is_admin():
        flash('Admin access required', 'error')
        return redirect(url_for('auth.login'))
    
    # Calculate stats
    total_trains = len(trains)
    active_trains = len([t for t in trains.values() if t['status'] == 'Active'])
    total_bookings = len(bookings)
    confirmed_bookings = len([b for b in bookings.values() if b['status'] == 'CONFIRMED'])
    waiting_list_count = sum(len(wl) for wl in waiting_lists.values())
    total_revenue = sum(b['fare'] for b in bookings.values() if b['status'] == 'CONFIRMED')
    
    stats = {
        'total_trains': total_trains,
        'active_trains': active_trains,
        'total_bookings': total_bookings,
        'confirmed_bookings': confirmed_bookings,
        'waiting_list_count': waiting_list_count,
        'total_revenue': total_revenue
    }
    
    return render_template_string(ADMIN_DASHBOARD_HTML, stats=stats, trains=trains)

@bp.route('/admin/trains')
def manage_trains():
    """Manage trains"""
    if not is_admin():
        flash('Admin access required', 'error')
        return redirect(url_for('auth.login'))
    
    return render_template_string(ADMIN_TRAINS_HTML, trains=trains)


@bp.route('/admin/add-train', methods=['POST'])
def add_train():
    """Add a new train (admin only)."""
    if not is_admin():
        flash('Admin access required', 'error')
        return redirect(url_for('auth.login'))

    train_id = request.form.get('train_id', '').strip()
    name = request.form.get('name', '').strip()
    source = request.form.get('source', '').strip()
    destination = request.form.get('destination', '').strip()
    departure = request.form.get('departure', '').strip()
    arrival = request.form.get('arrival', '').strip()
    seats_total = request.form.get('seats_total', '').strip()
    fare_sl = request.form.get('fare_sl', '').strip()
    fare_3a = request.form.get('fare_3a', '').strip()
    fare_2a = request.form.get('fare_2a', '').strip()
    status = request.form.get('status', 'Active').strip() or 'Active'

    if not train_id or train_id in trains:
        flash('Invalid or duplicate Train ID', 'error')
        return redirect(url_for('admin.manage_trains'))

    try:
        seats_total_i = int(seats_total)
        fare_sl_i = int(fare_sl)
        fare_3a_i = int(fare_3a)
        fare_2a_i = int(fare_2a)
    except ValueError:
        flash('Seats and fares must be numbers', 'error')
        return redirect(url_for('admin.manage_trains'))

    trains[train_id] = {
        'name': name or 'New Train',
        'route': {'source': source or 'NA', 'destination': destination or 'NA'},
        'departure': departure or '00:00',
        'arrival': arrival or '00:00',
        'seats': {'total': seats_total_i, 'available': seats_total_i},
        'fare': {'SL': fare_sl_i, '3A': fare_3a_i, '2A': fare_2a_i},
        'status': status or 'Active'
    }

    try:
        log_train(train_id, trains[train_id])
    except Exception:
        pass

    flash(f'Train {train_id} added successfully', 'success')
    return redirect(url_for('admin.manage_trains'))

@bp.route('/admin/bookings')
def manage_bookings():
    """Manage bookings"""
    if not is_admin():
        flash('Admin access required', 'error')
        return redirect(url_for('auth.login'))
    
    # Get recent bookings with train details
    booking_list = []
    for pnr, booking in bookings.items():
        train = trains.get(booking['train_id'], {})
        booking_info = {
            'pnr': pnr,
            'user_email': booking['user_email'],
            'train_name': train.get('name', 'Unknown'),
            'train_id': booking['train_id'],
            'status': booking['status'],
            'fare': booking['fare'],
            'booking_date': booking['booking_date'],
            'passengers': len(booking['passengers'])
        }
        booking_list.append(booking_info)
    
    # Sort by booking date (newest first)
    booking_list.sort(key=lambda x: x['booking_date'], reverse=True)
    
    return render_template_string(ADMIN_BOOKINGS_HTML, bookings=booking_list)

@bp.route('/admin/update-train-status', methods=['POST'])
def update_train_status():
    """Update train status"""
    if not is_admin():
        return redirect(url_for('auth.login'))
    
    train_id = request.form['train_id']
    new_status = request.form['status']
    
    if train_id in trains:
        trains[train_id]['status'] = new_status
        flash(f'Train {train_id} status updated to {new_status}', 'success')
    else:
        flash('Train not found', 'error')
    
    return redirect(url_for('admin.manage_trains'))

@bp.route('/admin/cancel-booking', methods=['POST'])
def cancel_booking():
    """Cancel a booking"""
    if not is_admin():
        return redirect(url_for('auth.login'))
    
    pnr = request.form['pnr']
    
    if pnr in bookings:
        booking = bookings[pnr]
        train_id = booking['train_id']
        
        # If confirmed booking, release seats
        if booking['status'] == 'CONFIRMED':
            trains[train_id]['seats']['available'] += len(booking['passengers'])
            
            # Check waiting list and confirm if possible
            if train_id in waiting_lists and waiting_lists[train_id]:
                next_pnr = waiting_lists[train_id].pop(0)
                if next_pnr in bookings:
                    bookings[next_pnr]['status'] = 'CONFIRMED'
                    trains[train_id]['seats']['available'] -= len(bookings[next_pnr]['passengers'])
        
        # Remove from waiting list if applicable
        elif booking['status'].startswith('WL'):
            if train_id in waiting_lists and pnr in waiting_lists[train_id]:
                waiting_lists[train_id].remove(pnr)
        
        bookings[pnr]['status'] = 'CANCELLED'
        flash(f'Booking {pnr} cancelled successfully', 'success')
    else:
        flash('Booking not found', 'error')
    
    return redirect(url_for('admin.manage_bookings'))

@bp.route('/admin/reports')
def reports():
    """Admin reports page"""
    if not is_admin():
        flash('Admin access required', 'error')
        return redirect(url_for('auth.login'))
    
    # Calculate report statistics
    total_bookings = len(bookings)
    confirmed_bookings = len([b for b in bookings.values() if b['status'] == 'CONFIRMED'])
    canceled_bookings = len([b for b in bookings.values() if b['status'] in ('CANCELLED', 'CANCELED')])
    waiting_bookings = len([b for b in bookings.values() if b['status'].startswith('WL')])
    total_revenue = sum(b['fare'] for b in bookings.values() if b['status'] == 'CONFIRMED')
    
    report_data = {
        'total_bookings': total_bookings,
        'confirmed_bookings': confirmed_bookings,
        'canceled_bookings': canceled_bookings,
        'waiting_bookings': waiting_bookings,
        'total_revenue': total_revenue
    }
    
    return render_template_string(ADMIN_REPORTS_HTML, report=report_data)


@bp.route('/admin/waiting-list')
def waiting_list_view():
    """View waiting list and allow confirmations."""
    if not is_admin():
        flash('Admin access required', 'error')
        return redirect(url_for('auth.login'))

    wl_rows = []
    first_demo_pnr = None
    for train_id, pnr_list in waiting_lists.items():
        for idx, pnr in enumerate(pnr_list, start=1):
            b = bookings.get(pnr)
            if not b:
                continue
            if first_demo_pnr is None:
                first_demo_pnr = pnr
            train_name = trains.get(train_id, {}).get('name', 'Unknown')
            passenger_name = b.get('passengers', [{}])[0].get('name', 'NA')
            wl_rows.append({
                'train_name': train_name,
                'train_id': train_id,
                'pnr': pnr,
                'passenger_name': passenger_name,
                'position': idx,
            })

    return render_template_string(ADMIN_WAITINGLIST_HTML, waiting_list=wl_rows, demo_pnr=first_demo_pnr)


@bp.route('/admin/confirm-wl', methods=['POST'])
def confirm_waiting_list():
    """Confirm a waiting list PNR if seats are available."""
    if not is_admin():
        flash('Admin access required', 'error')
        return redirect(url_for('auth.login'))

    pnr = request.form.get('pnr', '').strip()
    if pnr not in bookings:
        flash('Invalid PNR', 'error')
        return redirect(url_for('admin.waiting_list_view'))

    booking = bookings[pnr]
    train_id = booking['train_id']
    num_passengers = len(booking.get('passengers', []))

    # Check seat availability
    if trains[train_id]['seats']['available'] >= num_passengers:
        trains[train_id]['seats']['available'] -= num_passengers
        booking['status'] = 'CONFIRMED'
        # Remove PNR from waiting list
        if train_id in waiting_lists and pnr in waiting_lists[train_id]:
            waiting_lists[train_id] = [x for x in waiting_lists[train_id] if x != pnr]
        try:
            log_booking(pnr, booking)
        except Exception:
            pass
        flash(f'PNR {pnr} confirmed successfully', 'success')
    else:
        flash('Not enough seats available to confirm this PNR', 'error')

    return redirect(url_for('admin.waiting_list_view'))
