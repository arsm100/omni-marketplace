from omni_marketplace.marketplaces.model import Marketplace, db
from flask import redirect, url_for, render_template, Blueprint, flash, request
from flask_login import current_user, login_required
from omni_marketplace.helpers.lazada_sdk.lazop.base import LazopClient, LazopRequest, LazopResponse
from omni_marketplace import LAZADA_TEST_KEY, LAZADA_TEST_SECRET, LAZADA_REDIRECT_URI, lazada, oauth

marketplaces_blueprint = Blueprint(
    'marketplaces', __name__, template_folder='templates')

# url = "https://api.lazada.com.my/rest"

# client = LazopClient(url, LAZADA_TEST_KEY, LAZADA_TEST_SECRET)
# request = LazopRequest('/brands/get', 'GET')
# request.add_api_param('offset', '0')
# request.add_api_param('limit', '5')
# response = client.execute(request)
# print(response.type)
# print(response.body)

@marketplaces_blueprint.route('/check/lazada')
@login_required
def lazada_authorize():
    return lazada.authorize_redirect(LAZADA_REDIRECT_URI, _external= True)


@marketplaces_blueprint.route('/authorize/lazada')
def lazada_authorize_login():
    code = request.args.get('code')
    client = LazopClient("https://auth.lazada.com/rest", LAZADA_TEST_KEY, LAZADA_TEST_SECRET)
    api_request = LazopRequest("/auth/token/create")
    api_request.add_api_param("code", code)
    response = client.execute(api_request)
    access_token = response.body.get('access_token')
    refresh_token = response.body.get('refresh_token')
    email = response.body.get('account')
    seller_id = response.body.get('country_user_info')[0].get('seller_id')
    print(response)
    print(response.type)
    print(response.body)
    import pdb; pdb.set_trace()
    return redirect(url_for('home', lazada=True))  # change redirect destination later
