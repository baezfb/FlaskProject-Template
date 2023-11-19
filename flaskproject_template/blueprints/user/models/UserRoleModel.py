from flaskproject_template.app.extensions import db
from flaskproject_template.utils.sqlalchemy import Model


class UserRole(Model):
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, default=True)

    users = db.relationship("UserModel", backref="role", lazy=True)

    def __init__(self, **kwargs):
        super(UserRole, self).__init__(**kwargs)
