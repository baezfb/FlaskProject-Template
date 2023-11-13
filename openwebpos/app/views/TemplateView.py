from flask import render_template, url_for

from .BaseView import BaseView


class TemplateView(BaseView):
    template_name = None
    title = None
    nav_title = None
    back_url = None
    user_sidenav = True
    alt_sidenav = False
    back_url_dynamic = False
    form = None

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
