from flask import Flask
from flask import render_template

app = Flask(__name__ ,template_folder='templates', static_folder='static')

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
def inscription():
    yo = "Connexion"
    return render_template("connexion.html", voyages=yo)

if __name__ == '__main__':
    app.run(debug=True)