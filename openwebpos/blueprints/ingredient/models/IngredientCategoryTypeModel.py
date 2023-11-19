from openwebpos.app.extensions import db
from openwebpos.utils.sqlalchemy import Model, foreign_key
from openwebpos.utils import slugify_string


class IngredientCategoryType(Model):
    # Foreign Key
    category_id = foreign_key("ingredient_category")

    # Columns
    name = db.Column(db.String(30), unique=True, nullable=False)
    slug = db.Column(db.String(30), unique=True, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)

    # Relationships
    ingredients = db.relationship("Ingredient", backref="category_type", lazy=True)

    def __init__(self, **kwargs):
        super(IngredientCategoryType, self).__init__(**kwargs)
        self.slug = slugify_string(self.name.lower())
