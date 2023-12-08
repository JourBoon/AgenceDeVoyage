import sqlite3
import RequestExecutionException

class DBUtils:

    def __init__(self, url):
        self.url = url
        self.con = None
        self.cur = None

    def connect(self):
        self.con = sqlite3.connect(self.url)
        self.cur = self.con.cursor()

    def execute(self, request):
        try:
            self.cur.execute(request)
            return self.cur.fetchall()
        except sqlite3.Error as e:
            print("Error while executing request:", request)
            print("SQLite error:", e)
            raise RequestExecutionException(str(e))

    def multiExecute(self, request, dataSet):
        try:
            self.cur.executemany(request, dataSet)
            self.con.commit()
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