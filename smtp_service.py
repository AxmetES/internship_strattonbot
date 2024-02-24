import smtplib
from config import settings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header

def send_email_smtp(to, subject, message, file_path=None):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = settings.STMP_USERNAME
    smtp_password = settings.STMP_PASSWORD

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = to
        msg['Subject'] = Header(subject, 'utf-8')

        msg.attach(MIMEText(message, 'plain', 'utf-8'))
        if file_path:
            attachment = MIMEBase('application', 'octet-stream')
            with open(file_path, 'rb') as file:
                attachment.set_payload(file.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename="{file_path}"')
            msg.attach(attachment)

        # Send the email
        server.sendmail(smtp_username, to, msg.as_string())


        # mime = MIMEText(message, 'plain', 'utf-8')
        # mime = MIMEText(message, 'plain', 'utf-8')
        # mime['Subject'] = Header(subject, 'utf-8')
        # server.sendmail(smtp_username, to, mime.as_string())