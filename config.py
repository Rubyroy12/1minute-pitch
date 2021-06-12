import os

class Config():
    pass


class prodConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options ={
    'development':DevConfig,
    'prodConfig': prodConfig
}