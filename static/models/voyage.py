"""
Classe Voyage regroupant l'ensemble des paramètres d'un voyage.
"""
class Voyage:
    def __init__(self, dataset):
        """ Initialisation"""
        self.dataset = dataset

    def getID(self):
        """Renvoie l'id"""
        return self.dataset.get("id_voy", None)

    def getIDDest(self):
        """Renvoie l'id de la destination"""
        return self.dataset.get("id_dest", None)
    
    def getDepartDate(self):
        """Renvoie la date de départ"""
        return self.dataset.get("date_depart", None)
    
    def getBackDate(self):
        """Renvoie la date de retour"""
        return self.dataset.get("date_retour", None)
    
    def getPlaces(self):
        """Renvoie les places"""
        return self.dataset.get("places", None)
    
    def getCost(self):
        """Renvoie le cout"""
        return self.dataset.get("cost", None)

    def getValue(self, value):
        """Renvoie la valeur associée à 'value'"""
        return self.dataset.get(value, None)