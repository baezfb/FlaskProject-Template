from flask import url_for, request

from openwebpos.app.views import ListView
from openwebpos.utils.htmx import htmx_refresh
from ..forms.ProductTypeForm import ProductTypeForm, ProductTypeEditForm
from ..models.ProductTypeModel import ProductType


class ProductTypeListView(ListView):
    # decorators = [role_required("admin")]
    template_name = "product/product_type_list.html"
    title = "Product Types"
    nav_title = "Product Types"
    model = ProductType
    form = ProductTypeForm

    def get_context(self, **kwargs):
        return {
            "edit_form": ProductTypeEditForm(),
        }

    def post(self):
        form = self.form()
        if form.validate_on_submit():
            self.model.create(name=form.name.data, short_name=form.short_name.data)
        return self.redirect(url_for("product.types"))

    def put(self):
        form = self.form()
        if form.validate_on_submit():
            self.model.get_by_id(request.form.get("id")).update(
                name=form.name.data,
                short_name=form.short_name.data,
                active=form.active.data,
            )
        return htmx_refresh()

    def delete(self):
        self.model.get_by_id(request.form.get("id")).delete()
        return htmx_refresh()
