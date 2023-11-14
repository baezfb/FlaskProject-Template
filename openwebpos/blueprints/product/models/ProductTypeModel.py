from openwebpos.app.extensions import db
from openwebpos.utils.sqlalchemy import Model


class ProductType(Model):
    name = db.Column(db.String(24), nullable=False, unique=True)
    short_name = db.Column(db.String(12), nullable=False, unique=True)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name").lower()
        self.short_name = kwargs.get("short_name").lower()
