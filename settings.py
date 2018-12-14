import os
from pathlib import Path
from celery import Celery

FIFO_NAME = 'testpipe.data'
API_URL = 'https://api.github.com/'
DB_NAME = os.path.join(str(Path.home()), 'my_sql.db')
DB_RECORDS_COUNT = 10
DB_TABLES = [
    {
        'name': 'links',
        'attr': 'datetime text, src text, desc text'
    }
]

app = Celery('manager', backend='amqp://', broker='amqp://localhost')
