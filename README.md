# Bmail - Speech Enabled Email Client

Bmail is a Python script that serves as a basic email client with speech recognition capabilities. It allows users to compose and send emails, as well as read emails from their inbox using voice commands.

## Features

- Compose and send emails: Users can dictate the recipient, subject, and body of the email using speech recognition.
- Read inbox: Bmail can read out the sender and subject of new emails in the inbox, and optionally read the email message upon user request.
- Speech feedback: Bmail provides spoken feedback throughout the email composition and reading process using text-to-speech synthesis.

## Requirements

To run Bmail, you'll need the following dependencies installed:

- Python 3.x
- `speech_recognition` library
- `pyttsx3` library
- `smtplib` library
- `imaplib` library
- `pyfiglet` library (for ASCII art banner display)

You can install the dependencies using pip:

pip install speech_recognition pyttsx3 pyfiglet


## Usage

1. Clone this repository to your local machine:


2. Navigate to the project directory:


3. Open the `config` dictionary in the `bmail.py` file and fill in your email credentials and server details.

4. Enable access for Less Secure Apps:
   - Go to your Google Account settings by visiting [https://myaccount.google.com/](https://myaccount.google.com/).
   - Click on "Security" in the left sidebar.
   - Scroll down to the "Less secure app access" section.
   - Turn on the toggle switch for "Allow less secure apps". This allows applications like Bmail to access your Gmail account with your username and password.

5. (Recommended) Generate an App Password:
   - If you encounter issues with less secure apps access or prefer enhanced security, you can generate an app password instead.
   - In the same "Security" section of your Google Account settings, scroll down to the "Signing in to Google" section.
   - Click on "App passwords".
   - If prompted, enter your Google account password.
   - Click on "Select app" and choose "Other (Custom name)".
   - Enter a name for the app (e.g., "Bmail") and click "Generate".
   - Google will generate a 16-digit app password.
   - Use this generated password in your script instead of your regular Google account password.

6. Run the script: python3 bmail.py
7. Follow the spoken instructions to compose and send emails or read your inbox.

## Acknowledgements

- This project was inspired by the need for a hands-free email client for users with limited mobility or vision impairment.
- Thanks to the developers of the `speech_recognition`, `pyttsx3`, and other libraries used in this project for their contributions.


