import os

SECRET_KEY = ''
FLASK_APP = os.environ.get('FLASK_APP')
FLASK_ENV = os.environ.get('FLASK_ENV')

DEBUG = True
TEMPLATES_AUTO_RELOAD = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{username}:{passwword}@{host}/{db_name}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

JSON_AS_ASCII = False
