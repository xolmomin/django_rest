from celery import shared_task
from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER


@shared_task
def add(x, y):
    return x + y


@shared_task
def send_to_email(to_email: str):
    send_mail('Tema', 'xabar', EMAIL_HOST_USER, [to_email])
    return {'message': f'Email sent {to_email}'}
