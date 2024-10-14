from .settings import project
from home import render_home, home
from tour import render_tour, tour
from authorization import render_auth, authorization
from registration import render_register, registration
from user import render_user, user



project.add_url_rule(rule='/', view_func=render_home)

project.add_url_rule(rule='/tour', view_func=render_tour)

project.register_blueprint(blueprint=home)

project.register_blueprint(blueprint=tour)

project.add_url_rule(rule='/auth', view_func=render_auth, methods=['GET', 'POST'])

project.add_url_rule(rule='/reg', view_func=render_register, methods=['GET', 'POST'])

project.register_blueprint(blueprint=user)

project.register_blueprint(blueprint= authorization)

project.register_blueprint(blueprint= registration)





