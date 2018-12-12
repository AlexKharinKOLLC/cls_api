import os
from pathlib import Path

FIFO_NAME = 'testpipe.data'
API_URL = 'https://api.github.com/'
DB_NAME = os.path.join(str(Path.home()), 'my_sql.db')
DB_TABLES = [
    {
        'name': 'links',
        'attr': 'datetime text, src text, desc text'
    }
]