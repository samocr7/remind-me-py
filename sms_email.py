import email, smtplib, ssl
import os
from providers import PROVIDERS
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465


def send_sms_via_email(
    number: str,
    message: str,
    provider: str
):
    sender_email = os.getenv('MY_EMAIL')
    email_password = os.getenv('MY_EMAIL_APP_PASSWORD')
    receiver_email = _phone_number_address(number, provider)

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, message)

def _phone_number_address(number, provider):
    return number + PROVIDERS[provider]
