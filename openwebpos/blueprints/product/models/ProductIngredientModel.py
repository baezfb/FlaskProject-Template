from openwebpos.app.extensions import db
from openwebpos.utils.money import convert_to_cents
from openwebpos.utils.sqlalchemy import Model, foreign_key


class ProductIngredient(Model):
    product_id = db.Column(db.String(255), db.ForeignKey("product.id"))
    ingredient_id = db.Column(db.String(255), db.ForeignKey("ingredient.id"))

    # Columns
    amount = db.Column(db.Integer, nullable=False, unique=False, default=0)
    unit = db.Column(db.String(12), nullable=False, unique=False)

    product = db.relationship("Product", back_populates="ingredients")
    ingredient = db.relationship("Ingredient", back_populates="products")

    def __init__(self, **kwargs):
        super(ProductIngredient, self).__init__(**kwargs)
