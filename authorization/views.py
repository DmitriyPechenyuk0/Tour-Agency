import flask
import flask_login
from main import login_manager
from registration.models import User

def render_auth():
    if flask.request.method == "POST":
        for user in User.query.filter_by(username = flask.request.form['username']):
            if user.password == flask.request.form['password']:
                flask_login.login_user(user)
                return flask.redirect('/')
        return flask.redirect('/authorization_next')
    return flask.render_template('autho.html')