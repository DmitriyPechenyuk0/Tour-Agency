import flask, flask_sqlalchemy, flask_migrate, os
project = flask.Flask(
    import_name='main',
    template_folder='templates',
    instance_path=os.path.abspath(__file__ + '/..'),
    static_folder='static',
    static_url_path='/static/'
)

project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

DATABASE = flask_sqlalchemy.SQLAlchemy(app = project)
MIGRATE = flask_migrate.Migrate(app = project, db = DATABASE)