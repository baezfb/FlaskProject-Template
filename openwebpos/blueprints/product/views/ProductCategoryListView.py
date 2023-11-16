from flask import url_for, request

from openwebpos.app.views import ListView
from openwebpos.utils.htmx import htmx_refresh
from ..forms.ProductCategoryForm import ProductCategoryForm
from ..models import ProductCategory


class ProductCategoryListView(ListView):
    template_name = "product/product_category_list.html"
    title = "Product Categories"
    nav_title = "Categories"
    model = ProductCategory
    form = ProductCategoryForm

    def post(self):
        form = self.form()
        if form.validate_on_submit():
            self.model.create(name=form.name.data)
        return self.redirect(url_for("product.categories"))

    def put(self):
        form = self.form()
        if form.validate_on_submit():
            self.model.get_by_id(request.form.get("id")).update(
                name=form.name.data,
                active=form.active.data,
            )
        return htmx_refresh()

    def delete(self):
        self.model.get_by_id(request.form.get("id")).delete()
        return htmx_refresh()
