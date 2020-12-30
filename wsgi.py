"""
------------------------
WSGI module
Entry point of the project.
------------------------
"""
import os
import sys
import inspect
from dotenv import load_dotenv
from os.path import join, dirname

# Loading the ENV file.
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

root_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# Add the app's directory to the PYTHONPATH
sys.path.append(f'{root_dir}')

from kickstarter import create_app

application = create_app()
