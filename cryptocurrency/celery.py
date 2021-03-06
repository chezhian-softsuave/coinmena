import os

from celery import Celery
from celery.schedules import crontab

from cryptocurrency.settings import env

# Celery Configuration
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptocurrency.settings')

app = Celery('cryptocurrency')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Every Hour Data Fetching
app.conf.beat_schedule = {
    'add-every-hour-crontab': {
        'task': 'exchange.tasks.exchange_data',
        'schedule': 60,
    },
}

app.autodiscover_tasks()
