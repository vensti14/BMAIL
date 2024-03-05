import speech_recognition as sr
import smtplib
import imaplib
import email
import pyfiglet
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import decode_header
import pyttsx3

config = {
    'email': 'your_email@gmail.com',
    'password': 'your_password',
    'imap_server': 'imap.gmail.com',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587
}

r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    str = "Speak Now:"
    speak(str)
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=20, phrase_time_limit=20)
        mytext = r.recognize_google(audio)
        mytext = mytext.lower()
        print(mytext) 
    try:
        text = r.recognize_google(audio);
        return text
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that. Please try again.")
        return listen()

def login():
    mail = imaplib.IMAP4_SSL(config['imap_server'])
    mail.login(config['email'], config['password'])
    return mail

def extract_email_body(email_message):
    body = ""
    if email_message.is_multipart():
        for part in email_message.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))
            if ctype == 'text/plain' and 'attachment' not in cdispo:
                body += part.get_payload(decode=True).decode("utf-8")
                break
    else:
        body = email_message.get_payload(decode=True).decode("utf-8")
    return body

def get_inbox():
    mail = login()
    mail.select('inbox')
    _, data = mail.search(None, 'ALL')
    messages = []
    for num in data[0].split():
        _, msg = mail.fetch(num, '(RFC822)')
        messages.append(msg[0][1])
    for message in messages:
        email_message = email.message_from_bytes(message)
        sender = decode_header(email_message["From"])[0][0]
        subject = decode_header(email_message["Subject"])[0][0]
        speak(f"From {sender} Subject {subject}")
        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    speak(part.get_payload(decode=True).decode())
        else:
            speak(email_message.get_payload(decode=True).decode())

def send_email(to, subject, body):
    if not to.endswith("@gmail.com"):
       speak("Invalid email address. Please provide an email address that ends with @gmail.com.")
       return
    
    msg = MIMEMultipart()
    msg['From'] = config['email']
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
    server.starttls()
    server.login(config['email'], config['password'])
    text = msg.as_string()
    server.sendmail(config['email'], to, text)
    server.quit()

def compose():
    speak("Who do you want to send the email to?")
    to = listen().lower().replace(" ", "")
    speak("What is the subject of the email?")
    subject = listen()
    speak("What do you want to say in the email?")
    body = listen()
    send_email(to, subject, body)
    speak("Email sent successfully.")

while True:
    banner = pyfiglet.figlet_format("WELCOME TO BMAIL")
    print(banner)

    speak("Welcome to Bmail. What do you want to do?")
    speak("1. Speak 'compose' to compose and send an email")
    speak("2. Speak 'inbox' to read your inbox")
    speak("3. Speak 'exit' to exit")

    user_input = listen()

    if user_input == "compose":
        speak("You have chosen to compose and send an email")
        compose()

    elif user_input == "inbox":
        speak("You have chosen to read your inbox")
        inbox_messages = get_inbox()
        if not inbox_messages:
            speak("Your inbox is empty")
        else:
            for msg in inbox_messages:
                # extract relevant information from email message
                sender = decode_header(msg["From"])[0][0]
                subject = decode_header(msg["Subject"])[0][0]

                # read out email message
                speak(f"You have a new email from {sender}. The subject is {subject}.")
                speak("Do you want me to read the message?")
                read_message = listen()
                if read_message == "yes":
                    message_body = extract_email_body(msg)
                    speak("The message says:")
                    speak(message_body)

    elif user_input == "exit":
        speak("You have chosen to exit. Goodbye!")
        break

    else:
        speak("Invalid choice. Please try again.")
