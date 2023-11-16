from flask import url_for, request

from openwebpos.app.views import DetailView
from openwebpos.utils.htmx import htmx_refresh
from ..forms.ProductIngredientForm import ProductIngredientForm
from ..models import Product, ProductIngredient


class ProductIngredientDetailView(DetailView):
    template_name = "product/product_ingredient_detail.html"
    title = "Product Ingredients"
    nav_title = "Ingredients"
    model = Product
    product_ingredient_model = ProductIngredient
    form = ProductIngredientForm
    back_url_dynamic = True

    def get_context(self):
        return {
            "back_url": url_for("product.category", id=self.object.category_id),
        }

    def post(self):
        form = self.form()
        if form.validate_on_submit():
            self.product_ingredient_model.create(
                product_id=self.object.id,
                ingredient_id=form.ingredient_id.data,
                price=form.price.data,
            )
        return self.redirect(url_for("product.product_ingredients", id=self.object.id))

    def put(self):
        return htmx_refresh()

    def delete(self):
        self.product_ingredient_model.get_by_id(request.form.get("id")).delete()
        return htmx_refresh()
