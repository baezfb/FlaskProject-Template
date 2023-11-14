from flask import make_response


# https://htmx.org/docs/#requests
# https://htmx.org/docs/#response-headers


def htmx_refresh():
    """
    This function returns a response that will trigger a page reload.

    Returns:
        Response: A response that will trigger a page reload.
    """
    response = make_response()
    response.headers["HX-Refresh"] = "true"
    return response


def htmx_redirect(url):
    """
    This function returns a response that will trigger a redirect.

    Args:
        url (str): The URL to redirect to.

    Returns:
        Response: A response that will trigger a redirect.
    """
    response = make_response()
    response.headers["HX-Redirect"] = url
    return response
