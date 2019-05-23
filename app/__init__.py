'''
Application initialization.
'''
from flask import Flask
from flask_migrate import Migrate

from database import db
from .views.index import Index
from .views.assignment import AssignmentListResource, AssignmentResource
from .views.service_plan import ServicePlanListResource, ServicePlanResource
from app.assignment_status.endpoints import assignment_status_bp
from app.organization.endpoints import company_bp


CONFIG_ENV = {
    'default': 'config.default.Config',
    'development': 'config.development.DevelopmentConfig',
    'production': 'config.production.ProductionConfig',
    'testing': 'config.testing.TestingConfig',
}
API_URL_PREFIX = '/api/v0.1'


migrate = Migrate()


def create_app(config_name='default'):
    app = Flask('resourceidea')
    app.config.from_object(CONFIG_ENV[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    # api = Api(app)

    # api.add_resource(Index, '/api/v1')
    # api.add_resource(AssignmentListResource, '/api/v1/assignments')
    # api.add_resource(AssignmentResource, '/api/v1/assignments/<int:id>')
    # api.add_resource(ServicePlanListResource, '/api/v1/serviceplans')
    # api.add_resource(ServicePlanResource, '/api/v1/serviceplans/<int:id>')
    app.register_blueprint(company_bp, url_prefix=f'{API_URL_PREFIX}')
    app.register_blueprint(
        assignment_status_bp,
        url_prefix=f'{API_URL_PREFIX}')

    return app
