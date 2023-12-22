class Destination:

    def __init__(self, dataset):
        self.dataset = dataset

    def getName(self):
        return self.dataset.get("nom_dest", None)

    def getCost(self):
        return self.dataset.get("cost", None)
    
    def getDesc(self):
        return self.dataset.get("desc_dest", None)
    
    def getPlaces(self):
        return self.dataset.get("places", None)
    
    def getDuration(self):
        return self.dataset.get("duree", None)
    
    def getValue(self, value):
        return self.dataset.get(value, None)

