class Client:
    def __init__(self, dataset):
        self.dataset = dataset

    def getID(self):
        return self.dataset.get("id_client", None)
    
    def getFirstName(self):
        return self.dataset.get("prenom", None)
    
    def getLastName(self):
        return self.dataset.get("nom", None)
    
    def getAge(self):
        return self.dataset.get("age", None)
    
    def getAddress(self):
        return self.dataset.get("address", None)

    def getMail(self):
        return self.dataset.get("mail", None)
    
    def getMdp(self):
        return self.dataset.get("mdp", None)

    def getTelNum(self):
        return self.dataset.get("tel_num", None)

    def getValue(self, value):
        return self.dataset.get(value, None)
