from flask import url_for, request

from openwebpos.app.views import DetailView
from openwebpos.utils.htmx import htmx_refresh
from ..forms.IngredientForm import IngredientForm
from ..models import IngredientCategory, Ingredient


class IngredientCategoryDetailView(DetailView):
    template_name = "product/ingredient_category_detail.html"
    model = IngredientCategory
    ingredient_model = Ingredient
    form = IngredientForm
    back_url = "product.ingredient_categories"

    def get_context(self):
        obj_name = self.object.name.title()
        return {
            "title": f"{obj_name} Details",
            "nav_title": f"{obj_name}",
        }

    def post(self, id):
        form = self.form()
        if form.validate_on_submit():
            self.ingredient_model.create(category_id=id, name=form.name.data)
        return self.redirect(url_for("product.ingredient_category", id=id))

    def put(self, id):
        form = self.form()
        if form.validate_on_submit():
            self.ingredient_model.get_by_id(request.form.get("id")).update(
                name=form.name.data, active=form.active.data
            )
        return htmx_refresh()

    def delete(self, id):
        self.ingredient_model.get_by_id(request.form.get("id")).delete()
        return htmx_refresh()
