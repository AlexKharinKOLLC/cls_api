from utils import read_from_fifo
from db_utils import DBUtils
import simplejson
from celery import shared_task


def parse_data(data):
    result = []
    for block in data:
        result.append(simplejson.loads(block))
    return result


@shared_task(name="processor.process")
def process():
    db = DBUtils()
    db.create()
    data = parse_data(read_from_fifo())
    if len(data) > 0:
        for msg in data:
            for key, val in msg.items():
                db_record = dict(zip(["desc", "src"], [key, val]))
                db.save_data(db_record)
        print("Data received, msg_cnt: %d" % len(data))
    db.close()


if __name__ == "__main__":
    process.delay()
