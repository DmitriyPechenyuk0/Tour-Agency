import flask, flask_login

home = flask.Blueprint(
    name='home_app',
    import_name='home',
    template_folder='templates',
    static_url_path='/home/',
    static_folder='static',
)