class Client:
    def __init__(self, dataset, column_names):
        self.data_dict = dict(zip(column_names, dataset))

    def getID(self):
        return self.data_dict.get("id_client", None)
    
    def getFirstName(self):
        return self.data_dict.get("prenom", None)
    
    def getLastName(self):
        return self.data_dict.get("nom", None)
    
    def getAge(self):
        return self.data_dict.get("age", None)
    
    def getAddress(self):
        return self.data_dict.get("address", None)

    def getMail(self):
        return self.data_dict.get("mail", None)
    
    def getMdp(self):
        return self.data_dict.get("mdp", None)

    def getTelNum(self):
        return self.data_dict.get("tel_num", None)

    def getValue(self, value):
        return self.data_dict.get(value, None)
