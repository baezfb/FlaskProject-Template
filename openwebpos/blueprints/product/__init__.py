from flask import Blueprint

from .views.ProductCategoryDetailView import ProductCategoryDetailView
from .views.ProductCategoryListView import ProductCategoryListView
from .views.IngredientCategoryListView import IngredientCategoryListView

product_bp = Blueprint(
    "product", __name__, template_folder="templates", url_prefix="/product/"
)

ProductCategoryListView.register(product_bp, "categories", "categories")
ProductCategoryDetailView.register(product_bp, "category/<id>", "category")
IngredientCategoryListView.register(
    product_bp, "ingredient-categories", "ingredient_categories"
)
