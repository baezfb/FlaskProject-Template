from flask import url_for, request

from openwebpos.app.views import DetailView
from openwebpos.utils.htmx import htmx_refresh
from openwebpos.utils.money import convert_to_cents
from ..forms.ProductForm import ProductForm
from ..models import ProductCategory, Product


class ProductCategoryDetailView(DetailView):
    template_name = "product/product_category_detail.html"
    title = "Product Category Detail"
    nav_title = "Category Detail"
    model = ProductCategory
    product_model = Product
    form = ProductForm
    back_url = "product.categories"

    def get_context(self):
        return {"nav_title": self.object.name.title()}

    def post(self, id):
        form = self.form()
        if form.validate_on_submit():
            self.product_model.create(
                category_id=id,
                name=form.name.data,
                short_name=form.short_name.data,
                description=form.description.data,
                price=form.price.data,
            )
        return self.redirect(url_for("product.category", id=id))

    def put(self, id):
        form = self.form()
        if form.validate_on_submit():
            self.product_model.get_by_id(request.form.get("id")).update(
                name=form.name.data,
                short_name=form.short_name.data,
                description=form.description.data,
                price=convert_to_cents(float(form.price.data)),
                active=form.active.data,
            )
        return htmx_refresh()

    def delete(self, id):
        self.product_model.get_by_id(request.form.get("id")).delete()
        return htmx_refresh()
