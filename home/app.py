import flask

home = flask.Blueprint(
    name='home_app',
    import_name='home',
    template_folder='templates'
)