#!/usr/bin/env python3
"""
NextStop Railway Reservation System
Modular Startup Script

To run the application:
1. Create virtual environment: python -m venv venv
2. Activate: venv\\Scripts\\activate (Windows)
3. Install Flask: pip install Flask
4. Run: python run.py
5. Open browser: http://localhost:5000
"""

from app import create_app

if __name__ == '__main__':
    app = create_app()
    print("=" * 60)
    print("🚂 NextStop Railway Reservation System")
    print("=" * 60)
    print("Starting modular Flask server...")
    print("Open your browser to: http://localhost:5000")
    print("👤 Demo user: user@test.com / password123")
    print("🔐 Demo admin: admin@nextstop.com / admin123")
    print("=" * 60)
    
    app.run(debug=True, host='127.0.0.1', port=5000)
