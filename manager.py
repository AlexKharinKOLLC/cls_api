from crontab import CronTab
from db_utils import DBUtils


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


def db_info(count=None):
    db = DBUtils()
    db.create()
    db.load_data(count)
