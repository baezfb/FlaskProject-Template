from openwebpos.app.extensions import db
from openwebpos.utils.sqlalchemy import Model, foreign_key


class ProductIngredient(Model):
    # Foreign Key
    product_id = foreign_key("product", primary_key=True)
    ingredient_id = foreign_key("ingredient", primary_key=True)

    price = db.Column(db.Integer, default=0, nullable=False)

    def __init__(self, **kwargs):
        super(ProductIngredient, self).__init__(**kwargs)
