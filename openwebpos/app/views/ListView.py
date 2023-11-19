from .TemplateView import TemplateView


class ListView(TemplateView):
    """
    A view that will render a template with a list of objects.
    """

    init_every_request = False

    context_object_list_name = "object_list"

    def get_context_object_list_name(self):
        """
        Get context_object_list_name.
        """
        return self.context_object_list_name

    def get_object_list(self):
        """
        Get the list of objects. If this method is not overwritten, then a
        model variable must be declared, and it must have query.all().
        """
        if self.model is None:
            error = "%s must define either `model` or `get_object_list()`"
            raise NotImplementedError(error % self.__class__.__name__)
        return self.model.query.all()

    def get_default_context(self):
        """
        Add the object list to the context.
        """
        context = super().get_default_context()
        context[self.get_context_object_list_name()] = self.get_object_list()
        return context
