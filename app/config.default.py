
from pymongo import MongoClient

class Config(object):
    SOURCE_LANGUAGE = 'en'
    TARGET_LANGUAGES = ['ar','zh','ru','es']

    # how many results per page
    RPP = 10

    AWS_ACCESS_KEY_ID = 'your key here'
    AWS_SECRET_ACCESS_KEY = 'your secret access key here'

    DB_CLIENT = MongoClient(
        'localhost',
        port=27017,
        username='username',
        password='password',
        authSource='authentication database',
        authMechanism='SCRAM-SHA-256'
    )

    DB = DB_CLIENT['database']

    EN_FEED_URL = 'https://www.un.org/press/en/feed'

    UPDATE_TOKEN = 'generate a UUID and put it here'
    
class ProductionConfig(Config):
    DEBUG = False
    
class DevelopmentConfig(Config):
    # Provide overrides for production settings here.
    DEBUG = True
