from omni_marketplace.users.model import User
import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_assets import Bundle, Environment

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


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None

# Home Page
@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('home', id=current_user.id))
    else:
        return render_template('home.html')


# Grab the blueprints from the other views.py files for each "app"
# make sure route and method is defined in views.py
from omni_marketplace.users.views import users_blueprint
from omni_marketplace.sessions.views import sessions_blueprint
app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(sessions_blueprint, url_prefix='/')


# Flask_Assets
assets = Environment(app)

js = Bundle('js/vendor/jquery_3.2.1.js', 'js/vendor/popper_1.11.0.js', 'js/vendor/bootstrap_4.1.1.js',
            filters='jsmin', output='gen/packed.%(version)s.js')

css = Bundle('css/vendor/bootstrap_4.1.1.css', 'css/style.css',
             filters='cssmin', output='gen/packed.%(version)s.css')

assets.register({'js_all': js, 'css_all': css})
