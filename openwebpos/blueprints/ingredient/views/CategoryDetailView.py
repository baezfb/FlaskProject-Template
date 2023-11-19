from openwebpos.app.views import DetailView
from ..forms.CategoryTypeForm import CategoryTypeForm
from ..models import IngredientCategoryType, IngredientCategory


class CategoryDetailView(DetailView):
    template_name = "ingredient/category_detail.html"
    model = IngredientCategoryType
    query_model = IngredientCategory
    form = CategoryTypeForm
    query_field = "slug"
    back_url = "ingredient.categories"

    def get_context(self):
        ing_cat = IngredientCategory.get_by("slug", self.kwargs[self.url_variable])
        return {
            "title": ing_cat.name.title() + " Details",
            "nav_title": ing_cat.name.title(),
        }
