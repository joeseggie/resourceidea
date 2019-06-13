"""
Application initialization.
"""
from flask import Flask
from flask_migrate import Migrate

from database import db
from app.auth.endpoints import auth_bp
from app.auth.views import auth_views_bp
from app.client_industry.endpoints import client_industry_bp
from app.organization.endpoints import organization_bp
from app.role.endpoints import role_bp
from app.user.endpoints import user_bp


CONFIG_ENV = {
    'default': 'config.default.Config',
    'development': 'config.development.DevelopmentConfig',
    'production': 'config.production.ProductionConfig',
    'testing': 'config.testing.TestingConfig',
}
API_URL_PREFIX = '/api/v0.1'
URL_PREFIX = '/signup'


migrate = Migrate()


def create_app(config_name='default'):
    """
    App creation factory.

    Args:
        config_name: Environment configuration.

    Returns:
        Flask app for the environment configured.
    """
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(CONFIG_ENV[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(organization_bp, url_prefix=API_URL_PREFIX)
    app.register_blueprint(user_bp, url_prefix=API_URL_PREFIX)
    app.register_blueprint(auth_bp, url_prefix=API_URL_PREFIX)
    app.register_blueprint(role_bp, url_prefix=API_URL_PREFIX)
    app.register_blueprint(auth_views_bp, url_prefix=URL_PREFIX)
    app.register_blueprint(client_industry_bp, url_prefix=API_URL_PREFIX)
    return app
