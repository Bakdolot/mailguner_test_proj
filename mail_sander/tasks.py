from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User

from core import celery_app
from mail_sander.models import Message


@celery_app.task
def send_email_task(message_id, recipient_id, mail_template):
    message = Message.objects.get(id=message_id)
    recipient = User.objects.get(id=recipient_id)
    html_message = render_to_string(mail_template, {"message": message, "recipient": recipient})
    plain_message = strip_tags(html_message)
    send_mail(
        message.title,
        plain_message,
        settings.EMAIL_HOST_USER,
        [recipient.email],
        fail_silently=False,
        html_message=html_message,
    )
