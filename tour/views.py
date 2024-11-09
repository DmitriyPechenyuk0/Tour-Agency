import flask
from main.settings import DATABASE
from .models import Tour

def render_tour():

    return flask.render_template(template_name_or_list='tour.html', tours= Tour.query.all())

def render_particular_tour(ptour):
        return flask.render_template(template_name_or_list='tour_particular.html', tour = ptour)