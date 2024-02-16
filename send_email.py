import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(body):
    host = "smtp.gmail.com"
    port = 465

    username = "app1generator@gmail.com"
    authentication = os.getenv("AUTHENTICATION")

    receiver = "majewski.jacek002@gmail.com"
    my_context = ssl.create_default_context()

    message = MIMEMultipart()
    message["From"] = username
    message["To"] = receiver
    message["Subject"] = "Today's news"
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, authentication)
        server.sendmail(username, receiver, message.as_string())