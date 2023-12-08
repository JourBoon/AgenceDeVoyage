from flask import Flask
from flask import render_template, request, g
from DBUtils import DBUtils

app = Flask(__name__ ,template_folder='templates', static_folder='static')

db_utils = DBUtils("database/database.db")
db_utils.connect()

@app.route('/')
def home():
    yo = "Home Page"
    return render_template("home.html", voyages=yo)

@app.route('/reserver.html')
def reserver():
    yo = "Reserver"
    return render_template("reserver.html", voyages=yo)

@app.route('/inscription.html')
def inscription():
    yo = "Inscription"
    return render_template("inscription.html", voyages=yo)

@app.route('/connexion.html')
def connexion():
    yo = "Connexion"
    return render_template("connexion.html", voyages=yo)

if __name__ == '__main__':
    app.run(debug=True)