import sys
sys.path.append('static/services')
sys.path.append('static/services/exceptions')

from flask import Flask
from flask import render_template, request, g
from DBUtils import DBUtils

app = Flask(__name__ ,template_folder='templates', static_folder='static')

db_utils = DBUtils("database/database.db")
db_utils.connect()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/reserver.html')
def reserver():
    return render_template("reserver.html")

@app.route('/inscription.html')
def inscription():
    return render_template("inscription.html")

@app.route('/connexion.html')
def connexion():
    return render_template("connexion.html")

if __name__ == '__main__':
    app.run(debug=True)