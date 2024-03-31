import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', 'Sem id google')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', 'Sem script google')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'uma_chave_secreta_padrao')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///default.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
