from flask import url_for, request

from openwebpos.app.views import DetailView
from openwebpos.utils.htmx import htmx_refresh
from openwebpos.utils.money import convert_to_cents
from ..forms.ProductVariantForm import ProductVariantForm
from ..models import ProductVariant, Product


class ProductVariantDetailView(DetailView):
    template_name = "product/product_variant_detail.html"
    model = Product
    product_variant_model = ProductVariant
    form = ProductVariantForm
    back_url_dynamic = True

    def get_context(self):
        return {
            "title": f"{self.object.name.title()} Variants",
            "nav_title": f"{self.object.name.title()} Variants",
            "back_url": url_for("product.category", id=self.object.category_id),
        }

    def post(self, id):
        form = self.form()
        if form.validate_on_submit():
            self.product_variant_model.create(
                product_id=id,
                name=form.name.data,
                short_name=form.short_name.data,
                price=form.price.data,
            )
        return self.redirect(url_for("product.variants", id=id))

    def put(self, id):
        form = self.form()
        if form.validate_on_submit():
            self.product_variant_model.get_by_id(request.form.get("variant_id")).update(
                name=form.name.data,
                short_name=form.short_name.data,
                price=convert_to_cents(float(form.price.data)),
                active=form.active.data,
            )
        return htmx_refresh()

    def delete(self, id):
        self.product_variant_model.get_by_id(request.form.get("id")).delete()
        return htmx_refresh()
