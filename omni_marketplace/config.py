import os
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from omni_marketplace import app

# SET UP OUR POSTGRESQL DATABASE #####
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connects our Flask App to our Database
db = SQLAlchemy(app)

# Add on migration capabilities in order to run terminal commands
Migrate(app, db)

# Secret Key setup
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


# App Environment Conditions
class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    # GOOGLE_CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']
    # GOOGLE_CLIENT_SECRET = os.environ['GOOGLE_CLIENT_SECRET']


class DevelopmentConfig(Config):
    DEBUG = True
    # GOOGLE_CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']
    # GOOGLE_CLIENT_SECRET = os.environ['GOOGLE_CLIENT_SECRET']
    # SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True
