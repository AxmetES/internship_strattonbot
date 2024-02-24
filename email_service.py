import logging
from smtp_service import send_email_smtp


def send_email(email):
    send_email_smtp(email['to'], email['subject'], email['message'], email['file_path'])
