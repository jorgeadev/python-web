from flask import Blueprint
from flask import render_template, request
from .forms import LoginForm

page = Blueprint("page", __name__)


@page.app_errorhandler(404)
def page_not_found(error):
	return render_template('errors/404.html'), 404


@page.route("/")
def index():
	return render_template("index.html", title = "Nuevo titulo de la pagina de Jorge")


@page.route("/login", methods = ['GET', 'POST'])
def login():
	form = LoginForm(request.form)

	if (request.method == 'POST') and (form.validate()):
		print(form.username.data)
		print(form.password.data)
		print("Nueva sesión creada")

	return render_template("auth/login.html", title = "Login", form = form)