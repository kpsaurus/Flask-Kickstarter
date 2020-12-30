"""
------------------------
Generic functions module
The module consists utility functions that can be used in various scenarios.
------------------------
"""


def generate_final_data(status_code, custom_message=False, key=False):
    """
    Function to generate the final data dict that needs to be sent back to client.
    @param status_code: App specific status_code (string constants)
    @param custom_message: Custom string message
    @param key: specific key
    @return: generated final_data variable
    """
    if status_code == 'INVALID':
        final_data = {"status": "failed", "message": "Invalid request"}

    elif status_code == 'UNAUTHORIZED':
        final_data = {"status": "failed", "message": "Unauthorized access."}

    elif status_code == 'FAILED':
        final_data = {"status": "failed", "message": custom_message}

    elif status_code == 'API_KEY_NOT_FOUND':
        final_data = {"status": "failed", "message": "API Key is not provided"}

    elif status_code == 'INVALID_API_KEY':
        final_data = {"status": "failed", "message": "Invalid API key"}

    elif status_code == 'KEY_NOT_PROVIDED':
        final_data = {"status": "failed", "message": f"The key '{key}' is not provided"}

    elif status_code == 'ERROR':
        final_data = {"status": "failed", "message": "Please try again after some time"}

    elif status_code == 'FORM_ERROR':
        final_data = {"status": "failed", "message": "Validation error"}

    elif status_code == 'SUCCESS':
        final_data = {"status": "success", "message": custom_message}

    elif status_code == 'INFO':
        final_data = {"status": "success", "message": custom_message}

    elif status_code == 'FOUND':
        final_data = {"status": "success", "message": "Successfully retrieved the data"}

    elif status_code == 'NOT_FOUND':
        final_data = {"status": "success", "message": "No data found"}

    elif status_code == 'SAVED':
        final_data = {"status": "success", "message": "Successfully saved"}

    elif status_code == 'SAVE_FAILED':
        final_data = {"status": "failed", "message": "Failed to save"}

    elif status_code == 'UPDATED':
        final_data = {"status": "success", "message": "Successfully updated"}

    elif status_code == 'UPDATE_FAILED':
        final_data = {"status": "failed", "message": "Failed to update"}

    elif status_code == 'DELETED':
        final_data = {"status": "success", "message": "Successfully deleted"}

    elif status_code == 'DELETE_FAILED':
        final_data = {"status": "failed", "message": "Failed to delete"}

    else:
        final_data = {"status": "failed", "message": "Invalid request"}
    return final_data


def populate_errors(errors):
    """
    Method for populating errors from WTF forms
    @param errors: Flask-WTF form errors object
    @return: Final list of errors
    """
    error_list = []
    for key, values in errors.items():
        error_list.append({'field': key, 'errors': values})
    return error_list
