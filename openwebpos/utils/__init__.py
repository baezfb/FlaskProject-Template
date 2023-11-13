import inspect
import re
import uuid
from datetime import datetime
from os import getenv

import pytz
from flask import render_template


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
    namespace = uuid.uuid5(uuid.NAMESPACE_DNS, getenv("UUID_NAMESPACE"))
    uuid_value = str(uuid.uuid5(namespace, uuid.uuid4().hex))
    return uuid_value


def format_name(name: str, reverse: bool = False):
    """
    Format the name.

    Args:
        name: Name.
        reverse: Reverse the name. Default is False.

    Returns:
        str: Formatted name.
    """
    if reverse:
        name.replace("_", " ")
        return name.capitalize()
    return name.replace(" ", "_").lower()


def format_phone(phone: str):
    """
    Format the phone number.
    (XXX) XXX-XXXX

    Args:
        phone: Phone number.

    Returns:
        str: Formatted phone number.
    """
    if phone:
        return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    return ""


def convert_to_cents(amount: float):
    """
    Convert the amount to cent.

    Args:
        amount: Amount.

    Returns:
        int: Amount in cent.
    """
    return int(amount * 100)


def convert_to_dollar(amount: int):
    """
    Convert the amount to dollar.

    Args:
        amount: Amount.

    Returns:
        float: Amount in dollar.
    """
    return float(amount / 100)


def template(temp_dir, context=None):
    if context is None:
        context = {}
    bp_name = inspect.stack()[1][3] + ".html"
    _template = temp_dir + bp_name
    return render_template(_template, **context)


def template_filters(app):
    """
    Jinja template filters.
    """

    @app.template_filter("format_datetime")
    def format_datetime(value, _format=None):
        if _format is None:
            _format = "%Y-%m-%d %H:%M:%S"
        elif _format == "short-date":
            _format = "%y-%m-%d"
        elif _format == "full-date":
            _format = "%Y-%m-%d"
        elif _format == "time":
            _format = "%I:%M %p"
        elif _format == "time-24":
            _format = "%H:%M"
        else:
            _format = _format

        return value.strftime(_format)

    @app.template_filter("currency")
    def currency(value):
        return "{:,.2f}".format(round(value / 100, 2))

    @app.template_filter("currency_no_decimal")
    def currency_no_decimal(value):
        return "{:,.2f}".format(round(value / 100, 2)).split(".")[0]

    @app.template_filter("currency_only_decimal")
    def currency_only_decimal(value):
        return "{:,.2f}".format(round(value / 100, 2)).split(".")[1]

    @app.template_filter("phone")
    def phone(value):
        return f"({value[:3]}) {value[3:6]}-{value[6:]}"

    @app.template_filter("format_name")
    def format_name_filter(name):
        return name.replace("_", " ").capitalize()
