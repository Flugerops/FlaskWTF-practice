from flask_wtf import Form
from wtforms import StringField, SubmitField, ValidationError, PasswordField
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Length,
    NumberRange,
    URL,
    Email,
    ReadOnly,
    Optional,
    InputRequired
    
)



class PasswordForm(Form):
    text = PasswordField(
        "Enter the Password",
        validators=[
            DataRequired("This is required field)"),
            EqualTo("subtext", "Must be equal"),
            Length(min=5, max=30)
        ]
    )
    subtext = PasswordField("Enter again please")
    submit = SubmitField("Finish")