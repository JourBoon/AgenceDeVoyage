import sys
import os
sys.path.append('static/services')
sys.path.append('static/models')
sys.path.append('static/services/exceptions')

#Donner les droits à l'interpréteur d'accéder à la base de donnée.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'database/database.db')

from flask import Flask
from flask import render_template, request, render_template, redirect, url_for, request, flash
from static.services.DBUtils import DBUtils
from static.models.VoyageDAO import VoyageDAO
from static.models.client import Client
from static.models.reservation import Reservation
from static.models.voyage import Voyage
from static.models.destination import Destination

print("Imports successfully instanciated")

app = Flask(__name__ ,template_folder='templates', static_folder='static')
app.secret_key = '123456789'

db_utils = DBUtils(db_path)
db_utils.connect()

#L'absence d'hébergement sur un serveur web nous permet de simplement utiliser une variable
# pour l'authentification. -> isLogged
isLogged = False
session = None

voyageDAO = VoyageDAO()

@app.route('/')
def home():
    """
     Rendu de la page d'accueil index.html. Par défaut l'url est simplement l'adresse du site web sans argument.
    """
    clients_id = db_utils.fetch("SELECT * FROM CLIENT")
    num_client = len(clients_id)
    dests_id = db_utils.fetch("SELECT * FROM DESTINATION")
    num_dests = len(dests_id)
    acts_id = db_utils.fetch("SELECT * FROM ACTIVITE")
    num_acts = len(acts_id)
    destinations = db_utils.fetch("SELECT nom_dest, desc_dest, cost FROM DESTINATION")
    column_names = [column[0] for column in db_utils.local.cur.description]
    destinations_objects = [voyageDAO.toDestination(value, column_names) for value in destinations]
    return render_template("index.html", voyages=destinations_objects, isLogged=isLogged
                        , session=session, clients=num_client, dests=num_dests, acts=num_acts)

@app.route('/trip')
def trip():
    """
     Page de récapitulatif de la réservation d'un voyage.
    """
    dest_name = request.args.get('dest_name')
    # Déclaration de voyage
    if dest_name:
        destinaton = voyageDAO.getDestinationByName(dest_name)
        # Décris de voyage.
        if destinaton:
            return render_template("trip.html", destination=destinaton, isLogged = isLogged, session = session)
        else:
            return render_template("error.html", message="Destination non trouvée")
    else:
        return render_template("error.html", message="Paramètre manquant dans l'URL")

@app.route('/trip', methods=['GET', 'POST'])
def reserver_post():
    """
     Fonction de soumission de formulaire pour ajouter un nouveau voyage à la base de données.
    """
    if not isLogged and not session:
        return redirect(url_for('login'))

    dest_name = request.args.get('dest_name')
    email = session.getMail()
    date_depart = request.form.get("date_depart")
    date_retour = request.form.get("date_retour")

    if dest_name:
        destination = voyageDAO.getDestinationByName(dest_name)

        if destination:
            user = voyageDAO.getClientByEmail(email)
            
            # Si l'utilisateur n'est pas connecté, redirigez vers la page de connexion.
            if not user:
                flash('Impossible de récupérer le compte.')
                return redirect(url_for('login'))

            # Insertion du voyage
            new_voyage_query = """
            INSERT INTO VOYAGE (id_dest, date_depart, date_retour, places, cost)
            VALUES (?, ?, ?, ?, ?)
            """

            voyage_num = db_utils.fetch("SELECT * FROM VOYAGE")
            voyage_id = len(voyage_num)
            new_voyage_data = (
                voyage_id+1,
                date_depart,
                date_retour,
                destination.getPlaces(),
                destination.getCost()
            )
            print(voyage_id)
            print(new_voyage_data)
            db_utils.execute(new_voyage_query, new_voyage_data)
            # Insertion de la réservation
            new_res_query = """
            INSERT INTO RESERVATION (id_client, id_dest, id_voy, cost)
            VALUES (?, ?, ?, ?)
            """
            new_res_data = (
                user.getID(),
                destination.getID(),
                voyage_id+1,
                destination.getCost()
            )
            db_utils.execute(new_res_query, new_res_data)

            print('Réservation effectuée avec succès!')
            return redirect(url_for('dashboard'))
        else:
            return render_template("error.html", message="Destination non trouvée")
    else:
        return render_template("error.html", message="Paramètre manquant dans l'URL")

@app.route('/connexion')
def login():
    """
     Rendu de la page connexion.html
    """
    return render_template("connexion.html", isLogged=isLogged, session=session)

@app.route('/connexion', methods=['GET', 'POST'])
def login_post():
    """
     Fonction de connexion. Cette fonction est appelée par l'interface Web lorsqu'un utilisateur tente de se connecter.
    """
    global isLogged, session
    client = voyageDAO.getClientByEmail(request.form.get('email'))
    print(client.getMdp())
    print(request.form.get("mdp"))
    # Authentification réchée flash Nom d'utilisateur ou mot de passe incorrect
    if client and request.form.get("mdp") == client.getMdp():
        # Authentification réussie
        isLogged = True
        session = client
        return redirect(url_for('dashboard'))
    else:
        # Authentification échouée
        flash('Nom d\'utilisateur ou mot de passe incorrect')
        return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    """
     Rendu de la page tableau de bord. S'il n'y a pas d'utilisateur, un flash s'affiche. Si
    """
    global isLogged, session, voyageDAO
    try:
        email = session.getMail()
        user = voyageDAO.getClientByEmail(email)
        # Si l'utilisateur est connecté redirige vers la page de connexion.
        if user:
            # récupération des voyages du client.
            reservations = voyageDAO.getReservationsWithDetails(user.getID())
            return render_template("dashboard.html", isLogged=isLogged, session=user, reservations=reservations)
        else:
            flash('Impossible de récupérer le compte.')
            return redirect(url_for('login'))
    except Exception as e:
        flash('Erreur lors de l\'accès au tableau de bord.')
        print(str(e))
        return redirect(url_for('login'))

@app.route('/inscription')
def signup():
    """
     Rendu de la page inscription.html
    """
    return render_template('inscription.html')

@app.route('/inscription', methods=['GET', 'POST'])
def signup_post():
    """
     Fonction de formulaire d'inscription. Crée un nouveau client et retourne à la page de connexion. Si l'
    Rediriger vers la page de connexion ou rediriger vers la page d' inscription.
    """
    email = request.form.get('email')
    users = db_utils.fetch("SELECT mail FROM CLIENT WHERE mail = ?", (email,))
    # Si les utilisateurs ne sont pas connectés rediriger vers la page de connexion
    if users:
        flash('Il existe déjà un compte avec cette adresse mail')
        return redirect(url_for('login'))
    new_client_query = """
    INSERT INTO CLIENT (id_client, prenom, nom, age, adresse, mail, mdp, tel_num)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """

    clients_id = db_utils.fetch("SELECT * FROM CLIENT")
    num_client = len(clients_id)

    new_client_data = (
        num_client+1,
        request.form.get('prenom'),
        request.form.get('nom'),
        request.form.get('age'),
        request.form.get('adresse'),
        email,
        request.form.get('password'),
        request.form.get('tel_num')
    )

    db_utils.execute(new_client_query, new_client_data)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    """
     Déconnecte l'utilisateur et le redirige vers la page de connexion.
    """
    global isLogged, session
    isLogged = False
    session = None
    return redirect(url_for('login'))

# Exécutez l'application si __main__ est l'application principale. Exécutez le débug True
if __name__ == '__main__':
    app.run(debug=True)
