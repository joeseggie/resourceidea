"""Production environment configuration.
"""
from config.default import Config


class ProductionConfig(Config):
    """Production configurations.

    Parameters
    ----------
    Config
        Base configuration settings.
    """
    DEBUG = False
