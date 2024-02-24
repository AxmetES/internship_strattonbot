import email_service
import redis
from xlsx_file_generator import generate_xlsx_file

def send_email_endpoint(email):
    email_service.send_email(email)


if __name__ == "__main__":
    file_path = generate_xlsx_file()
    email = {
        'to': 'fraktsia@gmail.com',
        'subject': 'job_test',
        'message': 'Hello world',
        'file_path': file_path
    }
    send_email_endpoint(email)