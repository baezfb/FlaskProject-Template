from flask_wtf import FlaskForm
from wtforms import BooleanField, HiddenField
from wtforms.validators import DataRequired, Length

from openwebpos.utils.wtforms import CustomStringField, CustomSubmitField


class CategoryTypeForm(FlaskForm):
    category_id = HiddenField("Category ID")
    name = CustomStringField("Name", validators=[DataRequired(), Length(min=4, max=24)])
    active = BooleanField("Active")
    submit = CustomSubmitField("Submit")
