from flask import Blueprint

from .views.ProductTypeListView import ProductTypeListView

product_bp = Blueprint(
    "product", __name__, template_folder="templates", url_prefix="/product/"
)

ProductTypeListView.register(product_bp, "types", "types")
