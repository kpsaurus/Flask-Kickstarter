"""
------------------------
Controller module
Main module of this blueprint.
------------------------
"""
from flask import Blueprint

from kickstarter.middlewares.auth_guard import api_key_required
from kickstarter.generic.functions import generate_final_data, populate_errors
from kickstarter.blueprints.app.forms import ProfileForm

# creating a new Flask Blueprint called app.
app_blueprint = Blueprint("app", __name__, url_prefix='/app')


@app_blueprint.route('/')
def index():
    """
    Index route.
    """
    return generate_final_data('INFO', "Hey, you're in the app route!")


@app_blueprint.route('/protected')
@api_key_required
def protected_route():
    return generate_final_data('INFO', "Hey, you're in the protected route!")


@app_blueprint.route('/profile', methods=['POST'])
@api_key_required
def profile():
    """
    Profile route. A sample API for handling a POST request and returns the result.
    """
    form = ProfileForm()
    if form.validate_on_submit():
        # Successfully validated the form.
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = '' if form.email.data == '' else f" ({form.email.data})"
        message = f"Hey {first_name} {last_name}{email}, have a great day!"
        # Setting up the final data that needs to be returned.
        final_data = generate_final_data('INFO', message)
    else:
        # Form validation error.
        final_data = generate_final_data('FORM_ERROR')
        final_data['errors'] = populate_errors(form.errors)

    # Returns the final data in JSON format.
    return final_data
