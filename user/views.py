import flask
from .models import User, DATABASE
from flask_login import current_user, login_user


def render_register():
    if flask.request.method == 'POST':

        user = User(
            username = flask.request.form['username'],
            password = flask.request.form['password']
        )
        DATABASE.session.add(user)
        DATABASE.session.commit()
    return flask.render_template(template_name_or_list='registration.html')

def render_authorization():
    if flask.request.method == "POST":
        for user in User.query.filter_by(username = flask.request.form['username']):
            if user.password == flask.request.form["password"]:
                login_user(user)
                return flask.redirect("/")
            

    return flask.render_template(template_name_or_list='authorization.html')
