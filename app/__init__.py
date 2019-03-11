'''
Application initialization.
'''

from database import db
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from .views.index import Index
from .views.assignment import AssignmentResource
from .views.service_plan import ServicePlanListResource, ServicePlanResource


CONFIG_ENV = {
    'default': 'config.default.Config',
    'development': 'config.development.DevelopmentConfig',
    'production': 'config.production.ProductionConfig',
    'testing': 'config.testing.TestingConfig',
}


migrate = Migrate()


def create_app(config_name='default'):
    app = Flask('resourceidea')
    app.config.from_object(CONFIG_ENV[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)

    api.add_resource(Index, '/api/v1')
    api.add_resource(AssignmentResource, '/api/v1/assignments')
    api.add_resource(ServicePlanListResource, '/api/v1/serviceplans')
    api.add_resource(ServicePlanResource, '/api/v1/serviceplans/<int:id>')

    return app
