import os

from celery import Celery
from celery.schedules import crontab

from cryptocurrency.settings import env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptocurrency.settings')
app = Celery('cryptocurrency')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'add-every-hour-contrab': {
        'task': 'exchange.tasks.exchange_data',
        'schedule': crontab(hour=env('TIME_INTERVAL')),
    },
}

app.autodiscover_tasks()

