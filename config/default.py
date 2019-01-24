"""Default configuration
"""
import os


class Config:
    """Default configuration settings
    """
    APP_NAME = 'resourceidea'
    DEBUG = False
    MYSQL_DB = os.environ.get('MYSQL_DB')
    SECRET_KEY = os.environ.get('SECRET_KEY')
