"""
Application initialization.
"""
from flask import Flask
from flask_migrate import Migrate

from database import db
from app.auth.endpoints import auth_bp
from app.role.endpoints import role_bp
from app.organization.endpoints import organization_bp
from app.user.endpoints import user_bp


CONFIG_ENV = {
    'default': 'config.default.Config',
    'development': 'config.development.DevelopmentConfig',
    'production': 'config.production.ProductionConfig',
    'testing': 'config.testing.TestingConfig',
}
API_URL_PREFIX = '/api/v0.1'


migrate = Migrate()


def create_app(config_name='default'):
    """
    App creation factory.

    Args:
        config_name: Environment configuration.

    Returns:
        Flask app for the environment configured.
    """
    app = Flask('resourceidea')
    app.config.from_object(CONFIG_ENV[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(organization_bp, url_prefix=API_URL_PREFIX)
    app.register_blueprint(user_bp, url_prefix=API_URL_PREFIX)
    app.register_blueprint(auth_bp, url_prefix=API_URL_PREFIX)
    app.register_blueprint(role_bp, url_prefix=API_URL_PREFIX)

    return app
