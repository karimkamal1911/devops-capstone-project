"""
Module: error_handlers
"""
from flask import jsonify
from service.models import DataValidationError
from service import app
from . import status


######################################################################
# Error Handlers
######################################################################
@app.errorhandler(DataValidationError)
def request_validation_error(error):
    """Handle data validation errors"""
    return bad_request(error)


@app.errorhandler(status.HTTP_400_BAD_REQUEST)
def bad_request(error):
    """Handle bad requests (400 Bad Request)"""
    message = str(error)
    app.logger.warning(f"400 Bad Request: {message}")
    return (
        jsonify(
            status=status.HTTP_400_BAD_REQUEST,
            error="Bad Request",
            message=message,
        ),
        status.HTTP_400_BAD_REQUEST,
    )


@app.errorhandler(status.HTTP_404_NOT_FOUND)
def not_found(error):
    """Handle not found errors (404 Not Found)"""
    message = str(error)
    app.logger.warning(f"404 Not Found: {message}")
    return (
        jsonify(
            status=status.HTTP_404_NOT_FOUND,
            error="Not Found",
            message=message,
        ),
        status.HTTP_404_NOT_FOUND,
    )


@app.errorhandler(status.HTTP_405_METHOD_NOT_ALLOWED)  # pragma: no cover
def method_not_supported(error):  # pragma: no cover
    """Handle method not allowed errors (405 Method Not Allowed)"""
    message = str(error)
    app.logger.warning(f"405 Method Not Allowed: {message}")
    return (
        jsonify(
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            error="Method Not Allowed",
            message=message,
        ),
        status.HTTP_405_METHOD_NOT_ALLOWED,
    )


@app.errorhandler(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)  # pragma: no cover
def mediatype_not_supported(error):  # pragma: no cover
    """Handle unsupported media type errors (415 Unsupported Media Type)"""
    message = str(error)
    app.logger.warning(f"415 Unsupported Media Type: {message}")
    return (
        jsonify(
            status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            error="Unsupported Media Type",
            message=message,
        ),
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
    )


@app.errorhandler(status.HTTP_500_INTERNAL_SERVER_ERROR)  # pragma: no cover
def internal_server_error(error):  # pragma: no cover
    """Handle internal server errors (500 Internal Server Error)"""
    message = str(error)
    app.logger.error(f"500 Internal Server Error: {message}")
    return (
        jsonify(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error="Internal Server Error",
            message=message,
        ),
        status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
