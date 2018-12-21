from omni_marketplace.marketplaces.model import Marketplace, db
from flask import redirect, url_for, render_template, Blueprint, flash, request
from flask_login import current_user, login_required
from omni_marketplace.helpers.lazada_sdk.lazop.base import LazopClient, LazopRequest, LazopResponse
from omni_marketplace import LAZADA_TEST_KEY, LAZADA_TEST_SECRET

marketplaces_blueprint = Blueprint(
    'marketplaces', __name__, template_folder='templates')

url = "https://api.lazada.com.my/rest"

client = LazopClient(url, LAZADA_TEST_KEY, LAZADA_TEST_SECRET)
request = LazopRequest('/brands/get', 'GET')
request.add_api_param('offset', '0')
request.add_api_param('limit', '5')
response = client.execute(request)
# print(response.type)
print(response.body)

@marketplaces_blueprint.route('/authorize/lazada')
@login_required
def lazada_authorize_login():
    print("callback success")
