from flask import Blueprint

from .views.CategoryListView import CategoryListView
from .views.CategoryDetailView import CategoryDetailView

ingredient_bp = Blueprint(
    "ingredient", __name__, template_folder="templates", url_prefix="/ingredient/"
)


CategoryListView.register(ingredient_bp, "categories", "categories")
CategoryDetailView.register(ingredient_bp, "category/<var>", "category")
