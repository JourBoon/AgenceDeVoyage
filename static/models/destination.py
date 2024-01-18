"""
Classe Destination regroupant l'ensemble des paramètres d'une destination.
"""
class Destination:

    def __init__(self, dataset, column_names):
        """ Initialisation en transformant le dataset avec les colonnes en dictionnaire
            utilisable.
        """
        self.data_dict = dict(zip(column_names, dataset))

    def getID(self):
        """Renvoie l'id"""
        return self.data_dict.get("id_dest", None)

    def getName(self):
        """Renvoie le nom"""
        return self.data_dict.get("nom_dest", None)

    def getCost(self):
        """Renvoie le coût"""
        return self.data_dict.get("cost", None)
    
    def getDesc(self):
        """Renvoie la description"""
        return self.data_dict.get("desc_dest", None)
    
    def getPlaces(self):
        """Renvoie les places"""
        return self.data_dict.get("places", None)
    
    def getDuration(self):
        """Renvoie la durée"""
        return self.data_dict.get("duree", None)
    
    def getValue(self, value):
        """Renvoie la valeur associée à 'value'"""
        return self.data_dict.get(value, None)

