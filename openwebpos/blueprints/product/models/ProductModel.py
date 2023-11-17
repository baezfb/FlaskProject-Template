from openwebpos.app.extensions import db
from openwebpos.utils.money import convert_to_cents
from openwebpos.utils.sqlalchemy import Model, foreign_key


class Product(Model):
    # Foreign Keys
    category_id = foreign_key("product_category")

    # Columns
    name = db.Column(db.String(24), nullable=False, unique=True)
    short_name = db.Column(db.String(12), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True, unique=False)
    price = db.Column(db.Integer, nullable=False, unique=False, default=0)
    active = db.Column(db.Boolean, nullable=False, default=True)

    # Relationships
    ingredients = db.relationship("ProductIngredient", back_populates="product")
    variants = db.relationship("ProductVariant", backref="product")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name").lower()
        self.short_name = kwargs.get("short_name").lower()
        self.description = kwargs.get("description").lower()
        self.price = convert_to_cents(kwargs.get("price"))
