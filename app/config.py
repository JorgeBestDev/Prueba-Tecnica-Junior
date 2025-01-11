
import os
import secrets
SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(32))
SQLALCHEMY_DATABASE_URI = 'sqlite:///prueba_tecnica.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False