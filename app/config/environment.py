from os import environ
from flask import Flask

def configureEnvironment(app: Flask):
    app.config.update(
        HOST = environ.get('HOST'),
        API_KEY = environ.get('API_KEY')
    )