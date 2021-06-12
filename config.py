import os

class Config():
       SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Royal12@localhost/pitch'
    


class prodConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options ={
    'development':DevConfig,
    'prodConfig': prodConfig
}