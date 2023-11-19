from openwebpos.app.views import ListView
from ..forms.CategoryForm import CategoryForm
from ..models import IngredientCategory


class IngredientCategoryListView(ListView):
    template_name = "ingredient/category_list.html"
    title = "Ingredient Categories"
    nav_title = "Categories"
    model = IngredientCategory
    form = CategoryForm
