import flask
from .models import User, DATABASE

def render_register():
    if flask.request.method == 'POST':

        user = User(
            username = flask.request.form['username'],
            password = flask.request.form['password'],
        )
    return flask.render_template(template_name_or_list="registration.html")