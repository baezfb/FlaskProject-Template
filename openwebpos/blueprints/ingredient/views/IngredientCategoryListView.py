from flask import url_for, request

from openwebpos.app.views import ListView
from openwebpos.utils.htmx import htmx_refresh
from ..models import IngredientCategory


class IngredientCategoryListView(ListView):
    template_name = "ingredient/category_list.html"
    title = "Ingredient Categories"
    nav_title = "Categories"
    model = IngredientCategory
