from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms import validators

class LoginForm(Form):
	username = StringField("Username", [
		validators.length(min=4, max=50, message = "El username esta fuera de rango")
		])
	password = PasswordField("Password", [
		validators.Required()
		])