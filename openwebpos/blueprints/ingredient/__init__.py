from flask import Blueprint

from .views.IngredientCategoryListView import IngredientCategoryListView
from .views.IngredientCategoryDetailView import IngredientCategoryDetailView

ingredient_bp = Blueprint(
    "ingredient", __name__, template_folder="templates", url_prefix="/ingredient/"
)


IngredientCategoryListView.register(ingredient_bp, "categories", "categories")
IngredientCategoryDetailView.register(ingredient_bp, "category/<var>", "category")
