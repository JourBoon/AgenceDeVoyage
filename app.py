import sys
sys.path.append('static/services')
sys.path.append('static/models')
sys.path.append('static/services/exceptions')

from flask import Flask
from flask import render_template, request, g, Blueprint, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from static.services.DBUtils import DBUtils
from static.models.VoyageDAO import VoyageDAO
from static.models.client import Client

print("Imports successfully instanciated")

app = Flask(__name__ ,template_folder='templates', static_folder='static')

login_manager = LoginManager(app)
login_manager.login_view = 'login'

db_utils = DBUtils("database/database.db")
db_utils.connect()

auth = Blueprint('auth', __name__)
isLogged = False

voyageDAO = VoyageDAO()

@app.route('/')
def home():
    destinations = db_utils.fetch("SELECT nom_dest, desc_dest, cost FROM DESTINATION")
    column_names = [column[0] for column in db_utils.local.cur.description]
    destinations_objects = [voyageDAO.toDestination(value, column_names) for value in destinations]
    return render_template("index.html", voyages=destinations_objects)

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

@app.route('/connexion', methods=['POST'])
def login():
    client = voyageDAO.getClientByEmail(request.form.get('email'))
    if client and request.form.get("email") == client.getMail() and request.form.get("mdp") == client.getMdp():
        isLogged = True
        return redirect(url_for('dashboard'))
    else:
        flash('Nom d\'utilisateur ou mot de passe incorrect')
        return redirect(url_for('login'))

    return render_template('connexion.html')
@app.route('/inscription')
def signup():
    return render_template('inscription.html')

@app.route('/inscription', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    print("SELECT mail FROM CLIENT WHERE mail = ?", (email,))
    users = db_utils.fetch("SELECT mail FROM CLIENT WHERE mail = ?", (email,))
    #user = Client.query.filter_by(email=email).first()
    if users:
        flash('Il existe déjà un compte avec cette adresse mail')
        return redirect(url_for('login'))
    new_client_query = """
    INSERT INTO CLIENT (prenom, nom, age, adresse, mail, tel_num)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    new_client_data = (
        request.form.get('prenom'),
        request.form.get('nom'),
        request.form.get('age'),
        request.form.get('adresse'),
        email,
        request.form.get('tel_num')
    )

    db_utils.execute(new_client_query, new_client_data)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    return 'Logout'

if __name__ == '__main__':
    app.run(debug=True)