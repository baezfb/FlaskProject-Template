from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired


class CustomStringField(StringField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.render_kw = {"placeholder": " "}


class CustomSubmitField(SubmitField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.render_kw = {"class": "btn-full"}


class MoneyField(FloatField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators = [DataRequired()]
        self.render_kw = {
            "type": "number",
            "step": 0.01,
            "min": 0,
            "placeholder": " ",
        }
