"""
NextStop Railway Reservation System
Main Flask Application Module
"""

from flask import Flask
from app.data import initialize_data


def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    app.secret_key = 'nextstop_modular_system_2024'
    
    # Initialize dummy data
    initialize_data()

    # Mirror existing in-memory data to CSV snapshot
    try:
        from app.data import users, bookings, trains
        from app.csv_logger import bootstrap_dump
        bootstrap_dump(users, bookings, trains)
    except Exception:
        pass
    
    # Register blueprints/routes
    from app.routes import auth, main, booking, admin
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(booking.bp)
    app.register_blueprint(admin.bp)
    
    return app
