from .settings import project
from home import render_home, home
from user import render_authorization,render_register, user



project.add_url_rule(rule='/', view_func=render_home)



project.register_blueprint(blueprint=home)


project.add_url_rule(rule='/authorization', view_func=render_authorization, methods=['GET', 'POST'])

project.add_url_rule(rule='/registration', view_func=render_register, methods=['GET', 'POST'])

project.register_blueprint(blueprint=user)






