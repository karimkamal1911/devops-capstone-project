"""
Package: service
Package for the application models and service routes
This module creates and configures the Flask app and sets up the logging
and SQL database
"""
import sys
import logging
from flask import Flask
from service import config
from service.common import log_handlers

def create_app(test_config=None):
    """Application factory function"""
    app = Flask(__name__)
    
    # Configure application
    app.config.from_object(config)
    if test_config:
        app.config.update(test_config)

    # Initialize common components
    initialize_logging(app)
    initialize_extensions(app)
    
    return app

def initialize_logging(app):
    """Set up logging"""
    log_handlers.init_logging(app, "gunicorn.error")
    logger = logging.getLogger("flask.app")
    logger.info(70 * "*")
    logger.info("  A C C O U N T   S E R V I C E   R U N N I N G  ".center(70, "*"))
    logger.info(70 * "*")

def initialize_extensions(app):
    """Initialize database and other extensions"""
    try:
        from service.models import init_db
        init_db(app)  # Initialize database tables
        logger = logging.getLogger("flask.app")
        logger.info("Service initialized!")
    except Exception as error:  # pylint: disable=broad-except
        logger = logging.getLogger("flask.app")
        logger.critical("%s: Cannot continue", error)
        sys.exit(4)

# Create default app instance
app = create_app()

# Import routes and components after app creation to avoid circular imports
# pylint: disable=wrong-import-position, cyclic-import, wrong-import-order
from service import routes, models  # noqa: F401 E402
from service.common import error_handlers, cli_commands  # noqa: F401 E402