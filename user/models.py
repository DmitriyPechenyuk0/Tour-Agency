from main.settings import DATABASE
from flask_login import UserMixin

class User(DATABASE.Model, UserMixin):
    id = DATABASE.Column(DATABASE.Integer(), primary_key = True)
    username = DATABASE.Column(DATABASE.Text, nullable=False)
    password = DATABASE.Column(DATABASE.Text, nullable=False)

    def __repr__(self) -> str:
        return f"id: {self.id}"