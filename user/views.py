import flask
import flask_login
from .models import User
from main.settings import DATABASE


def render_register():
    if flask.request.method == 'POST':

        user = User(
            username = flask.request.form['username'],
            password = flask.request.form['password']
        )
        DATABASE.session.add(user)
        DATABASE.session.commit()
        return flask.redirect('/authorization')
    return flask.render_template(template_name_or_list='registration.html')

def render_authorization():
    
    if flask.request.method == "POST":
        for user in User.query.filter_by(username = flask.request.form['username']):
            if user.password == flask.request.form["password"]:
                flask_login.login_user(user)
                return flask.redirect("/")
            

    return flask.render_template(template_name_or_list='authorization.html')