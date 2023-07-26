from os import environ 

FLASK_APP = environ.get('FLASK_APP')
FLASK_ENV = environ.get('FLASK_ENV')
FLASK_DEBUG = environ.get('FLASK_DEBUG')
AUTH_KEY = environ.get('AUTH_KEY')