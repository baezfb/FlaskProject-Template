from flask import url_for, request

from openwebpos.app.views import DetailView
from openwebpos.utils.htmx import htmx_refresh
from ..models import IngredientCategory


class IngredientCategoryDetailView(DetailView):
    template_name = "ingredient/category_detail.html"
    model = IngredientCategory
    query_field = "slug"
    back_url = "ingredient.categories"
