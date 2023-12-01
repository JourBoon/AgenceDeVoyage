from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='public/static', template_folder='templates')

@app.route('/')
def home():
    yo = "Home Page"
    return render_template("home.html", voyages=yo)

@app.route('/reservation')
def reserver():
    yo = "Reserver"
    return render_template("reserver.html", voyages=yo)

if __name__ == '__main__':
    app.run(debug=True)