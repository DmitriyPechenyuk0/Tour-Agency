import flask, flask_login
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



def render_authorization():
    if flask.request.method == "POST":
        for user in User.query.filter_by(login = flask.request.form['login']):
            if user.password == flask.request.form['password']:
                flask_login.login_user(user)
    return flask.render_template(template_name_or_list='user.html')



def render_register():
    if flask.request.method == 'POST':
        user = User(
            login = flask.request.form['login'],
            email = flask.request.form['email'],
            password = flask.request.form['password']
            )        
    return flask.render_template(template_name_or_list="user.html")