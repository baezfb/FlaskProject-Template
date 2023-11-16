from openwebpos.app.extensions import db
from openwebpos.utils.sqlalchemy import Model, foreign_key


class Ingredient(Model):
    # Foreign Keys
    category_id = foreign_key("ingredient_category")

    # Columns
    name = db.Column(db.String(24), nullable=False, unique=True)
    active = db.Column(db.Boolean, nullable=False, default=True)

    # Relationship
    products = db.relationship(
        "Product", secondary="product_ingredient", back_populates="ingredients"
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name").lower()
