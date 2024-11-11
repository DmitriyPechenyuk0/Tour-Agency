import flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
import flask_migrate, flask_sqlalchemy

project = flask.Flask(
    import_name='main',
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/'
)

project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

DATABASE = flask_sqlalchemy.SQLAlchemy(app = project)

MIGRATE = flask_migrate.Migrate(app = project, db = DATABASE)




    