from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms.validators import DataRequired, Length

from openwebpos.utils.wtforms import CustomStringField, MoneyField, CustomSubmitField


class ProductVariantForm(FlaskForm):
    name = CustomStringField("Name", validators=[DataRequired(), Length(min=4, max=24)])
    short_name = CustomStringField(
        "Short Name", validators=[DataRequired(), Length(min=1, max=12)]
    )
    price = MoneyField("Price")
    active = BooleanField("Active")
    submit = CustomSubmitField("Submit")
