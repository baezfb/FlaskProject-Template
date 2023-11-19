import inspect
import os
import re
import uuid
from datetime import datetime

import pytz
from flask import render_template, current_app
from slugify import slugify


def remove_csrf_and_submit(form):
    form_data = form.data.copy()
    form_data.pop("csrf_token", None)  # Remove CSRF token
    form_data.pop("submit", None)  # Remove submit field
    return form_data


def slugify_string(string: str, length: int = 25) -> str:
    """
    Slugify a string.

    Args:
        string: The string to slugify.

    Returns:
        :param string:
        :param length: The length of the slugified string
    """
    return slugify(
        string, separator="_", max_length=length, word_boundary=True, save_order=True
    )


def write_config_to_file(config: dict, file_path: str = ".env"):
    """
    Write configuration to a file.

    Args:
        config: A dictionary containing configurations.
        file_path: The path to the file where the configurations will be written.

    """
    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode) as f:
        for key, value in config.items():
            f.write(f"{key}={value}\n")


def config_writer(config):
    """
    Write config to .env file.

    Args:
        config: Config to write to file.

    """
    config_file = os.path.join(current_app.config["APP_PATH"], ".env")
    write_config_to_file(config, config_file)


def convert_camel_to_snake():
    """
    Convert camel case to snake case.
    """
    regex = re.compile("((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))")
    camel_to_snake_pattern = regex
    return camel_to_snake_pattern


def timezone_datetime(tz: str = "US/Central"):
    """
    Get the timezone datetime.
    Args:
        tz:  Timezone. Default is US/Central.

    Returns:
        datetime: Timezone datetime.
    """
    timezone = pytz.timezone(tz)
    return datetime.now(timezone)


def get_current_user():
    """
    Get the current user.
    """
    from flask_login import current_user

    return current_user.id


def gen_uuid() -> str:
    """
    Generate a version 5 UUID with a custom DNS namespace.

    Returns:
        str: The generated UUID.
    """
    namespace = uuid.uuid5(uuid.NAMESPACE_DNS, current_app.config["UUID_NAMESPACE"])
    uuid_value = str(uuid.uuid5(namespace, uuid.uuid4().hex))
    return uuid_value


def template(temp_dir, context=None):
    if context is None:
        context = {}
    bp_name = inspect.stack()[1][3] + ".html"
    _template = temp_dir + bp_name
    return render_template(_template, **context)
