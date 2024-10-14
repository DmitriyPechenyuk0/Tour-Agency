import flask, flask_login, flask_sqlalchemy
from .models import User
from flask_login import UserMixin
import main.settings 
from main.settings import DATABASE



def render_user():
    if flask.request.method == 'POST':
        print(flask.request.form)
        user = User(
            login = flask.request.form['login'],
            email = flask.request.form['email'],
            password = flask.request.form['password']
        )
    return flask.render_template(template_name_or_list='user.html')


class User(UserMixin, DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    login = DATABASE.Column(DATABASE.String(150), unique=True, nullable=False)
    email = DATABASE.Column(DATABASE.String(150), unique=True, nullable=False)
    password = DATABASE.Column(DATABASE.String(150), nullable=False)

def load_user(user_id):
    return User.query.get(int(user_id))


def render_register():
    if request.method == 'POST':
        login = request.form['login']
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        return flask.render_template(template_name_or_list="reg.html")

def render_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        return flask.render_template(template_name_or_list='auth.html')







