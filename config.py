

import os

class Config:
    # db config
    SQLALCHEMY_DATABASE_URI = 'sqlite:///employees.db' # can modify to use diff db systems 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # app config
    PORT = 1111
    
    # auth config
    AUTH_USERNAME = 'admin'
    AUTH_PASSWORD = 'password'
