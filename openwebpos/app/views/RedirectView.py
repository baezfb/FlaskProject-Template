from .BaseView import BaseView


class RedirectView(BaseView):
    url = None

    def get_url(self):
        """
        Gets the URL, if this method is not overwritten, then a url variable must be set.
        """
        if self.url is None:
            # TODO: Raised adn error message if url is not set.
            pass
        return self.url

    def get(self, *args, **kwargs):
        return self.redirect(self.get_url())
