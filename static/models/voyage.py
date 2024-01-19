"""
Classe Voyage regroupant l'ensemble des paramètres d'un voyage.
"""
class Voyage:
    def __init__(self, dataset, column_names):
        """ Initialisation"""
        self.data_dict = dict(zip(column_names, dataset))

    def getID(self):
        """Renvoie l'id"""
        return self.data_dict.get("id_voy", None)

    def getIDDest(self):
        """Renvoie l'id de la destination"""
        return self.data_dict.get("id_dest", None)
    
    def getDepartDate(self):
        """Renvoie la date de départ"""
        return self.data_dict.get("date_depart", None)
    
    def getBackDate(self):
        """Renvoie la date de retour"""
        return self.data_dict.get("date_retour", None)
    
    def getPlaces(self):
        """Renvoie les places"""
        return self.data_dict.get("places", None)
    
    def getCost(self):
        """Renvoie le cout"""
        return self.data_dict.get("cost", None)

    def getValue(self, value):
        """Renvoie la valeur associée à 'value'"""
        return self.dataset.get(value, None)
    
    def setDestination(self, destination):
        """ Définit l'objet destination associé à ce voyage """
        self.destination = destination
