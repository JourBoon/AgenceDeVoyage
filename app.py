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

@app.route('/inscription')
def inscription():
    return render_template("inscription.html")

@app.route('/connexion')
def connexion():
    return render_template("connexion.html")

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

def data_tri():
    
if __name__ == '__main__':
    app.run(debug=True)