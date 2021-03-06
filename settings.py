import os
from pathlib import Path

API_URL = 'https://api.github.com/'
DB_NAME = os.path.join(str(Path.home()), 'my_sql.db')
DB_RECORDS_COUNT = 10
DB_TABLES = [
    {
        'name': 'links',
        'attr': 'datetime text, src text, desc text'
    }
]

# CELERY QUEUES CONFIG
BACKEND_URL = 'amqp://'
BROKER_URL = 'amqp://guest:guest@localhost//'
QUEUE_NAME = 'cls_api'
ROUTING_KEY = 'cls_api'
