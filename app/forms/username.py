from flask_wtf import Form
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Length,
    NumberRange,
    URL,
    Email,
    ReadOnly,
    Optional,
    InputRequired,
)


class UserNameForm(Form):
    text = StringField(
        "Enter the Username",
        validators=[
            DataRequired("This is required field)"),
            Length(min=5, max=20),
        ],
    )
    
    submit = SubmitField("Continue")



    
