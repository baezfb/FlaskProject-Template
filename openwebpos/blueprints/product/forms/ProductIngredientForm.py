from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired, InputRequired

from openwebpos.utils.wtforms import CustomStringField, CustomSubmitField, MoneyField
from ..models import Ingredient, ProductIngredient


class ProductIngredientForm(FlaskForm):
    ingredient_id = SelectField("Ingredient", coerce=str, validators=[DataRequired()])
    amount = CustomStringField("Amount", validators=[DataRequired()])
    unit = SelectField("Unit", coerce=str, validators=[DataRequired()])
    submit = CustomSubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(ProductIngredientForm, self).__init__(*args, **kwargs)
        associated_ingredients = [
            p.ingredient_id
            for p in ProductIngredient.query.filter_by(
                product_id=kwargs.get("product_id")
            )
        ]
        active_ingredients = Ingredient.query.filter_by(active=True).all()
        active_not_associated = [
            i for i in active_ingredients if i.id not in associated_ingredients
        ]
        self.ingredient_id.choices = [(c.id, c.name) for c in active_not_associated]
        # self.ingredient_id.choices = [
        #     (i.id, i.name) for i in Ingredient.query.filter_by(active=True).all()
        # ]
        self.unit.choices = [
            ("oz", "oz"),
            ("lb", "lb"),
            ("g", "g"),
            ("ml", "ml"),
            ("each", "each"),
        ]
