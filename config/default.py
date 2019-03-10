"""Default configuration
"""
import os


class Config:
    """Default configuration settings
    """
    APP_NAME = 'resourceidea'
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'production'
