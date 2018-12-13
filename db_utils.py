import sqlite3
import settings
from datetime import datetime


class DBUtils:
    
    def __init__(self):
        self.db = sqlite3.connect(settings.DB_NAME)
        self.cursor = self.db.cursor()
    
    def create(self):
        try:
            for table in settings.DB_TABLES:
                self.cursor.execute("CREATE TABLE %s (%s)" % (table['name'], table['attr']))
            self.db.commit()
        except sqlite3.OperationalError:
            print('Table already exists')
        finally:
            print('DB created')
    
    def save_data(self, data=None):
        if not data:
            return
        if not ('src' in data and 'desc' in data):
            print("Wrong data type")
            return
        self.cursor.execute("INSERT INTO %s VALUES ('%s', '%s', '%s')" % (settings.DB_TABLES[0]['name'], str(datetime.now()), data['src'], data['desc']))
        self.db.commit()
    
    def load_data(self, count=10):
        self.cursor.execute("SELECT * FROM %s" % settings.DB_TABLES[0]['name'])
        for record in self.cursor.fetchall()[-count:]:
            print(record)
    
    def close(self):
        self.db.close()
