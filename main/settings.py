import flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message

project = flask.Flask(
    import_name='main',
    template_folder='templates',
)

project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

DATABASE = flask_sqlalchemy.SQLAlchemy(app = project)

MIGRATE = flask_migrate.Migrate(app = project, db = DATABASE)

project.config['MAIL_SERVER'] = 'smtp.gmail.com'
project.config['MAIL_PORT'] = 465
project.config['MAIL_USE_SSL'] = True
project.config['MAIL_USERNAME'] = 'touragent.practice@gmail.com'
project.config['MAIL_PASSWORD'] = 'prwp rafv yylt xfgu'  
project.config['MAIL_DEFAULT_SENDER'] = 'touragent.practice@gmail.com'

    