from .BaseView import BaseView


class UrlNotSetException(Exception):
    """
    Custom exception for when a URL is not set.
    """

    pass


class RedirectView(BaseView):
    url = None

    def get_url(self):
        """
        Gets the URL, if this method is not overwritten, then a url variable must be set.
        """
        if self.url is None:
            raise UrlNotSetException("URL is not set.")
        return self.url

    def get(self, *args, **kwargs):
        return self.redirect(self.get_url())
