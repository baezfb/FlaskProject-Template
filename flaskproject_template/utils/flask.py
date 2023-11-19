import inspect

from flask import render_template


def template(context=None, sub_dir=None):
    """
    Render a template from the current blueprint.

    Will look for a template with the same name as the calling function.
    Will look for a template folder with the same name as the calling blueprint.
    Args:
        context: context to pass to the template.
        sub_dir: subdirectory to look for the template file.
            -If not provided, will look for the template in the current
            blueprint folder.

    Examples:
        * return template() - looks for the template with the same name as te calling function
        * return template(context) - same as above but with context
        * return template(context, sub_dir='settings') - looks for the template in the sub_dir folder
        - -(templates/settings/function_name.html)
        - -(templates/admin/settings/function_name.html) if on admin blueprint

    Returns:
        Flask render_template function.
    """
    if context is None:
        context = {}
    bp_name = inspect.stack()[1][3] + ".html"
    bp_temp_dir = inspect.stack()[1][1].split("/")[-2].split(".")[0] + "/"
    _template = bp_temp_dir + bp_name
    if sub_dir:
        _template = f"{bp_temp_dir}{sub_dir}{bp_name}"
    return render_template(_template, **context)
