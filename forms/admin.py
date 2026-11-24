from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    senha = PasswordField("Senha", validators=[DataRequired("Informe a senha.")])
    enviar = SubmitField("Entrar")
