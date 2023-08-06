import os
from os import environ

from openwebpos.utils import gen_urlsafe_token

SECRET_KEY = gen_urlsafe_token(16)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# database
DIALECT = environ.get('DB_DIALECT', 'sqlite')
DRIVER = None
DB_USER = environ.get('DB_USER')
DB_PASS = environ.get('DB_PASS')
HOST = environ.get('DB_HOST')
PORT = environ.get('DB_PORT')
DB_NAME = environ.get('DB_NAME')

if DIALECT == 'sqlite':
    db_uri = 'sqlite:///' + os.path.join(os.getcwd(), 'openwebpos.db')
elif DRIVER is None:
    db_uri = f'{DIALECT}+{DRIVER}://{DB_USER}:{DB_PASS}@{HOST}:{PORT}/{DB_NAME}'
else:
    db_uri = f'{DIALECT}://{DB_USER}:{DB_PASS}@{HOST}:{PORT}/{DB_NAME}'

SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
