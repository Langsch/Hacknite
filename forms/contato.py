from flask_wtf import FlaskForm
from wtforms import SubmitField


class ContatoForm(FlaskForm):
    # TODO (parte 4): campos nome, email, assunto e texto
    enviar = SubmitField("Enviar mensagem")
