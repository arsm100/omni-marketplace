import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

import config

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# session options parameter is used to override session options. If provided it's a dict of parameters passed to the session's 
db = SQLAlchemy(app, session_options={"autoflush": False})
# db = SQLAlchemy(app)

Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "sessions.sign_in"

# import user model so that you can run migration
from omni_marketplace.users.model import User

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None

# Grab the blueprints from the other views.py files for each "app"
# make sure route and method is defined in views.py
# from omni_marketplace.users.views import users_blueprint
# from omni_marketplace.sessions.views import sessions_blueprint

# app.register_blueprint(users_blueprint, url_prefix="/users")
# app.register_blueprint(sessions_blueprint, url_prefix='/')