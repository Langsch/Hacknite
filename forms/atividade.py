from flask_wtf import FlaskForm
from wtforms import SubmitField


class AtividadeForm(FlaskForm):
    # TODO (parte 3): campos dia, horario, titulo, local e descricao
    enviar = SubmitField("Salvar")
