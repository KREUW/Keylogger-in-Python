# Keylogger & Email


 ## Description

This Python script demonstrates the use of various programming concepts and libraries to achieve a specific functionality: a keystroke logger that captures all keyboard activity, logs it to a file, and then sends the contents of that file to a specified email address once a day. The script uses the pynput library to capture keystrokes, the schedule library to schedule tasks, and the smtplib library to deliver emails. This project is designed to be instructive, demonstrating how to programmatically monitor keyboard input, handle scheduled tasks, and send emails using a Python script.
<br />

 ## What I learned

   ### During the development of this project, I improved my understanding of some essential areas of Python programming and libary use cases to include:

- <b>Keyboard Event Monitoring:</b> Using the pynput package to listen for and record keyboard events in real time.
- <b>Task Scheduling:</b> Using the schedule module to run certain functions at predefined times, allowing for automated tasks within a Python script.
- <b>Email Handling in Python:</b> Use smtplib and MIME standards to construct and send emails programmatically, including plaintext and multipart communications.
- <b>File I/O Operations:</b> Managing file operations for logging data and comprehending the significance of flushing buffers to ensure data integrity.
- <b>Environmental Variables:</b> The significance of using environmental variables to securely manage sensitive information such as email credentials in scripts.


 ## Languages and Utilities Used 

- Python
- Visual Studio Code <br />

 ## Environments Used

- Windows 11

 ## Challenges

   ### Several problems were faced and solved during the development of this keystroke logger to include:

Efficient Data Logging: Ensure that the script logs keystrokes without consuming too many system resources or producing perceptible lag in user input.
Handling special keys: Creating a technique for logging special keystrokes (such as Shift, Ctrl, etc.) in an instructive and readable format.
Secure Email Transmission: Setting up smtplib to transmit emails securely over TLS, as well as securely handling email credentials without hardcoding them into the script.
Scheduling Precision: Setting up the scheduler to perform the email function at the same time every day, while accounting for the computer's sleep state and potential script interrupts.


 ## Script Explanatoin:

  ### Libraries: 
  These lines import the Python libraries required for job scheduling, time and date management, keyboard input tracking, and email sending. <br/>
![1](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/ebb76d24-14bc-4e85-9aef-99ba4bdcd69a)

  ### Sending Emails:
  
  Defines the function 'send_email' which accepts a subject and body for the email to be sent. <br/>
![2](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/1c5f9554-df2e-4572-abba-e80f6b8d8bf8)

  Sets the sender's and recipient's email addresses, as well as the sender's password. These should be changed with correct email addresses and passwords. <br/>
![3](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/8261d793-2434-48f9-8fe5-0400ab1a0c67)

  Creates an email message with the given subject and body. The body is set to plain text. <br/>
![4](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/1d1a7e82-f42b-41b7-99cd-45ea5fb648f7)

  Connects to Gmail's SMTP server, logs in using the sender's email and password, sends the email, and then terminates the connection. <br/>
![5](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/03944c24-8eaf-4821-9e82-ae690d40f51a)

  ### Reading Log and Sending Email

  Defines a function to read the keystroke log file and send its contents via email.<br/>
![6](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/99fb236a-2dc7-40f4-9a7f-6cd93ad60927)

  Opens the keystroke log file, reads its content, and stores it in 'captured_keys'. <br/>
![7](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/69ab02d4-6b3e-4409-aebe-a23fdd9853f4)

  Generates a timestamp for the current time and sends an email with the log file content. <br/>
![8](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/a58cd7d5-0a6c-407c-ad28-d27f3b511808)

  Clears the log file after sending the email. <br/>
![9](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/ff9d8b15-2bc7-4b3e-a95a-5df7a2f42e9a)

  ### Logging Keystrokes

  Defines a function to be called on each key press. <br/>
![10](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/b50a71b5-6359-404b-aa39-f05027fbb12d)

  Attempts to write the character of the pressed key to the log file. If the key doesn't have a character representation (like special keys), it writes the key's name instead. Then, it ensures the data is immediately written to the file. <br/>
![11](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/bb9a0174-c6db-4773-ba44-c5f6cdd29285)

  ### Main Execution

  Checks if the script is the main program being executed. <br/>
![12](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/65c6e348-a001-46f5-9cf7-8d9c8cbd897b)

  Starts a keyboard listener that calls 'keyPressed' on each key press. <br/>
![13](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/3f9d8f4e-68e4-457c-8df3-b69748a61f4c)

  Schedules the 'read_and_email_log' function to run daily at 22:00. <br/>
![14](https://github.com/KREUW/Keylogger-in-Python/assets/151568256/5dc652c9-d694-4ebf-8e6b-0e81e3e7e14c)

  Prints a message indicating the key logger has started and enters.

 ## Conclusion 



  ### Remember 
  This script combines keylogging, scheduling, and email functionalities in Python, showcasing how to use different modules together for a specific task. Remember, the use of such scripts should always comply with ethical guidelines and legal requirements, emphasizing transparency, consent, and security.

  

  

  
  

  

  

  
  
Launch the utility: <br/>

<br />
<br />
Select the disk:  <br/>

<br />
<br />
Enter the number of passes: <br/>

<br />
<br />
Confirm your selection:  <br/>

<br />
<br />
Wait for process to complete (may take some time):  <br/>

<br />
<br />
Sanitization complete:  <br/>

<br />
<br />
Observe the wiped disk:  <br/>

</p>
