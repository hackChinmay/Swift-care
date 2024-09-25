from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from datetime import timedelta, datetime
import sqlite3
from chatbot import college_chatbot  # Import the chatbot function

app = Flask(__name__)
app.secret_key = 'l'

# Set the session lifetime duration (e.g., 20 minutes of inactivity)
SESSION_TIMEOUT = timedelta(seconds=1200)

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

# Decorator to check if the user is logged in and session has not expired
def login_required(f):
    def wrapper(*args, **kwargs):
        # Check if the user is logged in
        if 'username' not in session:
            return redirect(url_for('signin'))
        
        # Check if session has expired
        last_activity = session.get('last_activity')
        if last_activity is not None:
            now = datetime.now()
            last_activity_time = datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S')
            if now - last_activity_time > SESSION_TIMEOUT:
                session.pop('username', None)
                flash('Your session has timed out. Please log in again.')
                return redirect(url_for('signin'))
        
        # Update last activity time
        session['last_activity'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

# Redirect the root page to the signin page
@app.route('/')
def home():
    return redirect(url_for('signin'))

# Route for "Landing" page (this will now be protected by login)
@app.route('/landing')
@login_required
def landing_page():
    return render_template('landing.html')

# Route for "About" page (protected by login)
@app.route('/about')
@login_required
def about():
    return render_template('about.html')

# Route for "Program" page (protected by login)
@app.route('/program')
@login_required
def program():
    return render_template('program.html')

# Route for "General Health Checkup" page (protected by login)
@app.route('/general-health-checkup')
@login_required
def general_health_checkup():
    return render_template('general_health_checkup.html')

# Route for specific doctor's appointment booking (protected by login)
@app.route('/book_doctor/<doctor_name>', methods=['GET', 'POST'])
@login_required
def book_doctor(doctor_name):
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        age = request.form['age']
        blood_group = request.form['blood_group']
        address = request.form['address']
        
        # Render the confirmation page with all details
        return render_template('appointment_confirmation.html', 
                               doctor_name=doctor_name, 
                               patient_name=patient_name,
                               age=age, 
                               blood_group=blood_group, 
                               address=address)
    
    # Render the appointment booking page with the doctor's name
    return render_template('appointment_booking.html', doctor_name=doctor_name)

# Route for "Health Camp" page (protected by login)
@app.route('/health-camp')
@login_required
def health_camp():
    return render_template('health_camp.html')

# Route for handling Health Camp booking confirmation (protected by login)
@app.route('/confirm_health_camp', methods=['POST'])
@login_required
def confirm_health_camp():
    purpose = request.form['purpose']
    target_population = request.form['target_population']
    date_venue = request.form['date_venue']
    address = request.form['address']

    return render_template('health_camp_confirmation.html', purpose=purpose, date_venue=date_venue, address=address)

# Route for final health camp confirmation page
@app.route('/final_health_camp_confirmation', methods=['POST'])
@login_required
def final_health_camp_confirmation():
    return render_template('final_health_camp_confirmation.html')

# Route for "Blood Donation" page (protected by login)
@app.route('/blood-donation')
@login_required
def blood_donation():
    return render_template('blood_donation.html')

# Route for handling blood donation form submission
@app.route('/confirm_blood_donation', methods=['POST'])
@login_required
def confirm_blood_donation():
    patient_name = request.form['patient_name']
    age = request.form['age']
    blood_component = request.form['blood_component']
    diagnosis = request.form['diagnosis']
    doctor_name = request.form['doctor_name']
    doctor_contact = request.form['doctor_contact']
    delivery_method = request.form['delivery_method']
    
    # Handle logic to store the data or process it (e.g., saving to database)

    # For now, let's just render a confirmation page
    return render_template('blood_donation_confirmation.html', 
                           patient_name=patient_name,
                           age=age, 
                           blood_component=blood_component, 
                           diagnosis=diagnosis, 
                           doctor_name=doctor_name, 
                           doctor_contact=doctor_contact, 
                           delivery_method=delivery_method)

# Route for "ICU On Wheel" page (protected by login)
@app.route('/icu-on-wheel')
@login_required
def icu_on_wheel():
    return render_template('icu_on_wheel.html')

# Route for handling ICU on Wheel form submission
@app.route('/confirm_icu_on_wheel', methods=['POST'])
@login_required
def confirm_icu_on_wheel():
    purpose = request.form['purpose']
    equipment = request.form['equipment']
    personnel = request.form['personnel']
    protocols = request.form['protocols']
    patient_name = request.form['patient_name']
    contact_info = request.form['contact_info']
    address = request.form['address']
    
    # Handle logic to store the data or process it (e.g., saving to database)
    
    # For now, let's just render a confirmation page
    return render_template('icu_on_wheel_confirmation.html', 
                           purpose=purpose, 
                           equipment=equipment, 
                           personnel=personnel, 
                           protocols=protocols, 
                           patient_name=patient_name, 
                           contact_info=contact_info, 
                           address=address)

# Chatbot Route
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('question')
    response = college_chatbot(user_input)
    return jsonify({"response": response})

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
            session['last_activity'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Track last activity
            return redirect(url_for('landing_page'))
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

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('signin'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
