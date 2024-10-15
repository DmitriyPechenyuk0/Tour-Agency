import flask

tour = flask.Blueprint(
    name='tour',
    import_name='tour',
    template_folder='templates',
    )