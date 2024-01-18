from static.models.voyage import Voyage
from static.models.destination import Destination
from static.models.client import Client
from static.services.DBUtils import DBUtils
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'database/database.db')

"""
Classe VoyageDAO: Data Access Object. Ensemble de patrons
    permettant la récupération des objets direct en transformant
    les données récupérées depuis une requête à la base de donnée.
    Les objets créés sont utilisé à travers l'injection des pages html.
"""
class VoyageDAO:

    def __init__(self) -> None:
        self.db_utils = DBUtils("database/database.db")
        pass

    def toVoyage(self, dataset):
        """
        Convertir le dataset en objet Voyage.
        """
        return Voyage(dataset)
    
    def toClient(self, dataset, column_names):
        """
        Convertir le dataset en objet Client.
        """
        return Client(dataset, column_names)

    def toDestination(self, dataset, column_names):
        """
        Convertir le dataset en objet Destination.
        """
        return Destination(dataset, column_names)
    
    def getClientByEmail(self, email):
        """
        Récupère un objet client à partir d'une email si existant dans 
        la base de donnée. Le cas échéant -> None.
        """
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
        """
        Récupère un objet Destination à partir d'une email si existant dans 
        la base de donnée. Le cas échéant -> None.
        """
        query = "SELECT * FROM DESTINATION WHERE nom_dest = ?"
        params = (voyage_name,)

        result = self.db_utils.fetch_one(query, params)
        column_names = [column[0] for column in self.db_utils.local.cur.description]

        if result:
            voyage = self.toDestination(result, column_names)
            return voyage
        else:
            return None