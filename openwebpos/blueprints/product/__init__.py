from flask import Blueprint

product_bp = Blueprint('product', __name__, template_folder='templates', url_prefix='/product/')
