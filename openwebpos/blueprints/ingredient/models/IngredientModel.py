from openwebpos.app.extensions import db
from openwebpos.utils.sqlalchemy import Model, foreign_key
from openwebpos.utils import slugify_string


class Ingredient(Model):
    # Foreign Key
    category_id = foreign_key("ingredient_category_type")

    # Columns
    name = db.Column(db.String(30), unique=True, nullable=False)
    slug = db.Column(db.String(30), unique=True, nullable=False)

    def __init__(self, **kwargs):
        super(Ingredient, self).__init__(**kwargs)
        self.slug = slugify_string(self.name.lower())
