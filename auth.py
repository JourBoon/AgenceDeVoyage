from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'votre_clé_secrète'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = request.form.get('remember')

        # Vérifiez les informations d'identification (par exemple, dans une base de données)

        # Si les informations d'identification sont valides, connectez l'utilisateur et stockez ses informations dans la session
        session['username'] = username

        # Si l'utilisateur a demandé à se souvenir de lui, configurez un cookie sécurisé
        if remember:
            session.permanent = True

        return redirect(url_for('accueil'))

    return render_template('login.html')

@app.route('/accueil')
def accueil():
    # Obtenez les informations de l'utilisateur à partir de la session
    username = session.get('username')
    return render_template('accueil.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
