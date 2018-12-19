from omni_marketplace import app
from omni_marketplace.users.model import User
from omni_marketplace.sessions.forms import LogInForm
from flask_login import login_user,confirm_login,current_user
from flask import redirect,url_for,request,render_template,sessions,Blueprint,flash
from werkzeug.security import check_password_hash

sessions_blueprint = Blueprint(
    'sessions', __name__, template_folder='templates')

@sessions_blueprint.route('/login')
def index():
    return render_template('sessions/sign_in.html',form=LogInForm())

@sessions_blueprint.route("/login",methods=['POST'])
def attempt_sign_in():
    form = LogInForm()
    user = User.query.filter_by(email = form.email.data.lower()).first()
    
    print(user)
    if user and check_password_hash(user.password_hash , form.password.data):
        login_user(user, remember=False)
        return redirect(url_for('home'))

    else:
        flash('Wrong Email/Password')
        return render_template('sessions/sign_in.html',form=form)
