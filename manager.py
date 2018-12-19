import os
import settings
from celery import Celery
from fetcher import fetch
from processor import process
from db_utils import DBUtils
from celery.schedules import crontab

app = Celery('manager', backend=settings.BACKEND_URL, broker=settings.BROKER_URL)


app.task(fetch)
app.task(process)

app.conf.beat_schedule = {
    'fetch': {
        'task': 'fetcher.fetch',
        'schedule': crontab()
    },
    'process': {
        'task': 'processor.process',
        'schedule': crontab(minute="*/5")
    }
}


def db_info():
    db = DBUtils()
    db.create()
    db.load_data(settings.DB_RECORDS_COUNT)


def db_drop():
    if os.path.exists(settings.DB_NAME):
        os.remove(settings.DB_NAME)
        print("DB dropped")
    else:
        print("DB doesn't exist")
