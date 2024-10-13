import flask, os, pandas
from main.settings import DATABASE
from .models import Tour




def render_tour():
    if Tour.query.count() >= 3:
        return flask.render_template(template_name_or_list='tour.html', tours=Tour.query.all())
    
    else:
        return flask.render_template(template_name_or_list='tour.html', tours=Tour.query.all())
    


