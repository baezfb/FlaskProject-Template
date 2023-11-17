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
            "form": self.form(product_id=self.object.id),
            "back_url": url_for("product.category", id=self.object.category_id),
            "product_ingredients": self.product_ingredient_model.query.filter_by(
                product_id=self.object.id
            ).all(),
        }

    def post(self, id):
        form = self.form()
        if form.validate_on_submit():
            self.product_ingredient_model.create(
                product_id=self.object.id,
                ingredient_id=form.ingredient_id.data,
                amount=form.amount.data,
                unit=form.unit.data,
            )
        else:
            print(form.errors)
        return self.redirect(url_for("product.ingredients", id=id))

    def delete(self, id):
        self.product_ingredient_model.get_by_id(request.form.get("id")).delete()
        return htmx_refresh()
