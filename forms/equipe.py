from flask_wtf import FlaskForm
from wtforms import SubmitField


class EquipeForm(FlaskForm):
    # TODO (parte 2): campos nome, trilha_id e descricao + validacao de nome repetido
    enviar = SubmitField("Criar equipe")
