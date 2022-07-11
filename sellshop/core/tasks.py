import imp
from celery import shared_task
import time

from core.publisher import Publish
from .models import  Subscriber
from blog.models import Blog
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

@shared_task
def process_func():
    time.sleep(10)
    return 'Process done'

@shared_task
def send_mail_to_subscribers():
    email_list = Subscriber.objects.filter(is_active = True).values_list('email',flat=True)
    blogs = Blog.objects.all()
    mail_text = render_to_string('email-subscriber.html',{
        'blogs': blogs,
    })
    Publish(data={"body":mail_text,"subject":"Blogs for this week","recipients": email_list,"subtype":"html"},event_type="send_mail")
    # msg = EmailMultiAlternatives(subject='Blogs for this week', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    # msg.attach_alternative(mail_text, "text/html")
    # msg.send()