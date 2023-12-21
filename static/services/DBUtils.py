import sqlite3
import threading
from RequestExecutionException import RequestExecutionException

class DBUtils:
    def __init__(self, url):
        self.url = url
        self.local = threading.local()

    def connect(self):
        if not hasattr(self.local, 'con') or self.local.con is None:
            self.local.con = sqlite3.connect(self.url)
            self.local.cur = self.local.con.cursor()

    def execute(self, request):
        try:
            self.connect()
            self.local.cur.execute(request)
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

    def fetch(self, request):
        return self.execute(request)

    def getURL(self):
        return self.url