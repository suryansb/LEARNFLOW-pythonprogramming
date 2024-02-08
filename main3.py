import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

def send_email(subject, body, to_email):
    # Email Configuration
    sender_email = "suryansbarmecha@gmail.com"
    sender_password = "9813438460"
    
    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject
    
    # Attach body to the email
    message.attach(MIMEText(body, 'plain'))
    
    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send email
        server.send_message(message)

def compose_and_send_email():
    # Compose Email
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")
    to_email = input("Enter the recipient's email address: ")

    # Send Email
    send_email(subject, body, to_email)
    print("Email sent successfully!")

# Schedule the email to be sent every day at a specific time
schedule.every().day.at("22:22").do(compose_and_send_email)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
