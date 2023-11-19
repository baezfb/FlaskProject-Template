from flask import Blueprint

from .views.ProductCategoryDetailView import ProductCategoryDetailView
from .views.ProductCategoryListView import ProductCategoryListView
from .views.ProductIngredientDetailView import ProductIngredientDetailView
from .views.ProductVariantDetailView import ProductVariantDetailView

product_bp = Blueprint(
    "product", __name__, template_folder="templates", url_prefix="/product/"
)

ProductCategoryListView.register(product_bp, "categories", "categories")
ProductCategoryDetailView.register(product_bp, "category/<id>", "category")
ProductIngredientDetailView.register(product_bp, "<id>/ingredient", "ingredients")
ProductVariantDetailView.register(product_bp, "<id>/variants", "variants")
