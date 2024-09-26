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
- [License](#license)

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
│   ├── users.db        # SQLite database file for storing user and service data
│   └── college_info.db # Database file for college-specific chatbot queries
├── static/
│   ├── css/
│   │   └── styles.css  # Custom CSS file for the project
│   ├── images/         # Images used across the platform
│   └── js/             # Optional JS files if needed
├── templates/
│   ├── about.html      # About Us page
│   ├── landing.html    # Main landing page after login
│   ├── login_signup.html # Login and Signup page
│   ├── health_camp.html  # Health Camp booking form
│   ├── health_camp_confirmation.html  # Health Camp confirmation page
│   ├── icu_on_wheel.html   # ICU on Wheel request form
│   ├── blood_donation.html # Blood Donation form
│   └── final_health_camp_confirmation.html  # Final confirmation page for Health Camp
├── .env                # Environment variables file (for API keys)
├── requirements.txt    # Python dependencies
└── README.md           # Project README file
