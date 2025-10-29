"""
HTML Templates Module
Contains all HTML templates for the application
"""

INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Railway Reservation System | Home</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop
            </a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/login">Login</a></li>
                <li><a href="/register">Register</a></li>
                <li><a href="/cancel-ticket">Cancel Ticket</a></li>
            </ul>
        </div>
    </nav>

    <main class="main-content">
        <div class="container">
            <header style="text-align: center; padding: 60px 0; background: var(--white); border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <h1 style="color: var(--primary-blue); margin-bottom: 10px;">Welcome to NextStop</h1>
                <p style="font-size: 1.2em; color: var(--secondary-grey);">Your seamless platform for train ticket reservations.</p>
                <div style="margin-top: 30px;">
                    <a href="/login" class="btn btn-primary" style="padding: 15px 30px; font-size: 1.1em;">Start Booking Now</a>
                </div>
            </header>

            <section style="margin-top: 40px; text-align: center;">
                <h2 style="color: var(--primary-blue); margin-bottom: 20px;">Railway Reservation System</h2>
                <p style="max-width: 800px; margin: 0 auto; color: #555;">
                    This system provides comprehensive functionality for Railway Reservation Management.
                    Book tickets, manage your journeys, and experience seamless travel planning.
                    We have pre-loaded demo data so you can explore all features immediately!
                </p>
                
                <div style="margin-top: 30px; padding: 20px; background: #e3f2fd; border-radius: 8px; max-width: 600px; margin: 30px auto;">
                    <h3 style="color: var(--primary-blue); margin-bottom: 15px;">🎯 Try Demo Accounts</h3>
                    <p style="font-size: 0.9em; color: #666;">
                        <strong>Users:</strong> john.doe@email.com / password123<br>
                        <strong>Admin:</strong> admin@nextstop.com / admin123
                    </p>
                </div>
            </section>
        </div>
    </main>
</body>
</html>
"""

LOGIN_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Railway Reservation System | Login</title>
    <link rel="stylesheet" href="/styles.css"> 
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop
            </a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/login">Login</a></li>
                <li><a href="/register">Register</a></li>
                <li><a href="/cancel-ticket">Cancel Ticket</a></li>
            </ul>
        </div>
    </nav>
<main class="main-content">
    <div class="form-card">
        <h2 style="text-align: center; color: var(--primary-blue); margin-bottom: 30px;">User Login</h2>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="message message-{{ 'success' if category == 'success' else 'error' }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form method="POST" action="/login">
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" placeholder="email@example.com" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="********" required>
            </div>
            <button type="submit" class="btn btn-primary" style="width: 100%; margin-bottom: 10px;">Login</button>
            <p style="text-align: center; margin-top: 15px; font-size: 0.9em;">
                Don't have an account? <a href="/register" style="color: var(--primary-blue);">Register here</a>
            </p>
            <p style="text-align: center; margin-top: 10px; font-size: 0.9em;">
                <a href="/admin-login" style="color: var(--secondary-grey);">Admin Login</a>
            </p>
        </form>
        
        <div style="margin-top: 20px; padding: 15px; background: #f8f9fa; border-radius: 4px; font-size: 0.85em; color: #666;">
            <strong>Demo Accounts:</strong><br>
            john.doe@email.com / password123<br>
            demo@user.com / demo123
        </div>
    </div>
</main>
</body>
</html>
"""

REGISTER_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Railway Reservation System | Register</title>
    <link rel="stylesheet" href="/styles.css"> 
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop
            </a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/login">Login</a></li>
                <li><a href="/register">Register</a></li>
                <li><a href="/cancel-ticket">Cancel Ticket</a></li>
            </ul>
        </div>
    </nav>
<main class="main-content">
    <div class="form-card">
        <h2 style="text-align: center; color: var(--primary-blue); margin-bottom: 30px;">Create Account</h2>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="message message-{{ 'success' if category == 'success' else 'error' }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form method="POST" action="/register">
            <div class="form-group">
                <label for="fullname">Full Name</label>
                <input type="text" id="fullname" name="fullname" placeholder="John Doe" required>
            </div>
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" placeholder="email@example.com" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="text" id="phone" name="phone" placeholder="9876543210" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="********" required>
            </div>
            <button type="submit" class="btn btn-primary" style="width: 100%;">Register</button>
            <p style="text-align: center; margin-top: 15px; font-size: 0.9em;">
                Already have an account? <a href="/login" style="color: var(--primary-blue);">Login here</a>
            </p>
        </form>
    </div>
</main>
</body>
</html>
"""

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NextStop | Dashboard</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop
            </a>
            <ul class="nav-links">
                <li><a href="/search">Book Tickets</a></li>
                <li><a href="/cancel-ticket">Cancel Ticket</a></li>
                <li><a href="/logout">Logout</a></li>
            </ul>
        </div>
    </nav>

    <main class="main-content">
        <div class="container">
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    {% for category, message in messages %}
                        <div class="message message-{{ 'success' if category == 'success' else 'error' }}">
                            {{ message }}
                        </div>
                    {% endfor %}
                {% endif %}
            {% endwith %}

            <div style="text-align: center; margin-bottom: 40px;">
                <h1 style="color: var(--primary-blue);">Welcome, {{ user.name }}! 🎫</h1>
                <p style="color: var(--secondary-grey); font-size: 1.1em;">Ready to book your next journey?</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 40px;">
                <!-- Quick Book -->
                <div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); text-align: center;">
                    <div style="font-size: 3em; margin-bottom: 15px;">🚂</div>
                    <h3 style="color: var(--primary-blue); margin-bottom: 15px;">Book Tickets</h3>
                    <p style="color: #666; margin-bottom: 20px;">Search and book train tickets quickly and easily</p>
                    <a href="/search" class="btn btn-primary">Start Booking</a>
                </div>

                <!-- Cancel Tickets -->
                <div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); text-align: center;">
                    <div style="font-size: 3em; margin-bottom: 15px;">📋</div>
                    <h3 style="color: var(--primary-blue); margin-bottom: 15px;">Cancel Tickets</h3>
                    <p style="color: #666; margin-bottom: 20px;">Cancel your existing bookings</p>
                    <a href="/cancel-ticket" class="btn btn-secondary">Cancel Ticket</a>
                </div>

                <!-- Account -->
                <div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); text-align: center;">
                    <div style="font-size: 3em; margin-bottom: 15px;">👤</div>
                    <h3 style="color: var(--primary-blue); margin-bottom: 15px;">Account</h3>
                    <p style="color: #666; margin-bottom: 20px;">Manage your profile and preferences</p>
                    <button class="btn btn-secondary" onclick="alert('Account management coming soon!')">Manage Account</button>
                </div>
            </div>

            <!-- User Stats -->
            <div style="background: linear-gradient(135deg, var(--primary-blue), #0056b3); color: white; padding: 30px; border-radius: 10px; margin-top: 30px; text-align: center;">
                <h3 style="margin-bottom: 20px;">Your Account Summary</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 20px;">
                    <div>
                        <div style="font-size: 2em; font-weight: bold;">{{ user.recent_bookings|length }}</div>
                        <div>Total Bookings</div>
                    </div>
                    <div>
                        <div style="font-size: 1.2em; font-weight: bold;">{{ user.email }}</div>
                        <div>Account Email</div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
"""

SEARCH_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Railway Reservation System | Search Trains</title>
    <link rel="stylesheet" href="/styles.css"> 
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop
            </a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/search">Search</a></li>
                <li><a href="/cancel-ticket">Cancel Ticket</a></li>
                <li><a href="/logout">Logout</a></li>
            </ul>
        </div>
    </nav>
<main class="main-content">
    <div class="form-card">
        <h2 style="text-align: center; color: var(--primary-blue); margin-bottom: 30px;">Search Trains</h2>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="message message-{{ 'success' if category == 'success' else 'error' }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form method="POST" action="/search">
            <div class="form-group">
                <label for="source">Source Station</label>
                <input type="text" id="source" name="source" placeholder="E.g., Mumbai" required>
            </div>
            <div class="form-group">
                <label for="destination">Destination Station</label>
                <input type="text" id="destination" name="destination" placeholder="E.g., Delhi" required>
            </div>
            <div class="form-group">
                <label for="date">Journey Date</label>
                <input type="date" id="date" name="date" required>
            </div>
            <button type="submit" class="btn btn-primary" style="width: 100%;">Search Trains</button>
        </form>
        
        <div style="margin-top: 20px; padding: 15px; background: #e8f5e8; border-radius: 4px; font-size: 0.85em; color: #666;">
            <strong>💡 Quick Tips:</strong><br>
            Try searching: Mumbai → Delhi, Delhi → Mumbai, or Delhi → Bangalore
        </div>
    </div>
</main>
<script>
// Set default date to tomorrow
document.addEventListener('DOMContentLoaded', function() {
    const dateInput = document.getElementById('date');
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    dateInput.value = tomorrow.toISOString().split('T')[0];
});
</script>
</body>
</html>
"""

RESULTS_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Railway Reservation System | Search Results</title>
    <link rel="stylesheet" href="/styles.css"> 
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop
            </a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/search">Book Ticket</a></li>
                <li><a href="/cancel-ticket">Cancel Ticket</a></li>
                <li><a href="/logout">Logout</a></li>
            </ul>
        </div>
    </nav>
<main class="main-content">
    <div class="container">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="message message-{{ 'success' if category == 'success' else 'error' }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <h2 style="color: var(--primary-blue); margin-bottom: 20px;">Train Search Results ({{ search_source }} to {{ search_destination }} on {{ search_date }})</h2>

        <table class="data-table">
            <thead>
                <tr>
                    <th>Train No</th>
                    <th>Train Name</th>
                    <th>Departure</th>
                    <th>Arrival</th>
                    <th>Available Seats</th>
                    <th>Fare (₹)</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {% if trains %}
                    {% for train in trains %}
                    <tr>
                        <td>{{ train.train_id }}</td>
                        <td>{{ train.name }}</td>
                        <td>{{ train.departure }}</td>
                        <td>{{ train.arrival }}</td>
                        <td>
                            {% if train.available_seats > 0 %}
                                <span style="color: var(--success-green); font-weight: bold;">{{ train.available_seats }}</span>
                            {% else %}
                                <span style="color: var(--danger-red); font-weight: bold;">WL-{{ train.waiting_list + 1 }}</span>
                            {% endif %}
                        </td>
                        <td>
                            SL: {{ train.fare.SL }}<br>
                            3A: {{ train.fare['3A'] }}<br>
                            2A: {{ train.fare['2A'] }}
                        </td>
                        <td><a href="/book/{{ train.train_id }}" class="btn btn-book">Book Now</a></td>
                    </tr>
                    {% endfor %}
                {% else %}
                    <tr>
                        <td colspan="7" style="text-align: center; padding: 30px;">No trains found for the selected route.</td>
                    </tr>
                {% endif %}
            </tbody>
        </table>
        
        <div style="text-align: center; margin-top: 20px;">
            <a href="/search" class="btn btn-secondary">Search Again</a>
        </div>
    </div>
</main>
</body>
</html>
"""

BOOKING_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Railway Reservation System | Booking</title>
    <link rel="stylesheet" href="/styles.css"> 
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop
            </a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/search">Book Ticket</a></li>
                <li><a href="/cancel-ticket">Cancel Ticket</a></li>
                <li><a href="/logout">Logout</a></li>
            </ul>
        </div>
    </nav>

    <main class="main-content">
        <div class="form-card" style="max-width: 800px;">
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    {% for category, message in messages %}
                        <div class="message message-{{ 'success' if category == 'success' else 'error' }}">
                            {{ message }}
                        </div>
                    {% endfor %}
                {% endif %}
            {% endwith %}
            <h2 style="text-align: center; color: var(--primary-blue); margin-bottom: 30px;">Confirm Booking: {{ train.name }} ({{ train_id }})</h2>

            {% if train.seats.available == 0 %}
            <div class="message message-waiting-list" style="margin-bottom: 30px;">
                **Waiting List Alert:** No confirmed seats available. If you proceed, your ticket will be on waiting list.
            </div>
            {% endif %}
            
            <form id="booking-form" method="POST" action="/process-booking">
                <input type="hidden" name="train_id" value="{{ train_id }}">
                <input type="hidden" name="date" value="{{ request.args.get('date', '2025-10-15') }}">
                <h3 style="margin-bottom: 15px; color: #444;">Passenger Details</h3>
                
                <div id="passenger-container">
                    <div class="passenger-form" id="passenger-1" data-fare="2500" style="border: 1px solid var(--light-grey); padding: 15px; border-radius: 4px; margin-bottom: 15px;">
                        <h4 style="margin-bottom: 10px; color: var(--primary-blue);">Passenger 1</h4>
                        <div style="display: flex; gap: 20px; flex-wrap: wrap;">
                            <div class="form-group" style="flex: 3; min-width: 200px;">
                                <label for="passenger_name">Name</label>
                                <input type="text" name="passenger_name" id="passenger_name" required>
                            </div>
                            <div class="form-group" style="flex: 1; min-width: 80px;">
                                <label for="passenger_age">Age</label>
                                <input type="number" name="passenger_age" id="passenger_age" required>
                            </div>
                            <div class="form-group" style="flex: 1; min-width: 100px;">
                                <label for="passenger_gender">Gender</label>
                                <select name="passenger_gender" id="passenger_gender">
                                    <option>Male</option>
                                    <option>Female</option>
                                    <option>Other</option>
                                </select>
                            </div>
                            <div class="form-group" style="flex: 2; min-width: 200px;">
                                <label for="seat_type">Seat Type</label>
                                <select name="seat_type" id="seat_type" onchange="updateTotalFare()">
                                    <option value="SL">Sleeper (SL) - ₹{{ train.fare.SL }}</option>
                                    <option value="3A">AC 3 Tier (3A) - ₹{{ train.fare['3A'] }}</option>
                                    <option value="2A">AC 2 Tier (2A) - ₹{{ train.fare['2A'] }}</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>

                <div style="text-align: right; margin-top: 30px; padding-top: 20px; border-top: 1px dashed var(--light-grey);">
                    <h3 style="color: var(--danger-red); margin-bottom: 15px;">Total Ticket Fare: <span id="total-fare">₹{{ train.fare.SL }}</span></h3>
                    <button type="submit" class="btn btn-primary" style="padding: 15px 40px; font-size: 1.1em;">Confirm Booking</button>
                </div>
            </form>
        </div>
    </main>

    <script>
        const trainFares = {{ train.fare|tojson }};
        
        function updateTotalFare() {
            const seatTypeSelect = document.getElementById('seat_type');
            const selectedSeatType = seatTypeSelect.value;
            const fare = trainFares[selectedSeatType];
            document.getElementById('total-fare').textContent = `₹${fare}`;
        }

        // Initialize on page load
        updateTotalFare();
    </script>
</body>
</html>
"""

BOOKING_DETAILS_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NextStop | Booking Details</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop
            </a>
            <ul class="nav-links">
                <li><a href="/search">Book Tickets</a></li>
                <li><a href="/cancel-ticket">Cancel Ticket</a></li>
                <li><a href="/logout">Logout</a></li>
            </ul>
        </div>
    </nav>

    <main class="main-content">
        <div class="container">
            <div class="form-card" style="max-width: 700px;">
                <h2 style="text-align: center; color: var(--primary-blue); margin-bottom: 30px;">
                    🎫 Booking Confirmation
                </h2>
                
                <div style="background: linear-gradient(135deg, var(--primary-blue), #0056b3); color: white; padding: 20px; border-radius: 8px; margin-bottom: 30px; text-align: center;">
                    <h3 style="margin-bottom: 10px;">PNR: {{ pnr }}</h3>
                    <p style="font-size: 1.2em;">Status: 
                        <strong>
                            {% if booking.status == 'CONFIRMED' %}
                                ✅ CONFIRMED
                            {% elif booking.status.startswith('WL-') %}
                                ⏳ {{ booking.status }}
                            {% else %}
                                {{ booking.status }}
                            {% endif %}
                        </strong>
                    </p>
                </div>

                <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
                    <h4 style="color: var(--primary-blue); margin-bottom: 15px;">🚂 Journey Details</h4>
                    <p><strong>Train:</strong> {{ train.name }} ({{ booking.train_id }})</p>
                    <p><strong>Route:</strong> {{ train.route.source }} → {{ train.route.destination }}</p>
                    <p><strong>Date:</strong> {{ booking.date }}</p>
                    <p><strong>Departure:</strong> {{ train.departure }}</p>
                    <p><strong>Arrival:</strong> {{ train.arrival }}</p>
                </div>

                <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
                    <h4 style="color: var(--primary-blue); margin-bottom: 15px;">👥 Passenger Details</h4>
                    {% for passenger in booking.passengers %}
                        <div style="border-bottom: 1px dashed #ccc; padding-bottom: 10px; margin-bottom: 10px;">
                            <p><strong>{{ loop.index }}.</strong> {{ passenger.name }} ({{ passenger.age }}{{ passenger.gender[0] }})</p>
                            <p style="color: #666;">{{ passenger.seat_type }} Class</p>
                        </div>
                    {% endfor %}
                </div>

                <div style="background: #e8f5e8; padding: 20px; border-radius: 8px; margin-bottom: 20px; text-align: center;">
                    <h4 style="color: var(--success-green); margin-bottom: 10px;">💰 Fare Details</h4>
                    <p style="font-size: 1.2em;"><strong>Total Paid: ₹{{ booking.fare }}</strong></p>
                    <p style="color: #666; font-size: 0.9em;">Booking Date: {{ booking.booking_date }}</p>
                </div>

                {% if booking.status.startswith('WL-') %}
                <div class="message message-waiting-list">
                    <strong>Waiting List Information:</strong><br>
                    Your ticket is on waiting list. You will be notified if seats become available due to cancellations.
                </div>
                {% endif %}

                <div style="text-align: center; margin-top: 30px;">
                    <a href="/search" class="btn btn-primary" style="margin-right: 10px;">Book Another Ticket</a>
                    <a href="/cancel-ticket" class="btn btn-secondary">Cancel This Ticket</a>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
"""

CANCELLATION_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NextStop | Cancel Ticket</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop
            </a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/search">Book Ticket</a></li>
                <li><a href="/cancel-ticket">Cancel Ticket</a></li>
                {% if session.user_email %}
                    <li><a href="/logout">Logout</a></li>
                {% else %}
                    <li><a href="/login">Login</a></li>
                {% endif %}
            </ul>
        </div>
    </nav>

    <main class="main-content">
        <div class="form-card">
            <h2 style="text-align: center; color: var(--primary-blue); margin-bottom: 30px;">Cancel Ticket</h2>
            
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    {% for category, message in messages %}
                        <div class="message message-{{ 'success' if category == 'success' else 'error' }}">
                            {{ message }}
                        </div>
                    {% endfor %}
                {% endif %}
            {% endwith %}

            <div style="background: #fff3cd; border: 1px solid #ffeeba; border-left: 4px solid #ffc107; padding: 15px; border-radius: 4px; margin-bottom: 20px;">
                <strong>Cancellation Policy:</strong><br>
                • 80% refund for confirmed tickets<br>
                • Full refund for waitlisted tickets<br>
                • Refund processed within 5-7 working days
            </div>

            <form method="POST" action="/cancel-ticket">
                <div class="form-group">
                    <label for="pnr">PNR Number</label>
                    <input type="text" id="pnr" name="pnr" placeholder="Enter your PNR number" required>
                </div>
                
                <button type="submit" class="btn btn-primary" style="width: 100%;">Cancel Ticket</button>
            </form>

            <div style="text-align: center; margin-top: 20px;">
                <a href="/search" style="color: var(--primary-blue);">← Back to Booking</a>
            </div>
            
            <div style="margin-top: 20px; padding: 15px; background: #f8f9fa; border-radius: 4px; font-size: 0.85em; color: #666;">
                <strong>💡 Demo PNRs to try:</strong><br>
                PNR1234567 (John's confirmed booking)<br>
                PNR3456789 (Demo's waitlisted booking)
            </div>
        </div>
    </main>
</body>
</html>
"""

ADMIN_LOGIN_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NextStop | Admin Login</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop Admin
            </a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/login">User Login</a></li>
            </ul>
        </div>
    </nav>

    <main class="main-content">
        <div class="form-card">
            <h2 style="text-align: center; color: var(--primary-blue); margin-bottom: 30px;">🔐 Admin Login</h2>
            
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    {% for category, message in messages %}
                        <div class="message message-{{ 'success' if category == 'success' else 'error' }}">
                            {{ message }}
                        </div>
                    {% endfor %}
                {% endif %}
            {% endwith %}

            <form method="POST" action="/admin-login">
                <div class="form-group">
                    <label for="username">Admin Email</label>
                    <input type="email" id="username" name="username" placeholder="admin@nextstop.com" required>
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" placeholder="********" required>
                </div>
                <button type="submit" class="btn btn-primary" style="width: 100%;">Login as Admin</button>
            </form>

            <div style="background: #d1ecf1; border: 1px solid #bee5eb; padding: 15px; border-radius: 4px; margin-top: 20px;">
                <strong>Demo Credentials:</strong><br>
                Email: admin@nextstop.com<br>
                Password: admin123
            </div>
        </div>
    </main>
</body>
</html>
"""

ADMIN_DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NextStop | Admin Dashboard</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop Admin
            </a>
            <ul class="nav-links">
                <li><a href="/admin">Dashboard</a></li>
                <li><a href="/admin/bookings">Bookings</a></li>
                <li><a href="/admin/reports">Reports</a></li>
                <li><a href="/logout">Logout</a></li>
            </ul>
        </div>
    </nav>

    <main class="main-content">
        <div class="container">
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    {% for category, message in messages %}
                        <div class="message message-{{ 'success' if category == 'success' else 'error' }}">
                            {{ message }}
                        </div>
                    {% endfor %}
                {% endif %}
            {% endwith %}

            <h1 style="color: var(--primary-blue); margin-bottom: 30px;">🏛️ Admin Dashboard</h1>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 40px;">
                <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-align: center;">
                    <h3 style="color: var(--primary-blue);">📊 View Reports</h3>
                    <p>Revenue and booking analytics</p>
                    <a href="/admin/reports" class="btn btn-primary">View Reports</a>
                </div>
                
                <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-align: center;">
                    <h3 style="color: var(--primary-blue);">📋 Manage Bookings</h3>
                    <p>View and manage all bookings</p>
                    <a href="/admin/bookings" class="btn btn-primary">Manage Bookings</a>
                </div>
                
                <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-align: center;">
                    <h3 style="color: var(--primary-blue);">⏳ Waiting List</h3>
                    <p>Manage waiting list passengers</p>
                    <a href="/admin/waiting-list" class="btn btn-primary">View Waiting List</a>
                </div>
            </div>

            <div style="background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-top: 30px;">
                <h3 style="color: var(--primary-blue); margin-bottom: 20px;">🚂 Current Trains</h3>
                <div class="data-table">
                    <table style="width: 100%;">
                        <thead>
                            <tr>
                                <th>Train ID</th>
                                <th>Name</th>
                                <th>Route</th>
                                <th>Timing</th>
                                <th>Seats</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for train_id, train in trains.items() %}
                            <tr>
                                <td>{{ train_id }}</td>
                                <td>{{ train.name }}</td>
                                <td>{{ train.route.source }} → {{ train.route.destination }}</td>
                                <td>{{ train.departure }} - {{ train.arrival }}</td>
                                <td>{{ train.seats.available }}/{{ train.seats.total }}</td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
"""

ADMIN_TRAINS_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NextStop | Admin Trains</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop Admin
            </a>
            <ul class="nav-links">
                <li><a href="/admin">Dashboard</a></li>
                <li><a href="/admin/trains">Trains</a></li>
                <li><a href="/admin/bookings">Bookings</a></li>
                <li><a href="/logout">Logout</a></li>
            </ul>
        </div>
    </nav>

    <main class="main-content">
        <div class="container">
            <h2 style="color: var(--primary-blue); margin-bottom: 20px;">🚂 Train Management</h2>
            
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Train ID</th>
                        <th>Name</th>
                        <th>Route</th>
                        <th>Departure</th>
                        <th>Arrival</th>
                        <th>Available Seats</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {% for train_id, train in trains.items() %}
                    <tr>
                        <td>{{ train_id }}</td>
                        <td>{{ train.name }}</td>
                        <td>{{ train.route.source }} → {{ train.route.destination }}</td>
                        <td>{{ train.departure }}</td>
                        <td>{{ train.arrival }}</td>
                        <td>{{ train.seats.available }}/{{ train.seats.total }}</td>
                        <td>
                            <span style="
                                {% if train.status == 'Active' %}color: var(--success-green);
                                {% else %}color: var(--danger-red);{% endif %}
                                font-weight: bold;">
                                {{ train.status }}
                            </span>
                        </td>
                        <td>
                            <form method="POST" action="/admin/update-train-status" style="display: inline;">
                                <input type="hidden" name="train_id" value="{{ train_id }}">
                                <select name="status" style="padding: 5px; border: 1px solid #ddd; border-radius: 4px;">
                                    <option value="Active" {% if train.status == 'Active' %}selected{% endif %}>Active</option>
                                    <option value="Inactive" {% if train.status == 'Inactive' %}selected{% endif %}>Inactive</option>
                                    <option value="Maintenance" {% if train.status == 'Maintenance' %}selected{% endif %}>Maintenance</option>
                                </select>
                                <button type="submit" class="btn btn-sm btn-primary" style="margin-left: 5px;">Update</button>
                            </form>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
            
            <div style="text-align: center; margin-top: 20px;">
                <a href="/admin" class="btn btn-secondary">← Back to Dashboard</a>
            </div>
        </div>
    </main>
</body>
</html>
"""

ADMIN_BOOKINGS_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NextStop | Admin Bookings</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop Admin
            </a>
            <ul class="nav-links">
                <li><a href="/admin">Dashboard</a></li>
                <li><a href="/admin/bookings">Bookings</a></li>
                <li><a href="/admin/reports">Reports</a></li>
                <li><a href="/logout">Logout</a></li>
            </ul>
        </div>
    </nav>

    <main class="main-content">
        <div class="container">
            <h2 style="color: var(--primary-blue); margin-bottom: 20px;">📋 All Bookings</h2>
            
            <table class="data-table">
                <thead>
                    <tr>
                        <th>PNR</th>
                        <th>Train</th>
                        <th>User Email</th>
                        <th>Date</th>
                        <th>Passengers</th>
                        <th>Fare</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {% if bookings %}
                        {% for booking in bookings %}
                        <tr>
                            <td>{{ booking.pnr }}</td>
                            <td>{{ booking.train_name }} ({{ booking.train_id }})</td>
                            <td>{{ booking.user_email }}</td>
                            <td>{{ booking.date }}</td>
                            <td>{{ booking.passengers }}</td>
                            <td>₹{{ booking.fare }}</td>
                            <td>
                                <span style="
                                    {% if booking.status == 'CONFIRMED' %}color: var(--success-green);
                                    {% elif booking.status == 'CANCELED' %}color: var(--danger-red);
                                    {% else %}color: #856404;{% endif %}
                                    font-weight: bold;">
                                    {{ booking.status }}
                                </span>
                            </td>
                        </tr>
                        {% endfor %}
                    {% else %}
                        <tr>
                            <td colspan="7" style="text-align: center; padding: 30px;">No bookings found.</td>
                        </tr>
                    {% endif %}
                </tbody>
            </table>
            
            <div style="text-align: center; margin-top: 20px;">
                <a href="/admin" class="btn btn-secondary">← Back to Dashboard</a>
            </div>
        </div>
    </main>
</body>
</html>
"""

ADMIN_REPORTS_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NextStop | Admin Reports</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop Admin
            </a>
            <ul class="nav-links">
                <li><a href="/admin">Dashboard</a></li>
                <li><a href="/admin/bookings">Bookings</a></li>
                <li><a href="/admin/reports">Reports</a></li>
                <li><a href="/logout">Logout</a></li>
            </ul>
        </div>
    </nav>

    <main class="main-content">
        <div class="container">
            <h2 style="color: var(--primary-blue); margin-bottom: 30px;">📊 Revenue & Analytics Report</h2>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 30px;">
                <div style="background: linear-gradient(135deg, var(--success-green), #1e7e34); color: white; padding: 20px; border-radius: 8px; text-align: center;">
                    <h3 style="margin-bottom: 10px;">💰 Total Revenue</h3>
                    <p style="font-size: 2em; font-weight: bold;">₹{{ "{:,}".format(report.total_revenue) }}</p>
                </div>
                
                <div style="background: linear-gradient(135deg, var(--primary-blue), #0056b3); color: white; padding: 20px; border-radius: 8px; text-align: center;">
                    <h3 style="margin-bottom: 10px;">📋 Total Bookings</h3>
                    <p style="font-size: 2em; font-weight: bold;">{{ report.total_bookings }}</p>
                </div>
                
                <div style="background: linear-gradient(135deg, #28a745, #1e7e34); color: white; padding: 20px; border-radius: 8px; text-align: center;">
                    <h3 style="margin-bottom: 10px;">✅ Confirmed</h3>
                    <p style="font-size: 2em; font-weight: bold;">{{ report.confirmed_bookings }}</p>
                </div>
                
                <div style="background: linear-gradient(135deg, #ffc107, #e0a800); color: white; padding: 20px; border-radius: 8px; text-align: center;">
                    <h3 style="margin-bottom: 10px;">⏳ Waiting List</h3>
                    <p style="font-size: 2em; font-weight: bold;">{{ report.waiting_bookings }}</p>
                </div>
                
                <div style="background: linear-gradient(135deg, var(--danger-red), #c82333); color: white; padding: 20px; border-radius: 8px; text-align: center;">
                    <h3 style="margin-bottom: 10px;">❌ Canceled</h3>
                    <p style="font-size: 2em; font-weight: bold;">{{ report.canceled_bookings }}</p>
                </div>
            </div>

            <div style="background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <h3 style="color: var(--primary-blue); margin-bottom: 20px;">📈 Summary</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
                    <div>
                        <h4 style="color: #666; margin-bottom: 10px;">Booking Success Rate</h4>
                        <p style="font-size: 1.2em; font-weight: bold; color: var(--success-green);">
                            {% if report.total_bookings > 0 %}
                                {{ "%.1f"|format((report.confirmed_bookings / report.total_bookings) * 100) }}%
                            {% else %}
                                0.0%
                            {% endif %}
                        </p>
                    </div>
                    
                    <div>
                        <h4 style="color: #666; margin-bottom: 10px;">Average Revenue per Booking</h4>
                        <p style="font-size: 1.2em; font-weight: bold; color: var(--primary-blue);">
                            {% if report.total_bookings > 0 %}
                                ₹{{ "%.2f"|format(report.total_revenue / report.total_bookings) }}
                            {% else %}
                                ₹0.00
                            {% endif %}
                        </p>
                    </div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 30px;">
                <a href="/admin" class="btn btn-secondary">← Back to Dashboard</a>
                <button onclick="window.print()" class="btn btn-primary" style="margin-left: 10px;">🖨️ Print Report</button>
            </div>
        </div>
    </main>
</body>
</html>
"""

ADMIN_WAITINGLIST_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NextStop | Waiting List</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container nav-content">
            <a href="/" class="logo">
                <img src="/static/logo.jpg" alt="NextStop Logo">
                NextStop Admin
            </a>
            <ul class="nav-links">
                <li><a href="/admin">Dashboard</a></li>
                <li><a href="/admin/bookings">Bookings</a></li>
                <li><a href="/admin/reports">Reports</a></li>
                <li><a href="/logout">Logout</a></li>
            </ul>
        </div>
    </nav>

    <main class="main-content">
        <div class="container">
            <h2 style="color: var(--primary-blue); margin-bottom: 20px;">⏳ Waiting List Management</h2>
            
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Train</th>
                        <th>PNR</th>
                        <th>Passenger Name</th>
                        <th>WL Position</th>
                    </tr>
                </thead>
                <tbody>
                    {% if waiting_list %}
                        {% for wl in waiting_list %}
                        <tr>
                            <td>{{ wl.train_name }} ({{ wl.train_id }})</td>
                            <td>{{ wl.pnr }}</td>
                            <td>{{ wl.passenger_name }}</td>
                            <td style="font-weight: bold; color: #856404;">WL-{{ wl.position }}</td>
                        </tr>
                        {% endfor %}
                    {% else %}
                        <tr>
                            <td colspan="4" style="text-align: center; padding: 30px;">No passengers in waiting list.</td>
                        </tr>
                    {% endif %}
                </tbody>
            </table>
            
            <div style="text-align: center; margin-top: 20px;">
                <a href="/admin" class="btn btn-secondary">← Back to Dashboard</a>
            </div>
        </div>
    </main>
</body>
</html>
"""