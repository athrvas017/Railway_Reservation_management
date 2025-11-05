"""
CSS Styles Module
Contains all CSS styling for the application
"""

CSS_STYLES = """
/* Modern Reset */
* { box-sizing: border-box; }
html, body { height: 100%; }
body {
  margin: 0;
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  line-height: 1.6;
  color: #0f172a; /* slate-900 */
  background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
}

/* Color System */
:root {
  --primary-blue: #0f62fe; /* IBM blue */
  --primary-blue-dark: #0043ce;
  --secondary-grey: #64748b; /* slate-500 */
  --white: #ffffff;
  --light-grey: #e2e8f0; /* slate-200 */
  --muted: #94a3b8; /* slate-400 */
  --success-green: #16a34a; /* green-600 */
  --danger-red: #dc2626; /* red-600 */
  --warning-amber: #f59e0b; /* amber-500 */
  --card-bg: #ffffffcc;
  --shadow: 0 10px 30px rgba(2, 6, 23, 0.08);
}

/* Utility Classes */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 15px;
}

/* Navigation Bar */
.navbar {
  background: linear-gradient(90deg, var(--primary-blue-dark), var(--primary-blue));
  padding: 14px 0;
  position: sticky;
  top: 0;
  z-index: 50;
  box-shadow: 0 6px 20px rgba(15, 23, 42, 0.08);
}

.nav-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
  color: var(--white);
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: .3px;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo img {
    height: 40px;
    width: auto;
    border-radius: 4px;
}

.nav-links {
    list-style: none;
    display: flex;
}

.nav-links li {
    margin-left: 20px;
}

.nav-links a {
    color: var(--white);
    text-decoration: none;
    padding: 5px 10px;
    transition: background-color 0.3s, color 0.3s;
    border-radius: 4px;
}

.nav-links a:hover {
    background-color: rgba(255, 255, 255, 0.1);
}

/* Main Content */
.main-content {
  padding: 48px 0;
  min-height: calc(100vh - 80px);
}

/* Forms */
.form-card {
  background: var(--card-bg);
  backdrop-filter: saturate(180%) blur(6px);
  padding: 36px;
  max-width: 760px;
  margin: 32px auto;
  border-radius: 14px;
  border: 1px solid var(--light-grey);
  box-shadow: var(--shadow);
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: var(--secondary-grey);
}

.form-group input[type="text"],
.form-group input[type="email"],
.form-group input[type="password"],
.form-group input[type="date"],
.form-group input[type="number"],
.form-group select {
    width: 100%;
    padding: 12px;
    border: 1px solid var(--light-grey);
    border-radius: 4px;
    font-size: 1em;
    transition: border-color 0.3s;
}

.form-group input:focus,
.form-group select:focus {
    border-color: var(--primary-blue);
    outline: none;
}

/* Buttons */
.btn {
    display: inline-block;
    padding: 12px 25px;
    font-size: 1em;
    font-weight: 600;
    cursor: pointer;
    border: none;
    border-radius: 4px;
    transition: background-color 0.3s, transform 0.1s;
    text-decoration: none;
    text-align: center;
}

.btn-primary {
  background: linear-gradient(180deg, var(--primary-blue), var(--primary-blue-dark));
  color: var(--white);
}

.btn-primary:hover {
  filter: brightness(1.05);
  transform: translateY(-1px);
}

.btn-secondary {
    background-color: var(--secondary-grey);
    color: var(--white);
}

.btn-secondary:hover {
    background-color: #5a6268;
}

.btn-book {
    background-color: var(--success-green);
    color: var(--white);
    padding: 8px 15px;
    font-size: 0.9em;
}

.btn-book:hover {
    background-color: #1e7e34;
}

.btn-add {
    background-color: var(--secondary-grey);
    color: var(--white);
    padding: 10px 20px;
    margin-top: 15px;
    display: block;
    width: fit-content;
}

.btn-add:hover {
    background-color: #5a6268;
}

/* Tables */
.data-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  background-color: var(--white);
  box-shadow: var(--shadow);
  border-radius: 12px;
  overflow: hidden;
}

.data-table th, .data-table td {
    padding: 15px;
    text-align: left;
    border-bottom: 1px solid var(--light-grey);
}

.data-table th {
  background: linear-gradient(90deg, var(--primary-blue-dark), var(--primary-blue));
  color: var(--white);
  font-weight: 700;
  text-transform: uppercase;
  font-size: 0.85em;
  letter-spacing: .4px;
}

.data-table tr:hover {
    background-color: #f8f9fa;
}

.data-table tbody tr:last-child td {
    border-bottom: none;
}

/* Admin Dashboard */
.admin-dashboard {
    display: flex;
}

.sidebar {
    width: 250px;
    background-color: #343a40;
    padding: 20px;
    height: calc(100vh - 80px);
}

.sidebar ul {
    list-style: none;
}

.sidebar li {
    margin-bottom: 15px;
}

.sidebar a {
    color: var(--white);
    text-decoration: none;
    display: block;
    padding: 10px;
    border-radius: 4px;
    transition: background-color 0.3s;
}

.sidebar a:hover, .sidebar a.active {
    background-color: var(--primary-blue);
}

.dashboard-content {
    flex-grow: 1;
    padding: 40px;
}

.dashboard-content h2 {
    margin-bottom: 20px;
    color: var(--primary-blue);
}

/* Messages */
.message {
  padding: 14px 16px;
  border-radius: 10px;
  margin: 18px auto;
  font-weight: 600;
  text-align: center;
  max-width: 720px;
  box-shadow: var(--shadow);
}

.message-success {
    background-color: #d4edda;
    color: var(--success-green);
    border: 1px solid #c3e6cb;
    border-left: 4px solid var(--success-green);
}

.message-error {
    background-color: #f8d7da;
    color: var(--danger-red);
    border: 1px solid #f5c6cb;
    border-left: 4px solid var(--danger-red);
}

.message-waiting-list {
    background-color: #fff3cd;
    color: #856404;
    border: 1px solid #ffeeba;
    border-left: 4px solid #ffc107;
}

.message-info {
    background-color: #d1ecf1;
    color: #0c5460;
    border: 1px solid #bee5eb;
    border-left: 4px solid #17a2b8;
}

/* Responsive Design */
@media (max-width: 768px) {
    .nav-content {
        flex-direction: column;
        align-items: flex-start;
    }

    .nav-links {
        margin-top: 10px;
        flex-direction: column;
        width: 100%;
    }

    .nav-links li {
        margin: 5px 0;
        width: 100%;
    }

    .nav-links a {
        display: block;
        text-align: center;
    }

    .form-card {
        padding: 20px;
        margin: 20px auto;
    }

    .data-table th, .data-table td {
        padding: 10px;
        font-size: 0.9em;
    }
}
"""