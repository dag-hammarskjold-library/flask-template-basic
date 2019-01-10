from pymongo import MongoClient

class Config(object):
    SOURCE_LANGUAGE = 'en'
    TARGET_LANGUAGES = ['ar','zh','ru','es']

    # how many results per page
    RPP = 10

    # If you need to access other AWS resources from within your application,
    # define your access credentials here.
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
    
class ProductionConfig(Config):
    DEBUG = False
    
class DevelopmentConfig(Config):
    # Provide overrides for production settings here.
    DEBUG = True
