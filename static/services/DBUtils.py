import sqlite3
import threading
from static.services.exceptions.RequestExecutionException import RequestExecutionException

class DBUtils:
    def __init__(self, url):
        self.url = url
        self.local = threading.local()

    def connect(self):
        if not hasattr(self.local, 'con') or self.local.con is None:
            self.local.con = sqlite3.connect(self.url)
            self.local.cur = self.local.con.cursor()

    def execute(self, request, args=None, fetch_one=False):
        try:
            self.connect()
            if args:
                self.local.cur.execute(request, args)
            else:
                self.local.cur.execute(request)

            if fetch_one:
                return self.local.cur.fetchone()
            else:
                return self.local.cur.fetchall()
        except sqlite3.Error as e:
            print("Error while executing request:", request)
            print("SQLite error:", e)
            raise RequestExecutionException(str(e))

    def multiExecute(self, request, dataSet):
        try:
            self.connect()
            self.local.cur.executemany(request, dataSet)
            self.local.con.commit()
        except sqlite3.Error as e:
            print("Error while executing multi request:", request)
            print("SQLite error:", e)
            raise RequestExecutionException(str(e))

    def insert(self, request, data):
        self.multiExecute(request, [data])

    def multiInsert(self, request, dataSet):
        self.multiExecute(request, dataSet)

    def fetch(self, request, args=None):
        return self.execute(request, args=args)
    
    def fetch_one(self, request, args=None):
        return self.execute(request, args=args, fetch_one=True)

    def getURL(self):
        return self.url