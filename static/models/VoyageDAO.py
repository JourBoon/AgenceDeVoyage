from static.models.voyage import Voyage
from static.models.destination import Destination
from static.models.client import Client
from static.services.DBUtils import DBUtils
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'database/database.db')

class VoyageDAO:

    def __init__(self) -> None:
        self.db_utils = DBUtils("database/database.db")
        pass

    def toVoyage(self, dataset):
        return Voyage(dataset)
    
    def toClient(self, dataset, column_names):
        return Client(dataset, column_names)

    def toDestination(self, dataset, column_names):
        return Destination(dataset, column_names)
    
    def getClientByEmail(self, email):
        query = "SELECT * FROM CLIENT WHERE mail = ?"
        params = (email,)

        result = self.db_utils.fetch_one(query, params)
        column_names = [column[0] for column in self.db_utils.local.cur.description]

        if result:
            voyage = self.toClient(result, column_names)
            return voyage
        else:
            return None

    def getDestinationByName(self, voyage_name):
        query = "SELECT * FROM DESTINATION WHERE nom_dest = ?"
        params = (voyage_name,)

        result = self.db_utils.fetch_one(query, params)
        column_names = [column[0] for column in self.db_utils.local.cur.description]

        if result:
            voyage = self.toDestination(result, column_names)
            return voyage
        else:
            return None