"""
------------------------
Forms module
Module for form classes.
------------------------
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length, Optional
from .validators import validate_email


class ProfileForm(FlaskForm):
    """
    WTF form class for validating the profile API request.
    """

    class Meta:
        csrf = False

    first_name = StringField('first_name', validators=[InputRequired(), Length(min=2,
                                                                               message="First name should be at least 2 characters long."), ])
    last_name = StringField('last_name', validators=[InputRequired()])
    email = StringField('email', validators=[Optional(), validate_email])
