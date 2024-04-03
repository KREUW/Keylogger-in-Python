Keylogger & Email


Description
This Python script demonstrates the use of various programming concepts and libraries to achieve a specific functionality: a keystroke logger that captures all keyboard activity, logs it to a file, and then sends the contents of that file to a specified email address once a day. The script uses the pynput library to capture keystrokes, the schedule library to schedule tasks, and the smtplib library to deliver emails. This project is designed to be instructive, demonstrating how to programmatically monitor keyboard input, handle scheduled tasks, and send emails using a Python script.
<br />

What I learned

During the development of this project, I improved my understanding of some essential areas of Python programming and libary use cases to include:

- <b>Keyboard Event Monitoring:</b> Using the pynput package to listen for and record keyboard events in real time.
- <b>Task Scheduling:</b> Using the schedule module to run certain functions at predefined times, allowing for automated tasks within a Python script.
- <b>Email Handling in Python:</b> Use smtplib and MIME standards to construct and send emails programmatically, including plaintext and multipart communications.
- <b>File I/O Operations:</b> Managing file operations for logging data and comprehending the significance of flushing buffers to ensure data integrity.
- <b>Environmental Variables:</b> The significance of using environmental variables to securely manage sensitive information such as email credentials in scripts.


## Languages and Utilities Used 

- <b>Python</b> - <b>Visual Studio Code</b>

Environments Used

- Windows 11

Challenges

Several problems were faced and solved during the development of this keystroke logger to include:

Efficient Data Logging: Ensure that the script logs keystrokes without consuming too many system resources or producing perceptible lag in user input.
Handling special keys: Creating a technique for logging special keystrokes (such as Shift, Ctrl, etc.) in an instructive and readable format.
Secure Email Transmission: Setting up smtplib to transmit emails securely over TLS, as well as securely handling email credentials without hardcoding them into the script.
Scheduling Precision: Setting up the scheduler to perform the email function at the same time every day, while accounting for the computer's sleep state and potential script interrupts.


Script Explanatoin:

<p align="center">
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
