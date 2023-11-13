from .TemplateView import TemplateView


class DetailView(TemplateView):
    """
    A view that will display details in a template for a single object.
    """

    init_every_request = False

    model = None
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
        return self.model.query.get_or_404(self.kwargs["id"])

    def get_default_context(self):
        """
        Add the object to the context.
        """
        context = super().get_default_context()
        context[self.get_context_object_name()] = self.get_object()
        return context

    def get(self, *args, **kwargs):
        """
        Set the object to an instance variable, then process as normal.
        """
        self.object = self.get_object()
        return super().get(*args, **kwargs)
