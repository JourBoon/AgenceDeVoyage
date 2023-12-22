class Voyage:
    def __init__(self, dataset):
        self.dataset = dataset

    def getID(self):
        return self.dataset.get("id_voy", None)

    def getIDDest(self):
        return self.dataset.get("id_dest", None)
    
    def getDepartDate(self):
        return self.dataset.get("date_depart", None)
    
    def getBackDate(self):
        return self.dataset.get("date_retour", None)
    
    def getPlaces(self):
        return self.dataset.get("places", None)
    
    def getCost(self):
        return self.dataset.get("cost", None)

    def getValue(self, value):
        return self.dataset.get(value, None)