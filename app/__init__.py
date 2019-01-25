"""Application initializer.
"""
import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


CONFIG_ENV = {
    'default': 'config.default.Config',
    'development': 'config.development.DevelopmentConfig',
    'production': 'config.production.ProductionConfig',
    'testing': 'config.testing.TestingConfig',
}


def setup_app(app: Flask):
    """Setup the application.

    Parameters
    ----------
    app {Flask}
        Flask application to be setup.
    """
    config_name = os.getenv('FLASK_ENV', 'default')
    app.config.from_object(CONFIG_ENV[config_name])


app = Flask('resourceidea')
setup_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.routes.api.index import index_blueprint
from app.routes.api.company import company_blueprint


app.register_blueprint(
    index_blueprint,
    url_prefix='/api/v1.0'
)

app.register_blueprint(
    company_blueprint,
    url_prefix='/api/v1.0/companies'
)
