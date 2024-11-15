import flask
from main.settings import DATABASE
from .models import Tour
from flask_login import current_user

id_of_tour = 0
choosen_tour = False
def render_tour():
    global id_of_tour, choosen_tour
    if flask.request.method == 'POST':
        id_of_tour = flask.request.form["url"]
        choosen_tour = True
        return flask.redirect('/tour/particular_tour/')
    try:
        user = current_user
    except Exception as exception:
        print(exception)

    return flask.render_template(template_name_or_list = 'tour.html', tours= Tour.query.all(), user= user)

def render_particular_tour():
    global id_of_tour, choosen_tour

    try:
        user = current_user
    except Exception as exception:
        print(exception)
    
    return flask.render_template(template_name_or_list = 'particular_tour.html', tour = Tour.query.filter_by(id=id_of_tour), user = user, choosen_tour = choosen_tour)