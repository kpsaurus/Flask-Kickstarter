Flask Kickstarter 🚀
======

![Python: 3.8](https://img.shields.io/badge/Python-v3.8-green)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)

===========

A simple ready-to-go app written in Flask framework with minimal boiler plate code to kick-start your project.

Introduction
------------

Managing the Flask application logic in one file will become a tedious task as the project grows. This kick-starter project bifurcates the application logic into smaller modules - hence, achieves a greater control over the code base. 

Setup
--------

  1. Clone the repository:

        ```git clone https://github.com/kpsaurus/flask-kickstarter```
        
        ```cd flask-kickstarter```
    
  2. Create and activate the virtual environment:

        ```virtualenv env```
        
        ```source env/bin/activate```

  3. Install requirements:

        ```pip install -r requirements.txt```
        
  4. Set FLASK_ENV and API_KEY environment variables.
        
       
  5. Run the application:
        
        Windows CMD:
        ```set FLASK_APP=wsgi.py```
        
        Unix Bash (Linux, Mac, etc.):
        ```export FLASK_APP=wsgi.py```
        
        ```flask run```

