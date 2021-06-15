import os

class Config():
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Royal12@localhost/pitch'
    SECRET_KEY = os.environ.get('SECRET_KEY')   
     #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") 


class prodConfig(Config):
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Royal12@localhost/pitch_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Royal12@localhost/pitch'

    DEBUG = True

config_options ={
    'development':DevConfig,
    'prodConfig': prodConfig
}