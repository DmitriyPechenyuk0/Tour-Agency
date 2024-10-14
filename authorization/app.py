import flask

authorization = flask.Blueprint(
    name="authorization",
    import_name="app",
    template_folder="autho/templates"
    )