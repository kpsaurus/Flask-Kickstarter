"""
------------------------
Authentication module
------------------------
"""

from flask import request, current_app
from functools import wraps
from kickstarter.generic.functions import generate_final_data


def api_key_required(func):
    """
    A wrapper function that deals with the checking of Api-Key token in the request header.
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('api-key')
        if api_key == current_app.config["API_KEY"]:
            valid = True
        else:
            valid = False
        if valid:
            return func(*args, **kwargs)
        else:
            return generate_final_data('INVALID_API_KEY')

    return wrapper
