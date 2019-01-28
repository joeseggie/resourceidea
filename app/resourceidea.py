"""Application initializer.
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


CONFIG_ENV = {
    'default': 'config.default.Config',
    'development': 'config.development.DevelopmentConfig',
    'production': 'config.production.ProductionConfig',
    'testing': 'config.testing.TestingConfig',
}
app = Flask('resourceidea')
config_name = os.getenv('FLASK_ENV', 'default')
app.config.from_object(CONFIG_ENV[config_name])
db = SQLAlchemy(app)
