import re
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from omni_marketplace import db
from omni_marketplace.helpers.helpers import validation_preparation
import re


class Marketplace(db.Model):
    __tablename__ = 'marketplaces'

    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, nullable=False)
    shop_name = db.Column(db.String(64), index=True, nullable=False)
    shop_description = db.Column(db.Text)
    shop_logo = db.Column(db.String())

    def __init__(self, shop_id, shop_name):
        self.shop_id = shop_id
        self.shop_name = shop_name

    def __repr__(self):
        return f"{self.shop_name} with id {self.shop_id} saved to database!"
