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
