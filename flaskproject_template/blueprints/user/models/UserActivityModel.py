from flask_login import current_user

from flaskproject_template.app.extensions import db
from flaskproject_template.utils import timezone_datetime
from flaskproject_template.utils.sqlalchemy import Model, foreign_key


class UserActivity(Model):
    user_id = foreign_key("user")
    sign_in_count = db.Column(db.Integer, nullable=False, default=0)
    current_sign_in_at = db.Column(db.DateTime, nullable=True)
    current_sign_in_ip = db.Column(db.String(100), nullable=True)
    last_sign_in_at = db.Column(db.DateTime, nullable=True, default=None)
    last_sign_in_ip = db.Column(db.String(100), nullable=True, default=None)
    user_agent = db.Column(db.String(120))
    referrer = db.Column(db.String(120))

    def __init__(self, **kwargs):
        super(UserActivity, self).__init__(**kwargs)

    def update_activity(self, user_agent: str, referrer: str, ip_address: str):
        """
        Update the user activity.
        """
        self.user_id = current_user.id
        self.user_agent = user_agent
        self.referrer = referrer
        self.last_sign_in_at = self.current_sign_in_at
        self.last_sign_in_ip = self.current_sign_in_ip
        self.current_sign_in_at = timezone_datetime()
        self.current_sign_in_ip = ip_address
        if self.sign_in_count is None:
            self.sign_in_count = 0
        else:
            self.sign_in_count += 1

        return self.update()
