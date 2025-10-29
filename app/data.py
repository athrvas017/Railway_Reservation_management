"""
Data Storage Module
Contains in-memory data storage and dummy data initialization
"""

import hashlib
from datetime import datetime, timedelta

# In-memory data storage
users = {}
admins = {}
trains = {}
bookings = {}
waiting_lists = {}

def hash_password(password):
    """Hash a password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def initialize_data():
    """Initialize the application with dummy data"""
    
    # Initialize admin accounts
    admins['admin@nextstop.com'] = {
        'password': hash_password('admin123')
    }
    
    # Initialize dummy users
    users['john.doe@email.com'] = {
        'password': hash_password('password123'),
        'fullname': 'John Doe',
        'phone': '9876543210'
    }
    
    users['jane.smith@email.com'] = {
        'password': hash_password('password123'),
        'fullname': 'Jane Smith',
        'phone': '9876543211'
    }
    
    users['demo@user.com'] = {
        'password': hash_password('demo123'),
        'fullname': 'Demo User',
        'phone': '9999999999'
    }
    
    # Initialize train data
    trains['12951'] = {
        'name': 'Rajdhani Express',
        'route': {'source': 'Mumbai', 'destination': 'Delhi'},
        'departure': '17:00',
        'arrival': '09:00',
        'seats': {'total': 200, 'available': 150},
        'fare': {'SL': 2500, '3A': 3500, '2A': 4500},
        'status': 'Active'
    }
    
    trains['12137'] = {
        'name': 'Punjab Mail',
        'route': {'source': 'Mumbai', 'destination': 'Delhi'},
        'departure': '19:30',
        'arrival': '21:30',
        'seats': {'total': 180, 'available': 20},
        'fare': {'SL': 1850, '3A': 2850, '2A': 3850},
        'status': 'Active'
    }
    
    trains['22221'] = {
        'name': 'Duronto Express',
        'route': {'source': 'Mumbai', 'destination': 'Delhi'},
        'departure': '23:00',
        'arrival': '13:00',
        'seats': {'total': 220, 'available': 0},
        'fare': {'SL': 3100, '3A': 4100, '2A': 5100},
        'status': 'Active'
    }

    trains['12001'] = {
        'name': 'Shatabdi Express',
        'route': {'source': 'Delhi', 'destination': 'Mumbai'},
        'departure': '06:00',
        'arrival': '22:30',
        'seats': {'total': 150, 'available': 75},
        'fare': {'SL': 2200, '3A': 3200, '2A': 4200},
        'status': 'Active'
    }

    trains['12259'] = {
        'name': 'Duronto Express',
        'route': {'source': 'Delhi', 'destination': 'Mumbai'},
        'departure': '16:55',
        'arrival': '09:15',
        'seats': {'total': 200, 'available': 100},
        'fare': {'SL': 2800, '3A': 3800, '2A': 4800},
        'status': 'Active'
    }
    
    trains['12627'] = {
        'name': 'Karnataka Express',
        'route': {'source': 'Delhi', 'destination': 'Bangalore'},
        'departure': '21:50',
        'arrival': '04:30',
        'seats': {'total': 180, 'available': 90},
        'fare': {'SL': 3200, '3A': 4200, '2A': 5200},
        'status': 'Active'
    }
    
    trains['12024'] = {
        'name': 'Janshatabdi Express',
        'route': {'source': 'Mumbai', 'destination': 'Pune'},
        'departure': '07:15',
        'arrival': '10:30',
        'seats': {'total': 120, 'available': 60},
        'fare': {'SL': 450, '3A': 750, '2A': 950},
        'status': 'Active'
    }
    
    # Initialize dummy bookings
    bookings['PNR1234567'] = {
        'user_email': 'john.doe@email.com',
        'train_id': '12951',
        'date': '2024-10-20',
        'passengers': [
            {'name': 'John Doe', 'age': '30', 'gender': 'Male', 'seat_type': 'SL'}
        ],
        'status': 'CONFIRMED',
        'fare': 2500,
        'booking_date': '2024-10-15 14:30:00'
    }
    
    bookings['PNR2345678'] = {
        'user_email': 'jane.smith@email.com',
        'train_id': '12137',
        'date': '2024-10-18',
        'passengers': [
            {'name': 'Jane Smith', 'age': '28', 'gender': 'Female', 'seat_type': '3A'},
            {'name': 'Bob Smith', 'age': '32', 'gender': 'Male', 'seat_type': '3A'}
        ],
        'status': 'CONFIRMED',
        'fare': 5700,
        'booking_date': '2024-10-14 16:45:00'
    }
    
    bookings['PNR3456789'] = {
        'user_email': 'demo@user.com',
        'train_id': '22221',
        'date': '2024-10-25',
        'passengers': [
            {'name': 'Demo User', 'age': '25', 'gender': 'Male', 'seat_type': 'SL'}
        ],
        'status': 'WL-1',
        'fare': 3100,
        'booking_date': '2024-10-15 10:15:00'
    }
    
    # Initialize waiting lists
    waiting_lists['22221'] = ['PNR3456789']
    
    print("✅ Dummy data initialized successfully!")
    print(f"   - {len(users)} dummy users created")
    print(f"   - {len(trains)} trains available")
    print(f"   - {len(bookings)} sample bookings created")
    print("   - Login credentials:")
    print("     • User: john.doe@email.com / password123")
    print("     • User: jane.smith@email.com / password123") 
    print("     • User: demo@user.com / demo123")
    print("     • Admin: admin@nextstop.com / admin123")