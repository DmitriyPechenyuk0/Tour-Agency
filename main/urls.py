from .settings import project
from home import render_home, home
from tour import render_tour, tour



project.add_url_rule(rule='/', view_func=render_home)

project.add_url_rule(rule='/tour', view_func=render_tour)

project.register_blueprint(blueprint=home)

project.register_blueprint(blueprint=tour)