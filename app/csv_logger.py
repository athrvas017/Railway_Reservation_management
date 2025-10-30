"""
CSV Logging utilities to mirror in-memory data to CSV files.
Creates/updates CSVs under a data_logs directory at project root.
"""

import csv
import os
from datetime import datetime
from typing import Dict, Any

# Determine project root (two levels up from this file)
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(PROJECT_ROOT, 'data_logs')

FILES = {
    'users': os.path.join(LOG_DIR, 'users.csv'),
    'bookings': os.path.join(LOG_DIR, 'bookings.csv'),
    'cancellations': os.path.join(LOG_DIR, 'cancellations.csv'),
    'pnr_checks': os.path.join(LOG_DIR, 'pnr_status_checks.csv'),
    'trains': os.path.join(LOG_DIR, 'trains.csv'),
}


def _ensure_dir():
    os.makedirs(LOG_DIR, exist_ok=True)


def _write_header_if_needed(path: str, headers: list[str]):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()


def log_user(email: str, user: Dict[str, Any]):
    """Append or update a user entry."""
    try:
        _ensure_dir()
        path = FILES['users']
        headers = ['timestamp', 'email', 'fullname', 'phone']
        _write_header_if_needed(path, headers)
        with open(path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writerow({
                'timestamp': datetime.now().isoformat(timespec='seconds'),
                'email': email,
                'fullname': user.get('fullname', ''),
                'phone': user.get('phone', ''),
            })
    except Exception:
        # Swallow logging errors to not break app flow
        pass


def log_train(train_id: str, train: Dict[str, Any]):
    try:
        _ensure_dir()
        path = FILES['trains']
        headers = ['timestamp', 'train_id', 'name', 'source', 'destination', 'departure', 'arrival', 'seats_total', 'seats_available', 'fare_SL', 'fare_3A', 'fare_2A', 'status']
        _write_header_if_needed(path, headers)
        with open(path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writerow({
                'timestamp': datetime.now().isoformat(timespec='seconds'),
                'train_id': train_id,
                'name': train.get('name', ''),
                'source': train.get('route', {}).get('source', ''),
                'destination': train.get('route', {}).get('destination', ''),
                'departure': train.get('departure', ''),
                'arrival': train.get('arrival', ''),
                'seats_total': train.get('seats', {}).get('total', ''),
                'seats_available': train.get('seats', {}).get('available', ''),
                'fare_SL': train.get('fare', {}).get('SL', ''),
                'fare_3A': train.get('fare', {}).get('3A', ''),
                'fare_2A': train.get('fare', {}).get('2A', ''),
                'status': train.get('status', ''),
            })
    except Exception:
        pass


def log_booking(pnr: str, booking: Dict[str, Any]):
    try:
        _ensure_dir()
        path = FILES['bookings']
        headers = ['timestamp', 'pnr', 'user_email', 'train_id', 'date', 'status', 'fare', 'booking_date', 'passenger_count', 'passengers']
        _write_header_if_needed(path, headers)
        with open(path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            passengers_serialized = '; '.join([f"{p.get('name')}|{p.get('age')}|{p.get('gender')}|{p.get('seat_type')}" for p in booking.get('passengers', [])])
            writer.writerow({
                'timestamp': datetime.now().isoformat(timespec='seconds'),
                'pnr': pnr,
                'user_email': booking.get('user_email', ''),
                'train_id': booking.get('train_id', ''),
                'date': booking.get('date', ''),
                'status': booking.get('status', ''),
                'fare': booking.get('fare', ''),
                'booking_date': booking.get('booking_date', ''),
                'passenger_count': len(booking.get('passengers', [])),
                'passengers': passengers_serialized,
            })
    except Exception:
        pass


def log_cancellation(pnr: str, booking: Dict[str, Any], refund_amount: float):
    try:
        _ensure_dir()
        path = FILES['cancellations']
        headers = ['timestamp', 'pnr', 'user_email', 'train_id', 'status_before', 'refund_amount']
        _write_header_if_needed(path, headers)
        with open(path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writerow({
                'timestamp': datetime.now().isoformat(timespec='seconds'),
                'pnr': pnr,
                'user_email': booking.get('user_email', ''),
                'train_id': booking.get('train_id', ''),
                'status_before': booking.get('status', ''),
                'refund_amount': refund_amount,
            })
    except Exception:
        pass


def log_pnr_status_check(pnr: str, found: bool, status: str = ''):
    try:
        _ensure_dir()
        path = FILES['pnr_checks']
        headers = ['timestamp', 'pnr', 'found', 'status']
        _write_header_if_needed(path, headers)
        with open(path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writerow({
                'timestamp': datetime.now().isoformat(timespec='seconds'),
                'pnr': pnr,
                'found': 'yes' if found else 'no',
                'status': status,
            })
    except Exception:
        pass


def bootstrap_dump(users: Dict[str, Any], bookings: Dict[str, Any], trains: Dict[str, Any] | None = None):
    """Write a fresh snapshot of current in-memory data to CSVs (overwrites)."""
    try:
        _ensure_dir()
        # Users snapshot
        users_path = FILES['users']
        with open(users_path, mode='w', newline='', encoding='utf-8') as f:
            headers = ['timestamp', 'email', 'fullname', 'phone']
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            now = datetime.now().isoformat(timespec='seconds')
            for email, u in users.items():
                writer.writerow({'timestamp': now, 'email': email, 'fullname': u.get('fullname', ''), 'phone': u.get('phone', '')})
        
        # Bookings snapshot
        bookings_path = FILES['bookings']
        with open(bookings_path, mode='w', newline='', encoding='utf-8') as f:
            headers = ['timestamp', 'pnr', 'user_email', 'train_id', 'date', 'status', 'fare', 'booking_date', 'passenger_count', 'passengers']
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            now = datetime.now().isoformat(timespec='seconds')
            for pnr, b in bookings.items():
                passengers_serialized = '; '.join([f"{p.get('name')}|{p.get('age')}|{p.get('gender')}|{p.get('seat_type')}" for p in b.get('passengers', [])])
                writer.writerow({
                    'timestamp': now,
                    'pnr': pnr,
                    'user_email': b.get('user_email', ''),
                    'train_id': b.get('train_id', ''),
                    'date': b.get('date', ''),
                    'status': b.get('status', ''),
                    'fare': b.get('fare', ''),
                    'booking_date': b.get('booking_date', ''),
                    'passenger_count': len(b.get('passengers', [])),
                    'passengers': passengers_serialized,
                })
        
        # Trains snapshot (optional)
        if trains is not None:
            trains_path = FILES['trains']
            with open(trains_path, mode='w', newline='', encoding='utf-8') as f:
                headers = ['timestamp', 'train_id', 'name', 'source', 'destination', 'departure', 'arrival', 'seats_total', 'seats_available', 'fare_SL', 'fare_3A', 'fare_2A', 'status']
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                now = datetime.now().isoformat(timespec='seconds')
                for tid, t in trains.items():
                    writer.writerow({
                        'timestamp': now,
                        'train_id': tid,
                        'name': t.get('name', ''),
                        'source': t.get('route', {}).get('source', ''),
                        'destination': t.get('route', {}).get('destination', ''),
                        'departure': t.get('departure', ''),
                        'arrival': t.get('arrival', ''),
                        'seats_total': t.get('seats', {}).get('total', ''),
                        'seats_available': t.get('seats', {}).get('available', ''),
                        'fare_SL': t.get('fare', {}).get('SL', ''),
                        'fare_3A': t.get('fare', {}).get('3A', ''),
                        'fare_2A': t.get('fare', {}).get('2A', ''),
                        'status': t.get('status', ''),
                    })
    except Exception:
        # Don't crash app if snapshot fails
        pass