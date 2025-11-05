"""
Authentication Routes Module
Handles user login, registration, logout, and dashboard
"""

from flask import Blueprint, render_template_string, request, redirect, url_for, session, flash
from app.templates import LOGIN_HTML, REGISTER_HTML, DASHBOARD_HTML
from app.data import users, admins, hash_password
from app.csv_logger import log_user

bp = Blueprint('auth', __name__)

@bp.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page"""
    if request.method == 'POST':
        email = request.form.get('email') or request.form.get('username') or ''
        email = email.strip().lower()
        password = request.form.get('password', '')
        
        if ' ' in password:
            flash('Password cannot contain spaces', 'error')
        elif email in admins and admins[email]['password'] == hash_password(password):
            session['user_email'] = email
            session['is_admin'] = True
            flash('Admin login successful!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid admin credentials', 'error')
    
    # Use dedicated admin login template
    from app.templates import ADMIN_LOGIN_HTML
    return render_template_string(ADMIN_LOGIN_HTML)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        email = (request.form.get('email') or '').strip().lower()
        password = request.form.get('password', '')
        
        if ' ' in password:
            flash('Password cannot contain spaces', 'error')
        elif email not in users:
            flash('User not found', 'error')
        elif users[email]['password'] != hash_password(password):
            flash('Invalid password', 'error')
        else:
            session['user_email'] = email
            session['user_name'] = users[email]['fullname']
            session['is_admin'] = False  # Explicitly set to False for regular users
            flash('Login successful', 'success')
            return redirect(url_for('auth.dashboard'))
    
    return render_template_string(LOGIN_HTML)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        fullname = (request.form.get('fullname') or '').strip()
        email_raw = (request.form.get('email') or '').strip()
        phone = (request.form.get('phone') or '').strip()
        password = request.form.get('password', '')
        
        email = email_raw.lower()
        
        if ' ' in password:
            flash('Password cannot contain spaces', 'error')
        elif not email or email in users:
            flash('Email already exists', 'error')
        elif not (phone.isdigit() and len(phone) == 10):
            flash('Phone must be exactly 10 digits', 'error')
        else:
            users[email] = {
                'password': hash_password(password),
                'fullname': fullname,
                'phone': phone
            }
            # Mirror to CSV
            try:
                log_user(email, users[email])
            except Exception:
                pass
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('auth.login'))
    
    return render_template_string(REGISTER_HTML)

@bp.route('/dashboard')
def dashboard():
    """User dashboard"""
    if 'user_email' not in session:
        flash('Please login to access dashboard', 'error')
        return redirect(url_for('auth.login'))
    
    user_data = {
        'name': session['user_name'],
        'email': session['user_email'],
        'recent_bookings': []
    }
    return render_template_string(DASHBOARD_HTML, user=user_data)

@bp.route('/logout')
def logout():
    """User logout"""
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('main.index'))