from omni_marketplace.marketplaces.model import Marketplace, db
from flask import redirect, url_for, render_template, Blueprint, flash, request
from flask_login import login_user, current_user, login_required, logout_user


marketplaces_blueprint = Blueprint(
    'marketplaces', __name__, template_folder='templates')


@marketplaces_blueprint.route('/authorize/lazada')
@login_required
def lazada_authorize_login():
    pass
