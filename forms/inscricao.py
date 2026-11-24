from flask_wtf import FlaskForm
from wtforms import SubmitField


class InscricaoForm(FlaskForm):
    # TODO (parte 1): campos nome, email, curso, instituicao, nivel, equipe_id e aceite
    #                 + validacao de e-mail repetido e de equipe lotada
    enviar = SubmitField("Confirmar inscrição")
