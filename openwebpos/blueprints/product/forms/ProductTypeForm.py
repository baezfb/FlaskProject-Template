from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class ProductTypeForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[DataRequired(), Length(min=4, max=24)],
        render_kw={"placeholder": " "},
    )
    short_name = StringField(
        "Short Name",
        validators=[DataRequired(), Length(min=1, max=12)],
        render_kw={"placeholder": " "},
    )
    active = BooleanField("Active")
    submit = SubmitField("Submit", render_kw={"class": "btn-full"})


class ProductTypeEditForm(ProductTypeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.submit.label.text = "Update"
