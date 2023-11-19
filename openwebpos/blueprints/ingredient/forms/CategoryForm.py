from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms.validators import DataRequired, Length

from openwebpos.utils.wtforms import CustomStringField, CustomSubmitField


class CategoryForm(FlaskForm):
    name = CustomStringField("Name", validators=[DataRequired(), Length(min=4, max=24)])
    active = BooleanField("Active")
    submit = CustomSubmitField("Submit")
