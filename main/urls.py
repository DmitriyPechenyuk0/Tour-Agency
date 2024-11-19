from .settings import project
from home import render_home, home
from tour import render_tour, tour, render_particular_tour
from user import render_authorization, render_register, user



project.add_url_rule(rule='/', view_func=render_home, methods=['GET', 'POST'])

project.add_url_rule(rule='/tour/', view_func=render_tour, methods= ['GET','POST'])

project.add_url_rule(rule='/tour/particular_tour/', view_func=render_particular_tour, methods= ['GET','POST'])

project.add_url_rule(rule='/registration/', view_func=render_register, methods=['GET', 'POST'])

project.add_url_rule(rule='/authorization/', view_func=render_authorization, methods=['GET', 'POST'])

project.register_blueprint(blueprint=home)

project.register_blueprint(blueprint=tour)

project.register_blueprint(blueprint=user)
