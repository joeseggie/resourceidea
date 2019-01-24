"""Testing environment configuration.
"""
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
