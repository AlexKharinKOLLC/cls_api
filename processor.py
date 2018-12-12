from utils import read_from_fifo
from db_utils import DBUtils


def parse_data(data):
    result = []
    for lines in data:
        result.append(lines.replace("{\"", "\"").replace("\"}", "\"").replace("\",\"", "\"\n\"").
                      replace("\":\"", "\": \"").replace("\"", "").split("\n"))
    return result


def process():
    db = DBUtils()
    db.create()
    data = parse_data(read_from_fifo())
    if len(data) > 0:
        for msg in data:
            for line in msg:
                db_record = dict(zip(["desc", "src"], line.split(": ")))
                db.save_data(db_record)
    db.close()


if __name__ == "__main__":
    process()
