import os

from celery import shared_task
from django.core.mail import send_mail
from dotenv import load_dotenv

load_dotenv()


@shared_task
def send_activation_email(user_email, abs_url,user_username):
    activation_link = f"{abs_url}"
    subject = 'Activation Account'
    message = f"Hi {user_username} Use link below to verify email\n{activation_link}"
    from_email = os.getenv('EMAIL_HOST_USER')
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list,fail_silently=False)
