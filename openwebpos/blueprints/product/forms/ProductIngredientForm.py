from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired

from openwebpos.utils.wtforms import CustomSubmitField, MoneyField
from ..models import Ingredient


class ProductIngredientForm(FlaskForm):
    ingredient_id = SelectField("Ingredient", coerce=str, validators=[DataRequired()])
    price = MoneyField("Price")
    submit = CustomSubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(ProductIngredientForm, self).__init__(*args, **kwargs)
        self.ingredient_id.choices = [
            (i.id, i.name) for i in Ingredient.query.filter_by(active=True).all()
        ]
