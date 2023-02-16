from flask import Flask

app = Flask(__name__)

import my_app.views

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
app.config.from_object(Config)