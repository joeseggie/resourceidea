"""Application setup.
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def setup_app(app: Flask):
    """Setup the application.

    Parameters
    ----------
    app {Flask}
        Flask application to be setup.
    """
    config_name = os.getenv('FLASK_ENV', 'default')
    app.config.from_object(CONFIG_ENV[config_name])


CONFIG_ENV = {
    'default': 'config.default.Config',
    'development': 'config.development.DevelopmentConfig',
    'production': 'config.production.ProductionConfig',
    'testing': 'config.testing.TestingConfig',
}
app = Flask('resourceidea')
setup_app(app)
db = SQLAlchemy(app)
