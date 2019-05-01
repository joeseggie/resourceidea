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
    ENV = 'testing'
    ROOT_DIR = '/Users/jserunjogi/source/repos/eastseat/python/flask/resourceidea'
    TEST_DB = os.path.join(ROOT_DIR, 'tests', 'test_resourceidea.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + TEST_DB
