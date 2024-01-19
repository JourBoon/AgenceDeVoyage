import sys
import os
sys.path.append('static/services')
sys.path.append('static/models')
sys.path.append('static/services/exceptions')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'database/database.db')

from flask import Flask
from flask import render_template, request, g, Blueprint, render_template, redirect, url_for, request, flash
from static.services.DBUtils import DBUtils
from static.models.VoyageDAO import VoyageDAO
from static.models.client import Client

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
    destinations = db_utils.fetch("SELECT nom_dest, desc_dest, cost FROM DESTINATION")
    column_names = [column[0] for column in db_utils.local.cur.description]
    destinations_objects = [voyageDAO.toDestination(value, column_names) for value in destinations]
    return render_template("index.html", voyages=destinations_objects, isLogged=isLogged
                        , session=session)

@app.route('/reserver')
def reserver():
    return render_template("reserver.html")

@app.route('/explore')
def explorer():
    destinations = db_utils.fetch("SELECT nom_dest, desc_dest, cost FROM DESTINATION")
    column_names = [column[0] for column in db_utils.local.cur.description]
    destinations_objects = [voyageDAO.toDestination(value, column_names) for value in destinations]
    return render_template("explorer.html", voyages=destinations_objects)

@app.route('/trip')
def trip():
    dest_name = request.args.get('dest_name')
    if dest_name:
        destinaton = voyageDAO.getDestinationByName(dest_name)
        if destinaton:
            return render_template("trip.html", destination=destinaton)
        else:
            return render_template("error.html", message="Destination non trouvé")
    else:
        return render_template("error.html", message="Paramètre manquant dans l'URL")

@app.route('/connexion')
def login():
    return render_template("connexion.html", isLogged=isLogged)

@app.route('/connexion', methods=['GET', 'POST'])
def login_post():
    global isLogged, session
    client = voyageDAO.getClientByEmail(request.form.get('email'))
    print(client.getMdp())
    print(request.form.get("mdp"))
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
    return render_template("dashboard.html", isLogged=isLogged, session=session)

@app.route('/inscription')
def signup():
    return render_template('inscription.html')

@app.route('/inscription', methods=['GET', 'POST'])
def signup_post():
    email = request.form.get('email')
    users = db_utils.fetch("SELECT mail FROM CLIENT WHERE mail = ?", (email,))
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

@app.route('/trip', methods=['GET', 'POST'])
def reserver_post():
    return redirect(url_for('dashboard'))

@app.route('/login')
def logout():
    global isLogged, session
    isLogged = False
    session = None
    return redirect(url_for('/login'))

if __name__ == '__main__':
    app.run(debug=True)
