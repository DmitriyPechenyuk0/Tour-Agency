import flask
from .models import User



def render_user():
    if flask.request.method == 'POST':
        print(flask.request.form)
        user = User(
            login = flask.request.form['login'],
            email = flask.request.form['email'],
            password = flask.request.form['password']
        )
    return flask.render_template(template_name_or_list='user.html')