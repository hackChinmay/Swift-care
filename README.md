# SwiftCare - Mobile Healthcare System

SwiftCare is a comprehensive mobile healthcare platform designed to bring healthcare services right to the user's doorstep. With this platform, patients can book appointments, schedule health camps, request ICU on wheels, and even manage blood donations – all from the comfort of their home. Powered by an AI chatbot integrated with OpenAI's GPT model, the platform provides intelligent responses to common questions and offers a seamless healthcare experience.

---

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)

---

## Project Description

SwiftCare is a user-friendly healthcare web application aimed at simplifying the process of receiving medical care. Whether a user needs general health checkups, an ICU on wheels, or blood donation services, SwiftCare allows users to access a range of medical services from their devices. With its easy-to-use interface, detailed forms, and real-time chatbot support, it caters to patients seeking convenient healthcare services.

Key features include:
- A healthcare services dashboard
- Booking options for general health checkups, blood donations, ICU on wheels, and health camps
- AI-powered chatbot for healthcare-related inquiries
- User authentication (Sign-in and Sign-up functionality)
- Mobile-responsive design
- Customizable and secure

---

## Features

- **General Health Checkup**: Users can book checkups directly through the app.
- **Blood Donation**: Patients can request blood or donate blood with a structured form to ensure all necessary details are collected.
- **ICU on Wheels**: Emergency ICU services can be booked to reach the patient's location.
- **Health Camp**: Users can book and schedule health camps for their community.
- **AI Chatbot**: A ChatGPT-powered assistant integrated to assist users with general queries and guide them through the process.
- **Session Management**: Secure session handling with automatic timeout.
- **Admin**: Admin control for managing users, services, and hospitals (optional feature to expand).
- **User-friendly Interface**: Simple and responsive design that works seamlessly across devices.

---

## Technologies Used

- **Backend**: Flask (Python) for the server-side logic
- **Frontend**: HTML5, CSS3, Bootstrap for styling, Google Fonts for typography
- **Database**: SQLite for data storage (user info, hospital data, etc.)
- **Chatbot**: OpenAI GPT-3.5 integration for the AI chatbot functionality
- **Session Management**: Flask session for handling user login/logout with timeouts
- **Authentication**: User sign-up and login system

---

## Project Structure

```bash
SwiftCare/
│
├── app.py              # Flask application main file
├── chatbot.py          # Chatbot logic and OpenAI integration
├── instance/
│   └── users.db        # SQLite database file for storing user and service data
├── static/
│   ├── css/
│   │   └── styles.css  # Custom CSS file for the project
│   ├── images/ 
│   │   ├── ACC.jpeg
│   │   ├── ministry_of_health.svg
│   │   └── national_health_mission.png
│   └── js/             # Optional JS files if needed
├── templates/
│   ├── about.html      # About Us page
│   ├── appointment_booking.html      # Appointment Booking Page
│   ├── appointment_confirmation.html      # Appointment Booking Confirmation Page
│   ├── blood_donation_confirmation.html      # Blood Donation Confirmation Page
│   ├── blood_donation.html      # Blood Donation Page
│   ├── final_health_camp_confirmation.html      # Health Camp Final Confirmation Page
│   ├── general_health_checkup.html      # General Health Checkup Page
│   ├── health_camp_confirmation.html      # Health Camp Confirmation Page
│   ├── health_camp.html      # Health Camp Page
│   ├── icu_on_wheel_confirmation.html      # ICU On Wheels Confirmation Page
│   ├── icu_on_wheel.html      # ICU On Wheels Page
│   ├── landing.html      # Landing Page
│   ├── login_signup.html      # Login and Signup Page
│   └── signup.html      # Signup Page
├── .env                # Environment variables file (for API keys)
├── .gitignore          # Git ignore file to exclude certain files from being tracked by git
├── requirements.txt    # Python dependencies
└── README.md           # Project README file
```

---

## Installation

To setup this project on your local machine:

### Prerequisites

- Python 3.x
- Flask
- SQLite3
- OpenAI API Key

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/SwiftCare.git
   ```

2. Navigate to the project directory:
    ```bash
    cd Swift-care
    ```

3. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up the SQLite databases:
    - Create the users.db for user login information
    ```bash
    sqlite3 instance/users.db
    ```

6. Setup the .env file:
    - Create a .env file in the root directory and add your OpenAI API key:
    ```makefile
    OPENAI_API_KEY=your-openai-api-key
    ```

7. Run the Flask application:
    ```bash
    python app.py
    ```

---

## Usage

- **Sign up and login**: Users need to sign up and log in to access the main platform.
- **Healthcare services**: Users can book different services such as health checkups, blood donations, or ICU on wheels.
- **Chatbot**: Use the AI chatbot to ask healthcare-related questions or general queries about the services.
- **Back button functionality**: Navigate back to the home page with ease after exploring different services.

---

## Screenshots



---

## Future Enhancements

- **Admin dashboard**: A dashboard for admins to manage user data, services, and hospitals.
- **Integration with external APIs**: Connect with healthcare databases or local hospitals for real-time data.
- **Payment gateway integration**: Include options for users to make payments for premium services.
- **Expanded chatbot functionality**: Add more context-specific features for the AI assistant to improve the user experience.

---

## Contributors

- [Chinmay (Project Lead)](https://github.com/Hxzardd)
- [Darsheel](https://github.com/Hxzardd)
- [Anshul Gupta](https://github.com/Hxzardd)
- [Vimal](https://github.com/Hxzardd)
- [Kshitij](https://github.com/Hxzardd)
- [Jegan](https://github.com/Hxzardd)

