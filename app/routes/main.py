"""
Main Routes Module
Handles home page, static files, and general routes
"""

from flask import Blueprint, render_template_string, Response, send_from_directory
from app.templates import INDEX_HTML, CANCELLATION_HTML
from app.styles import CSS_STYLES
from app.csv_logger import log_cancellation, log_pnr_status_check

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Homepage"""
    return render_template_string(INDEX_HTML)

@bp.route('/styles.css')
def serve_css():
    """Serve CSS styles"""
    return Response(CSS_STYLES, mimetype='text/css')

@bp.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files (logo, images, etc.)"""
    import os
    static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
    return send_from_directory(static_dir, filename)

@bp.route('/cancel-ticket', methods=['GET', 'POST'])
def cancel_ticket():
    """Handle ticket cancellation and PNR status check - accessible without login"""
    from flask import request, flash
    from app.data import bookings, trains, waiting_lists

    booking_info = None
    
    if request.method == 'POST':
        pnr = request.form['pnr']
        action = request.form.get('action', 'cancel')
        
        # PNR status check path
        if action == 'check':
            if pnr in bookings:
                booking_info = bookings[pnr]
                status = booking_info['status']
                log_pnr_status_check(pnr, True, status)
                flash(f'PNR {pnr} status: {status}', 'success')
            else:
                log_pnr_status_check(pnr, False, '')
                flash('Booking not found with this PNR number', 'error')
        else:
            # Cancel path
            if pnr not in bookings:
                flash('Booking not found with this PNR number', 'error')
            else:
                booking = bookings[pnr]
                train_id = booking['train_id']
                
                if booking['status'] == 'CONFIRMED':
                    # Free up seats and promote waiting list
                    num_passengers = len(booking['passengers'])
                    trains[train_id]['seats']['available'] += num_passengers
                    
                    # Promote waiting list
                    if train_id in waiting_lists and waiting_lists[train_id]:
                        promoted_pnr = waiting_lists[train_id].pop(0)
                        if promoted_pnr in bookings:
                            bookings[promoted_pnr]['status'] = 'CONFIRMED'
                
                elif booking['status'].startswith('WL-'):
                    # Remove from waiting list
                    if train_id in waiting_lists and pnr in waiting_lists[train_id]:
                        waiting_lists[train_id].remove(pnr)
                
                # Log cancellation before mutating status for accurate status_before
                refund_amount = booking['fare'] * 0.8  # 80% refund
                try:
                    log_cancellation(pnr, booking, refund_amount)
                except Exception:
                    pass

                booking['status'] = 'CANCELED'
                
                flash(f'Ticket canceled successfully! PNR: {pnr}. Refund: ₹{refund_amount}', 'success')
                booking_info = booking
    
    return render_template_string(CANCELLATION_HTML, booking=booking_info)
