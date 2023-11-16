from openwebpos.app.extensions import db
from openwebpos.utils.sqlalchemy import Model


class ProductCategory(Model):
    name = db.Column(db.String(24), nullable=False, unique=True)
    active = db.Column(db.Boolean, nullable=False, default=True)

    # Relationships
    products = db.relationship("Product", backref="product_category", lazy=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name").lower()
