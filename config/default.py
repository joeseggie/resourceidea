"""Default configuration
"""
import os


class Config:
    """Default configuration settings
    """
    APP_NAME = 'resourceidea'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')
