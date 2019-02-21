'''
Application initialization.
'''
import os

from flask import Flask
from database import db
from flask_migrate import Migrate

from . import models
from .views.index import home_bp


CONFIG_ENV = {
    'default': 'config.default.Config',
    'development': 'config.development.DevelopmentConfig',
    'production': 'config.production.ProductionConfig',
    'testing': 'config.testing.TestingConfig',
}


migrate = Migrate()


def create_app():
    app = Flask('resourceidea')
    config_name = os.getenv('FLASK_ENV', 'default')
    app.config.from_object(CONFIG_ENV[config_name])
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_bp)

    return app


app = create_app()
