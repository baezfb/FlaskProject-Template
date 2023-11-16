from openwebpos.app.extensions import db
from openwebpos.utils.sqlalchemy import Model


class IngredientCategory(Model):
    name = db.Column(db.String(24), nullable=False, unique=True)
    active = db.Column(db.Boolean, nullable=False, default=True)

    # Relationships
    ingredients = db.relationship("Ingredient", backref="category", lazy=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name").lower()
