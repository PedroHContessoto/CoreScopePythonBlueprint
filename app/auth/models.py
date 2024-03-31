from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, index=True)
    is_admin = db.Column(db.Boolean, default=False)
    is_approved = db.Column(db.Boolean, default=False)  # Indica se o usuário está aprovado
    on_waiting_list = db.Column(db.Boolean, default=True)  # Usuários novos entram na lista de espera

    def set_admin(self):
        self.is_admin = True
