from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional, ValidationError

from extensions import db
from models import Equipe


class EquipeForm(FlaskForm):
    # TODO (parte 2): campos nome, trilha_id e descricao + validacao de nome repetido
    enviar = SubmitField("Criar equipe")
