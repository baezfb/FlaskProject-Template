from openwebpos.app.extensions import db
from openwebpos.utils.money import convert_to_cents
from openwebpos.utils.sqlalchemy import Model, foreign_key


class ProductVariant(Model):
    product_id = foreign_key("product")

    name = db.Column(db.String(24), nullable=False, unique=False)
    short_name = db.Column(db.String(24), nullable=False, unique=False)
    price = db.Column(db.Integer, nullable=False, unique=False, default=0)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name").lower()
        self.short_name = kwargs.get("short_name").lower()
        self.price = convert_to_cents(kwargs.get("price"))
