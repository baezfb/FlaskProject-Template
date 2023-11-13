from openwebpos.app.extensions import db
from openwebpos.utils.sqlalchemy import Model, foreign_key


class UserProfile(Model):
    """
    User profile model.
    """

    # Foreign Keys
    user_id = foreign_key("user")

    # Fields
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=False)
    zip_code = db.Column(db.String(80), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

    def __init__(self, **kwargs):
        super(UserProfile, self).__init__(**kwargs)
