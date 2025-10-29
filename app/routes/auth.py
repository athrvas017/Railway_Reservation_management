"""
Authentication Routes Module
Handles user login, registration, logout, and dashboard
"""

from flask import Blueprint, render_template_string, request, redirect, url_for, session, flash
from app.templates import LOGIN_HTML, REGISTER_HTML, DASHBOARD_HTML
from app.data import users, admins, hash_password

bp = Blueprint('auth', __name__)

@bp.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page"""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email in admins and admins[email]['password'] == hash_password(password):
            session['user_email'] = email
            session['is_admin'] = True
            flash('Admin login successful!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid admin credentials', 'error')
    
    # Use modified login template for admin
    admin_login_html = LOGIN_HTML.replace('User Login', 'Admin Login').replace('/login', '/admin-login').replace('Register here', 'User Login').replace('/register', '/login')
    return render_template_string(admin_login_html)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email not in users:
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
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        
        if email in users:
            flash('Email already exists', 'error')
        else:
            users[email] = {
                'password': hash_password(password),
                'fullname': fullname,
                'phone': phone
            }
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