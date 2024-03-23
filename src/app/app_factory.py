from flask import Flask
from flasgger import Swagger
from app.models.Core import db, migrate
from app.views.Dummy import DummyView
from app.views.Tracking import TrackingView
import os

def register_api(app, name, view, root_element='/'):
    item = view.as_view(f'{name}')
    path = os.path.join(root_element, f'{name}')
    app.add_url_rule(path, f'{name}', view_func=item)
    app.add_url_rule(f'{path}/<uuid:id>', f'{name}', view_func=item)

def register_endpoints(app):
    register_api(app, '/dummy', DummyView)
    register_api(app, '/track', TrackingView)

def setup_database(app):
    db.init_app(app)
    migrate.init_app(app, db)

def create_app():
    app = Flask(__name__)

    _env = os.environ.get('FLASK_ENV')
    app.config.from_object(f'app.config.{_env}')

    Swagger(app, template_file=os.path.join('.', 'docs', 'template.yaml'))

    register_endpoints(app)
    setup_database(app)
    #Marshmallow(app)

    return app
