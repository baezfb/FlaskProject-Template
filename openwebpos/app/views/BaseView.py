from flask import redirect
from flask.views import MethodView

from openwebpos.utils import convert_camel_to_snake


class BaseView(MethodView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = None
        self.kwargs = None

    @classmethod
    def register(cls, blueprint, route, name=None):
        if name is None:
            # Convert 'ViewName' to 'view_name' and use it
            name = convert_camel_to_snake().sub(r"_\1", cls.__name__).lower()
        blueprint.add_url_rule(route, view_func=cls.as_view(name))

    def dispatch_request(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        result = self.dispatch()
        if result is None:
            return super().dispatch_request(**kwargs)
        return result

    def dispatch(self) -> object:
        """
        Hook for the actual dispatching of a request.
        """
        pass

    def redirect(self, location, code=302):
        """
        Redirects the user to the specified URL.

        :param location: The URL to redirect to.
        :param code: The HTTP status code to use for the redirect (default is 302).

        :return: A redirect response to the specified URL.
        """
        return redirect(location, code)
