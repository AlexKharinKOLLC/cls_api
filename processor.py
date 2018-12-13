from utils import read_from_fifo
from db_utils import DBUtils
import simplejson


def parse_data(data):
    result = []
    for block in data:
        result.append(simplejson.loads(block))
    return result


def process():
    db = DBUtils()
    db.create()
    data = parse_data(read_from_fifo())
    if len(data) > 0:
        for msg in data:
            for key, val in msg.items():
                db_record = dict(zip(["desc", "src"], [key, val]))
                db.save_data(db_record)
    db.close()


if __name__ == "__main__":
    process()
