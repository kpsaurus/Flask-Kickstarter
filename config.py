"""
------------------------
Flask application configuration module
------------------------
"""
import os


class Config(object):
    """
    Parent config class.
    """
    API_KEY = os.getenv("API_KEY")
    DEBUG = True
    TESTING = True
    PROPAGATE_EXCEPTIONS = True
    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = True


class DevelopmentConfig(Config):
    """
    Configuration for the development environment.
    """
    pass


class ProductionConfig(Config):
    """
    Configuration for the production environment.
    """
    DEBUG = False
    TESTING = False
