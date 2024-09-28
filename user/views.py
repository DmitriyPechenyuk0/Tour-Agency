import flask


def render_user():
    return flask.render_template(template_name_or_list='user.html')