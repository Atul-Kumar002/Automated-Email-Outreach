# Automated Email Outreach (CLI)
A Python-based automation tool that sends personalized internship/job application emails using structured CSV data and secure Gmail SMTP authentication.
This project demonstrates real-world automation, data preprocessing, secure credential management, and scalable email workflow design.

# Features
CSV-based HR contact processing
Secure authentication using environment variables
Automatic resume attachment
Built-in rate limiting to reduce spam risk
CSV column sanitization & validation
Invalid email and incomplete row handling
Success tracking and progress metrics

# Tech Stack
Python
Pandas
Yagmail (SMTP)
Environment Variables for Security

# Project Structure
##### Automated-Email-Outreach/
##### │
##### ├── send_mails.py
##### ├── HR_list_sample.csv
##### ├── requirements.txt
##### ├── README.md
##### └── .gitignore

# Installation & Setup
## 1️⃣ Clone the Repository
git clone https://github.com/Atul-Kumar002/Automated-Email-Outreach.git
## 2️⃣ Install Dependencies
pip install -r requirements.txt
## 3️⃣ Set Environment Variables
For security reasons, email credentials are not stored in the code.

Windows (PowerShell):
setx EMAIL "your_email@gmail.com"
setx APP_PASSWORD "your_16_character_app_password"

Restart your terminal after setting these.

## 4️⃣ Prepare CSV File

Ensure your CSV follows this format:

name,email,company
John Smith,john.smith@example.com,ABC Technologies
Sarah Lee,sarah.lee@example.com,Innovate Solutions

Only three required columns:
name
email
company

## 5️⃣ Run the Script
python send_mails.py
The script will:
Validate CSV structure
Skip invalid emails
Attach resume automatically
Send emails with delay control
Display success summary

# Disclaimer

This project is intended for educational and automation purposes. Users are responsible for complying with email communication guidelines and ethical outreach practices.

# Author

Developed as a practical automation project demonstrating Python scripting, data handling, and secure system integration.
