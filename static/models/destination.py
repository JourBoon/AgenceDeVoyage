class Destination:

    def __init__(self, dataset, column_names):
        self.data_dict = dict(zip(column_names, dataset))

    def getID(self):
        return self.data_dict.get("id_dest", None)

    def getName(self):
        return self.data_dict.get("nom_dest", None)

    def getCost(self):
        return self.data_dict.get("cost", None)
    
    def getDesc(self):
        return self.data_dict.get("desc_dest", None)
    
    def getPlaces(self):
        return self.data_dict.get("places", None)
    
    def getDuration(self):
        return self.data_dict.get("duree", None)
    
    def getValue(self, value):
        return self.data_dict.get(value, None)

