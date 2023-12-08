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
            res = self.cur.execute(request)
            if res == None:
                raise RequestExecutionException
            else:
                return res
        except RequestExecutionException:
            print("Error while executing request:", request)

    def multiExecute(self, request, dataSet):
        try:
            res = self.cur.executemany(request, dataSet)
            if res == None:
                raise RequestExecutionException
            else:
                return res
        except RequestExecutionException:
            print("Error while executing multi request:", request)

    def insert(self, request, data):
        self.multiExecute(request, data)

    def multiInsert(self, request, dataSet):
        self.multiExecute(request, dataSet)

    def fetch(self, request):
        return self.execute(request)

    def getURL(self):
        return self.url