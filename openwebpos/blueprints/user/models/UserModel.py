from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from openwebpos.app.extensions import db
from openwebpos.utils.sqlalchemy import Model, foreign_key
from .UserRoleModel import UserRole


class User(Model, UserMixin):
    # Foreign Keys
    role_id = foreign_key("user_role")

    # Fields
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, default=True)

    # Relationships
    profile = db.relationship(
        "UserProfile",
        backref="user",
        lazy=True,
        uselist=False,
        cascade="all, delete-orphan",
    )
    activity = db.relationship(
        "UserActivity",
        backref="user",
        lazy=True,
        uselist=False,
        cascade="all, delete-orphan",
    )

    def verify_password(self, password):
        """
        Verifies the given password against the stored password hash for the user.

        Parameters:
            password (str): The password to be checked.

        Returns:
            bool: True if the password matches the stored password hash, False otherwise.

        """
        return check_password_hash(self.password, password)

    def has_role(self, role) -> bool:
        """
        Check if the user has a specific role.

        Parameters:
            role (str): The name of the role to check.

        Returns:
            bool: True if the user has the specified role, False otherwise.

        Example Usage:
            # Check if the current user has the 'admin' role
            current_user.has_role('admin')
        """
        return self.role.name == role.lower()

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = generate_password_hash(self.password)
        if self.role_id is None:
            self.role_id = UserRole.get_by_name("user").id
