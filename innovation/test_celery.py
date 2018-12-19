from celery import Celery
import settings
import os
# Setting the Default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE','celeryProj.settings')
app=Celery('celeryProj')

# Using a String here means the worker will always find the configuration information
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

from celery import Celery
from celery.schedules import crontab

#The decorator is used for recognizing a periodic task
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    #Sending the email every 10 Seconds
    sender.add_periodic_task(10.0, send_feedback_email_task.s('Ankur','ankur@xyz.com','Hello'), name='add every 10')
  # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        send_feedback_email_task.s('Ankur','ankur@xyz.com','Hello'),)

#The task to be processed by the worker
@app.task
def send_feedback_email_task(name,email,message):
    send_feedback_email(name,email,message)
    logger.info("Sent email")