"""Testing environment configuration.
"""
import os

from config.default import Config


class TestingConfig(Config):
    """Testing configurations.

    Parameters
    ----------
    Config
        Base configuration settings.
    """
    DEBUG = False
    TESTING = True
    ENV = 'staging'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_SQLALCHEMY_DATABASE_URI')
