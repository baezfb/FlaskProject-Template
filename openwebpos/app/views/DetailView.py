from .TemplateView import TemplateView


class DetailView(TemplateView):
    """
    A view that will display details in a template for a single object.
    """

    init_every_request = False

    url_variable = "var"  # Used to get the object from the URL
    query_field = None  # field to query. If none it will query the id field and use url_variable as the id
    context_object_name = "object"

    def get_context_object_name(self):
        """
        Get context_object_name.
        """
        return self.context_object_name

    def get_object(self):
        """
        Get the object. We don't make any assumptions, so this must be
        overwritten by the subclass.
        """
        if self.model is None:
            error = "%s must define `get_object()`"
            raise NotImplementedError(error % self.__class__.__name__)

        if self.query_field:
            return self.model.query.filter_by(
                **{self.query_field: self.kwargs[self.url_variable]}
            ).first_or_404()
        else:
            return self.model.query.get_or_404(self.kwargs[self.url_variable])

        # if self.request_variable == "id":
        #     return self.model.query.get_or_404(self.kwargs[self.request_variable])
        # elif self.request_variable == "slug":
        #     return self.model.query.filter_by(
        #         slug=self.kwargs[self.request_variable]
        #     ).first_or_404()
        # else:
        #     raise NotImplementedError("request_variable must be either 'id' or 'slug'")
        # return self.model.query.get_or_404(self.kwargs[self.request_variable])

    def get_default_context(self):
        """
        Add the object to the context.
        """
        if self.nav_title is None:
            if self.get_object().name:
                self.nav_title = self.get_object().name.title()

        if self.title is None:
            if self.get_object().name:
                self.title = self.get_object().name.title() + " Details"
            else:
                self.title = "Details"

        context = super().get_default_context()
        context[self.get_context_object_name()] = self.get_object()
        return context

    def get(self, *args, **kwargs):
        """
        Set the object to an instance variable, then process as normal.
        """
        self.object = self.get_object()
        return super().get(*args, **kwargs)
