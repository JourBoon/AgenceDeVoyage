from voyage import Voyage
from destination import Destination
from DBUtils import DBUtils

class VoyageDAO:

    def __init__(self) -> None:
        self.db_utils = DBUtils("database/database.db")
        pass

    def toVoyage(self, dataset):
        return Voyage(dataset)
    
    def toDestination(self, dataset, column_names):
        return Destination(dataset, column_names)
    
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