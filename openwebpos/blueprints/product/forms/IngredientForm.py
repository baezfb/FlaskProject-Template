from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms.validators import DataRequired

from openwebpos.utils.wtforms import CustomStringField, CustomSubmitField


class IngredientForm(FlaskForm):
    name = CustomStringField("Name", validators=[DataRequired()])
    active = BooleanField("Active")
    submit = CustomSubmitField("Save")
