import sys
sys.path.append('static/services')
sys.path.append('static/models')
sys.path.append('static/services/exceptions')

from flask import Flask
from flask import render_template, request, g
from DBUtils import DBUtils
from VoyageDAO import VoyageDAO

print("Imports successfully instanciated")

app = Flask(__name__ ,template_folder='templates', static_folder='static')

db_utils = DBUtils("database/database.db")
db_utils.connect()

voyageDAO = VoyageDAO()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/reserver.html')
def reserver():
    return render_template("reserver.html")

@app.route('/explorer.html')
def explorer():
    destinations = db_utils.fetch("SELECT nom_dest, desc_dest, cost FROM DESTINATION")
    column_names = [column[0] for column in db_utils.local.cur.description]
    destinations_objects = [voyageDAO.toDestination(value, column_names) for value in destinations]
    return render_template("explorer.html", voyages=destinations_objects)

@app.route('/inscription.html')
def inscription():
    return render_template("inscription.html")

@app.route('/connexion.html')
def connexion():
    return render_template("connexion.html")

if __name__ == '__main__':
    app.run(debug=True)