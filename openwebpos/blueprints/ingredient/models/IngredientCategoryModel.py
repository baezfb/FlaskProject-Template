from openwebpos.app.extensions import db
from openwebpos.utils.sqlalchemy import Model
from openwebpos.utils import slugify_string


class IngredientCategory(Model):
    # Columns
    name = db.Column(db.String(255), nullable=False, unique=True)
    slug = db.Column(db.String(255), nullable=False, unique=True)
    active = db.Column(db.Boolean, nullable=False, default=True)

    # Relationships
    category_types = db.relationship(
        "IngredientCategoryType", backref="category", lazy=True
    )

    def __init__(self, **kwargs):
        super(IngredientCategory, self).__init__(**kwargs)
        self.slug = slugify_string(self.name.lower())
