import flask, flask_login

home = flask.Blueprint(
    name='home_app',
    import_name='home',
    template_folder='templates'
)