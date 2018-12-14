import os
import settings
from celery import Celery
from fetcher import fetch
from processor import process
from db_utils import DBUtils
from crontab import CronTab

app = Celery('manager', backend='rpc://', broker='amqp://localhost')

app.task(fetch)
app.task(process)


def add_task(user=None, command=None, timeout=0):
    if not user or not command:
        print("Wrong number of params!\n")
        return

    cron = CronTab(user=user)
    job = cron.new(command="python3 %s" % command)
    job.minute.every(timeout)
    cron.write()
    print("User - %s\nCommand - %s...\nTask added" % (user, command))


def remove_tasks(user=None):
    if not user:
        print("User not given!\n")
        return
    cron = CronTab(user=user)
    cron.remove_all()
    cron.write()
    
    print("Tasks for user %s removed\n" % user)


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
