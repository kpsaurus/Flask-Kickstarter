"""
------------------------
Error handler module
The module consists functions that helps the Flask to handle various HTTP errors.
------------------------
"""

from .loggers import error_logger
import traceback
import sys
from .functions import generate_final_data
from flask import request


def handle_401(error):
    """
    Function to handle the HTTP 401 errors.
    @param error:
    @return: final_data variable in dict format
    """
    final_data = generate_final_data('UNAUTHORIZED')
    return final_data, 401


def handle_404(error):
    """
    Function to handle the HTTP 404 errors.
    @param error:
    @return: final_data variable in dict format
    """
    final_data = generate_final_data('INVALID')
    return final_data, 404


def handle_405(error):
    """
    Function to handle the HTTP 405 errors.
    @param error:
    @return: final_data variable in dict format
    """
    final_data = generate_final_data('INVALID')
    return final_data, 405


def handle_500(e):
    """
    Function to handle the internal server errors (HTTP 500) or exceptions.
    @param e: Exception/error
    @return: final_data variable in dict format
    """
    etype, value, tb = sys.exc_info()
    detailed_traceback = traceback.format_exc()

    final_data = generate_final_data('ERROR')
    log_content = f'Exception Type: {etype} || Value: {value} || Traceback object: {tb} || Traceback details: {detailed_traceback}'

    # Logging the error into the log file.
    error_logger(f'Route: {request.path}').error(log_content)

    return final_data, 500
