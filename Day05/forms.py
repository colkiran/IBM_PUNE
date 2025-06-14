
from wtforms import Form, StringField, EmailField, validators

class UserForm(Form):
    username = StringField('Username', [validators.length(min=4,max=50)])
    email = EmailField('Email', [validators.Email()])