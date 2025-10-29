"""
Booking Routes Module
Handles train search, booking, and ticket management
"""

from flask import Blueprint, render_template_string, request, redirect, url_for, session, flash
from app.templates import SEARCH_HTML, RESULTS_HTML, BOOKING_HTML, BOOKING_DETAILS_HTML
from app.data import trains, bookings, waiting_lists
from datetime import datetime
import random
import string

bp = Blueprint('booking', __name__)

def generate_booking_id():
    """Generate a unique PNR"""
    return 'PNR' + ''.join(random.choices(string.digits, k=7))

def search_trains(source, destination, date):
    """Search for available trains"""
    available_trains = []
    for train_id, train_data in trains.items():
        if (train_data['route']['source'].lower() == source.lower() and 
            train_data['route']['destination'].lower() == destination.lower() and
            train_data['status'] == 'Active'):
            
            available_seats = train_data['seats']['available']
            waiting_list_count = len(waiting_lists.get(train_id, []))
            
            train_info = {
                'train_id': train_id,
                'name': train_data['name'],
                'departure': train_data['departure'],
                'arrival': train_data['arrival'],
                'available_seats': available_seats,
                'waiting_list': waiting_list_count,
                'fare': train_data['fare']
            }
            available_trains.append(train_info)
    
    return available_trains

def process_booking(train_id, date, passenger_list, total_fare, user_email):
    """Process a booking and return PNR and status"""
    pnr = generate_booking_id()
    train = trains[train_id]
    
    if train['seats']['available'] >= len(passenger_list):
        # Confirmed booking
        train['seats']['available'] -= len(passenger_list)
        status = 'CONFIRMED'
    else:
        # Waiting list
        if train_id not in waiting_lists:
            waiting_lists[train_id] = []
        waiting_lists[train_id].append(pnr)
        wl_number = len(waiting_lists[train_id])
        status = f'WL-{wl_number}'
    
    booking = {
        'user_email': user_email,
        'train_id': train_id,
        'date': date,
        'passengers': passenger_list,
        'status': status,
        'fare': total_fare,
        'booking_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    bookings[pnr] = booking
    return pnr, status

@bp.route('/search', methods=['GET', 'POST'])
def search():
    """Search for trains"""
    if 'user_email' not in session:
        flash('Please login to search trains', 'error')
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        source = request.form['source']
        destination = request.form['destination']
        date = request.form['date']
        
        trains_list = search_trains(source, destination, date)
        
        return render_template_string(RESULTS_HTML, 
                             trains=trains_list, 
                             search_source=source, 
                             search_destination=destination, 
                             search_date=date)
    
    return render_template_string(SEARCH_HTML)

@bp.route('/book/<train_id>')
def book(train_id):
    """Show booking form for a specific train"""
    if 'user_email' not in session:
        return redirect(url_for('auth.login'))
    
    if train_id not in trains:
        flash('Train not found', 'error')
        return redirect(url_for('booking.search'))
    
    train = trains[train_id]
    return render_template_string(BOOKING_HTML, train_id=train_id, train=train)

@bp.route('/process-booking', methods=['POST'])
def process_booking_route():
    """Process the booking form submission"""
    if 'user_email' not in session:
        return redirect(url_for('auth.login'))
    
    train_id = request.form['train_id']
    date = request.form.get('date', datetime.now().strftime('%Y-%m-%d'))
    user_email = session['user_email']
    
    # Simple passenger processing for demo
    passengers = [{
        'name': request.form.get('passenger_name', 'Demo Passenger'),
        'age': request.form.get('passenger_age', '30'),
        'gender': request.form.get('passenger_gender', 'Male'),
        'seat_type': request.form.get('seat_type', 'SL')
    }]
    
    # Calculate total fare
    train = trains[train_id]
    total_fare = sum(train['fare'][p['seat_type']] for p in passengers)
    
    pnr, status = process_booking(train_id, date, passengers, total_fare, user_email)
    
    flash(f'Booking successful! PNR: {pnr}, Status: {status}', 'success')
    return redirect(url_for('booking.booking_details', pnr=pnr))

@bp.route('/booking-details/<pnr>')
def booking_details(pnr):
    """Show booking details"""
    if 'user_email' not in session:
        return redirect(url_for('auth.login'))
    
    if pnr not in bookings:
        flash('Booking not found', 'error')
        return redirect(url_for('booking.search'))
    
    booking = bookings[pnr]
    train = trains[booking['train_id']]
    return render_template_string(BOOKING_DETAILS_HTML, pnr=pnr, booking=booking, train=train)