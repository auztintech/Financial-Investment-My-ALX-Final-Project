from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab

app = Celery('website')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'run-increment-user-balances': {
        'task': 'user.tasks.increase_amount',  
        'schedule': crontab(minute='*/1'),  
    },
}