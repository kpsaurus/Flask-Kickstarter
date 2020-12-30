"""
------------------------
Kickstarter module
------------------------
"""

from flask import Flask

from kickstarter.settings import CURRENT_ENV


def create_app():
    """
    Function to create a Flask application object.
    @return:
    """
    # Creating the Flask application object.
    app = Flask(__name__, instance_relative_config=True)

    if CURRENT_ENV == 'development':
        # Loading the development configuration.
        app.config.from_object('config.DevelopmentConfig')
    elif CURRENT_ENV == 'production':
        # Loading the production configuration.
        app.config.from_object('config.ProductionConfig')
    else:
        # default environment is development.
        app.config.from_object('config.DevelopmentConfig')

    register_extensions(app)

    register_blueprints(app)

    register_error_handlers(app)

    @app.route('/')
    def index():
        return "Hello World!"

    return app


def register_extensions(app):
    """
    Function to register the Flask extensions
    @param app: Flask application object
    """
    pass


def register_blueprints(app):
    """
    Function to register Flask blueprints
    @param app: Flask application object
    """
    from kickstarter.blueprints.app.controller import app_blueprint
    app.register_blueprint(app_blueprint)


def register_error_handlers(app):
    """
    Function to register Flask error handlers.
    @param app: Flask application object
    """
    from kickstarter.generic.error_handlers import handle_401, handle_404, handle_405, handle_500

    app.register_error_handler(401, handle_401)
    app.register_error_handler(404, handle_404)
    app.register_error_handler(405, handle_405)
    app.register_error_handler(Exception, handle_500)
