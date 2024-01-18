from flask_login import UserMixin
import app

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@app.login_manager.user_loader
def load_user(user_id):
    # Remplacer cette fonction par votre propre logique pour charger l'utilisateur à partir de la base de données
    return User(user_id)