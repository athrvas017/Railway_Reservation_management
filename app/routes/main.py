"""
Main Routes Module
Handles home page, static files, and general routes
"""

from flask import Blueprint, render_template_string, Response, send_from_directory
from app.templates import INDEX_HTML, CANCELLATION_HTML
from app.styles import CSS_STYLES

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
    """Handle ticket cancellation - accessible without login"""
    from flask import request, flash, session
    from app.data import bookings, trains, waiting_lists
    
    if request.method == 'POST':
        pnr = request.form['pnr']
        
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
            
            booking['status'] = 'CANCELED'
            refund_amount = booking['fare'] * 0.8  # 80% refund
            
            flash(f'Ticket canceled successfully! PNR: {pnr}. Refund: ₹{refund_amount}', 'success')
    
    return render_template_string(CANCELLATION_HTML)