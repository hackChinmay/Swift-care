from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('instance/users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database
def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Serve the landing page at the home route
@app.route('/')
def landing_page():
    return render_template('landing.html')

# Route for "About" page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for "Program" page
@app.route('/program')
def program():
    return render_template('program.html')

# Route for "General Health Checkup" page
@app.route('/general-health-checkup')
def general_health_checkup():
    return render_template('general_health_checkup.html')

# Route for specific doctor's appointment booking
@app.route('/book_doctor/<doctor_name>', methods=['GET', 'POST'])
def book_doctor(doctor_name):
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        age = request.form['age']
        blood_group = request.form['blood_group']
        address = request.form['address']
        
        # Here, you can handle saving the appointment data to the database
        return f'Appointment with {doctor_name} for {patient_name} booked successfully!'
    
    # Render the appointment booking page with the doctor's name
    return render_template('appointment_booking.html', doctor_name=doctor_name)

# Route for Appointment Booking (POST submission handler)
@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    patient_name = request.form['patient_name']
    age = request.form['age']
    blood_group = request.form['blood_group']
    address = request.form['address']
    
    # You can add logic here to save appointment data to a database or perform other actions
    return f'Appointment for {patient_name} booked successfully!'

# Route for "Health Camp" page
@app.route('/health-camp')
def health_camp():
    return render_template('health_camp.html')

# Route for "Blood Donation" page
@app.route('/blood-donation')
def blood_donation():
    return render_template('blood_donation.html')

# Route for "ICU On Wheel" page
@app.route('/icu-on-wheel')
def icu_on_wheel():
    return render_template('icu_on_wheel.html')

# Signin route for login form
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        
        if user:
            session['username'] = username
            return 'Logged in successfully!'
        else:
            flash('Invalid credentials, please try again.')
            return redirect(url_for('signin'))
    
    return render_template('login_signup.html')

# Signup route for creating a new account
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        
        flash('Account created successfully! Please log in.')
        return redirect(url_for('signin'))
    
    return render_template('signup.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
