import sqlite3
import threading
import os
from static.services.exceptions.RequestExecutionException import RequestExecutionException
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'database/database.db')

"""
Classe DBUtils : Une classe utilitaire instanciée dans VoyageDAO et app afin
    de faciliter les requêtes vers la base de donnée.
    Prévient la répétition de code.
"""
class DBUtils:
    def __init__(self, url):
        """Initialisation"""
        #Url du chemin de la base de donnée
        self.url = url
        #Gestion des threads -> Eviter les erreurs de Runtime a l'éxécution.
        self.local = threading.local()

    def connect(self):
        """Connexion à la base de donnée"""
        if not hasattr(self.local, 'con') or self.local.con is None:
            self.local.con = sqlite3.connect(self.url)
            self.local.cur = self.local.con.cursor()

    def execute(self, request, args=None, fetch_one=False):
        """
        Entrée: Une requête SQL 'request', 
            des arguments optionnels 'args', 
            un indicateur 'fetch_one' pour récupérer un seul résultat.
        Sortie: Le résultat de la requête (fetchall ou fetchone) 
            ou None si la requête modifie la base de .
        Rôle: Exécuter une requête SQL sur la base de données.
        Précondition: La connexion à la base de données doit être établie.
        Postcondition: La requête est exécutée, les changements sont validés 
            dans la base de données, et le résultat est renvoyé.
        """
        try:
            # Établir la connexion à la base de données
            self.connect()

            # Exécuter la requête avec ou sans arguments
            if args:
                self.local.cur.execute(request, args)
                self.local.con.commit()
            else:
                self.local.cur.execute(request)
                self.local.con.commit()

            # Récupérer les résultats de la requête
            if fetch_one:
                return self.local.cur.fetchone()
            else:
                return self.local.cur.fetchall()
        except sqlite3.Error as e:
            # Gérer les erreurs lors de l'exécution de la requête
            print("Error while executing request:", request)
            print("SQLite error:", e)
            raise RequestExecutionException(str(e))

    def multiExecute(self, request, dataSet):
        """
        Entrée: Une requête SQL 'request' et un ensemble de données 'dataSet'.
        Sortie: Aucune (modifie la base de données).
        Rôle: Exécuter plusieurs requêtes SQL avec des ensembles de données.
        Précondition: La connexion à la base de données doit être établie.
        Postcondition: Les requêtes sont exécutées avec les ensembles de données fournis.
        """
        try:
            # Établir la connexion à la base de données
            self.connect()

            # Exécuter plusieurs requêtes avec l'ensemble de données
            self.local.cur.executemany(request, dataSet)
            self.local.con.commit()
        except sqlite3.Error as e:
            # Gérer les erreurs lors de l'exécution des requêtes multiples
            print("Error while executing multi request:", request)
            print("SQLite error:", e)
            raise RequestExecutionException(str(e))

    def insert(self, request, data):
        # Simplification de l'insertion pour un seul ensemble de données
        self.multiExecute(request, [data])

    def multiInsert(self, request, dataSet):
        # Utiliser la méthode multiExecute pour l'insertion multiple
        self.multiExecute(request, dataSet)

    def fetch(self, request, args=None):
        # Utiliser la méthode execute pour récupérer tous les résultats
        return self.execute(request, args=args)

    def fetch_one(self, request, args=None):
        # Utiliser la méthode execute avec l'indicateur fetch_one pour récupérer un seul résultat
        return self.execute(request, args=args, fetch_one=True)

    def getURL(self):
        # Renvoyer l'URL de la base de données
        return self.url
