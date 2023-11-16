from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms.validators import DataRequired, Length

from openwebpos.utils.wtforms import CustomStringField, CustomSubmitField


class IngredientCategoryForm(FlaskForm):
    name = CustomStringField(
        "Name",
        validators=[
            DataRequired(message="Name is required."),
            Length(min=1, max=24, message="Name must be between 1 and 24 characters."),
        ],
    )
    active = BooleanField("Active")
    submit = CustomSubmitField("Save")
