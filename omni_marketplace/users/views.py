from flask import Blueprint, render_template, request, redirect, url_for, flash, escape, sessions
from omni_marketplace.users.forms import SignupForm
from omni_marketplace.users.model import User
from flask_login import login_user, logout_user, login_required, login_url, current_user
from omni_marketplace import db

users_blueprint = Blueprint(
    'users', __name__, template_folder='templates/')


@users_blueprint.route("/new", methods=['GET'])
def new():
    if current_user.is_authenticated:
        flash('You are logged in!!')
        return redirect(url_for('home'))
    else:
        form = SignupForm()
        return render_template('users/new.html', form=form)


@users_blueprint.route("/create", methods=['POST'])
def create():
    form = SignupForm()
    if form.validate_on_submit():
        new_user = User(form.email.data.lower(), form.first_name.data, form.last_name.data,
                        form.store_name.data, form.password.data)
        if len(new_user.validation_errors) == 0:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            # send_signup_email(new_user.email)
            flash('Account created successfully')
            return redirect(url_for('home', id=current_user.id))
        return render_template('users/new.html', form=form, validation_errors=new_user.validation_errors)
    return render_template('users/new.html', form=form)
