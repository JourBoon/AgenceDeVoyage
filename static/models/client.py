"""
Classe Client regroupant l'ensemble des paramètres d'une session client.
"""
class Client:
    def __init__(self, dataset, column_names):
        """ Initialisation en transformant le dataset avec les colonnes en dictionnaire
            utilisable.
        """
        self.data_dict = dict(zip(column_names, dataset))

    def getID(self):
        """Renvoie l'id"""
        return self.data_dict.get("id_client", None)
    
    def getFirstName(self):
        """Renvoie le prénom"""
        return self.data_dict.get("prenom", None)
    
    def getLastName(self):
        """Renvoie le nom"""
        return self.data_dict.get("nom", None)
    
    def getAge(self):
        """Renvoie l'age"""
        return self.data_dict.get("age", None)
    
    def getAddress(self):
        """Renvoie l'adresse"""
        return self.data_dict.get("address", None)

    def getMail(self):
        """Renvoie l'email"""
        return self.data_dict.get("mail", None)
    
    def getMdp(self):
        """Renvoie le mot de passe (Non sécure proof)
        -> absence de hashage pour les mots de passe."""
        return self.data_dict.get("mdp", None)

    def getTelNum(self):
        """Renvoie le numéro de téléphone"""
        return self.data_dict.get("tel_num", None)

    def getValue(self, value):
        """Renvoie la valeur associée à 'value'"""
        return self.data_dict.get(value, None)
