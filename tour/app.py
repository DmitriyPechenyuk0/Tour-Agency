import flask

tour = flask.Blueprint(
    name='tour',
    import_name='tour',
    template_folder='templates',
    static_folder='static',
    static_url_path='/tour/'
    )