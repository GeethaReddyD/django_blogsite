from celery import shared_task 
from .models import Subscriber 
from django.core.mail import send_mail
from blogsite import settings

@shared_task(bind = True) 

def test(self):
    subscribers = Subscriber.objects.all()
    for user in subscribers:
        email_subject = "Celery Testing"
        message = "Thank You for subscribing.New post has been updated.please check it"
        to_email = user.email 
        send_mail(
            subject = email_subject,
            message = message,
            from_email = 'flasksample123@gmail.com',
            recipient_list = [to_email],
            fail_silently = True,
        ) 
    return "Done"