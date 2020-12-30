"""
------------------------
Validators module
Module for custom validations.
------------------------
"""
import re
from wtforms import ValidationError


def validate_email(form, field):
    """
    Checking the email is valid or not.
    @param form:
    @param field:
    @return: If validation fails, validator will return a validation error.
    """
    email = field.data
    regex = '^[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    email_regex = re.search(regex, email)
    if not email_regex:
        raise ValidationError('Please provide a valid email address.')
