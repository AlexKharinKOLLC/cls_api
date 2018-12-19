from utils import read_from_fifo
from db_utils import DBUtils
from celery import shared_task


@shared_task(name="processor.process", time_limit=30)
def process():
    db = DBUtils()
    db.create()
    data = read_from_fifo()
    if len(data) > 0:
        for msg in data:
            for key, val in msg.items():
                db_record = dict(zip(["desc", "src"], [key, val]))
                db.save_data(db_record)
        print("Data received, msg_cnt: %d" % len(data))
    db.close()


if __name__ == "__main__":
    process.delay()
