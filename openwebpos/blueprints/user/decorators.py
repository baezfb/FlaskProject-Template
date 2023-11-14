from functools import wraps

from flask import redirect, url_for
from flask_login import current_user


def has_required_role(required_roles):
    """Check if the current user has one of the required roles.

    Args:
        required_roles: Roles required to access.

    Returns:
        bool: True if user has a role in required_roles, False otherwise.
    """
    logged_in = current_user.is_authenticated
    if not logged_in:
        return False
    return current_user.role.name in required_roles


def role_required(*required_roles):
    """Decorator to check if the current user has one of the required roles.

    Args:
        required_roles: Roles required to access.

    Returns:
        Decorator function.
    """

    def decorator(f):
        @wraps(f)
        def wrapped_function(*args, **kwargs):
            if not has_required_role(required_roles):
                return redirect(url_for("user.login"))
            return f(*args, **kwargs)

        return wrapped_function

    return decorator
