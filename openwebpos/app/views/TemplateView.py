from flask import render_template, url_for, request

from .BaseView import BaseView
from ...utils import remove_csrf_and_submit
from ...utils.htmx import htmx_refresh


class TemplateView(BaseView):
    template_name = None
    title = None
    nav_title = None
    back_url = None
    user_sidenav = True
    alt_sidenav = False
    back_url_dynamic = False
    form = None
    model = None

    def get_default_context(self):
        context = {
            "title": self.title,
            "nav_title": self.nav_title,
            "back_url": None
            if self.back_url is None
            else lambda: url_for(self.back_url),
            "user_sidenav": self.user_sidenav,
            "alt_sidenav": self.alt_sidenav,
            "form": self.form() if self.form is not None else None,
        }
        context.update(self.get_context())
        return context

    @staticmethod
    def get_context():
        return {}

    def get(self, *args, **kwargs):
        context = self.get_default_context()
        # Using a lambda function to get url_for value:
        if self.back_url_dynamic is False:
            if context["back_url"] is not None:
                context["back_url"] = context["back_url"]()
        return render_template(self.template_name, **context)

    def post(self, *args, **kwargs):
        if self.form().validate_on_submit():
            cleaned_data = remove_csrf_and_submit(self.form())
            if self.model:
                self.model.create(**cleaned_data)
                return self.redirect(url_for(request.endpoint, **request.view_args))
            else:
                raise NotImplementedError("model must be defined")
        else:
            # TODO: Add error handling here to display errors on page instead of console log and log to file
            print("form not validated")
            print(self.form().errors)
            return self.get()

    def put(self, *args, **kwargs):
        if self.model:
            cleaned_data = remove_csrf_and_submit(self.form())
            self.model.get_by_id(request.form.get("id")).update(**cleaned_data)
            return htmx_refresh()
        else:
            raise NotImplementedError("model must be defined")

    def delete(self, *args, **kwargs):
        if self.model:
            self.model.get_by_id(request.form.get("id")).delete()
            return htmx_refresh()
        else:
            raise NotImplementedError("model must be defined")
