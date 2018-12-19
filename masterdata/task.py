from celery import shared_task
from celery.utils.log import get_task_logger
# from celeryapp.emails import send_feedback_email
from django.conf import settings
logger=get_task_logger(__name__)


from django.core.mail import send_mail

def send_feedback_email(name,email,message):
    send_mail(name,message+" \n "+settings.DEFAULT_FROM_EMAIL,email,['kadhirmani@gmail.com'],fail_silently=False)




# This is the decorator which a celery worker uses
@shared_task(name="send_feedback_email_task")
def send_feedback_email_task(name,email,message):
    logger.info("Sent email")
    return send_feedback_email(name,email,message)