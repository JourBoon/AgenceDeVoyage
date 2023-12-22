import sys
sys.path.append('static/services')
sys.path.append('static/models')
sys.path.append('static/services/exceptions')
from app import app
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from database import db

auth = Blueprint('auth', __name__)

@auth.route('/connexion')
def login():
    return render_template('connexion.html')

@auth.route('/inscription')
def signup():
    return render_template('inscription.html')

@auth.route('/inscription', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.inscription'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.connexion'))
