from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional, ValidationError

from extensions import db
from models import Equipe


class EquipeForm(FlaskForm):
    nome = StringField("Nome da equipe", validators=[
        DataRequired("Informe o nome da equipe."),
        Length(min=3,max=60,message="O nome deve ter entre 3 e 60 caracteres.")
    ])
    trilha_id = SelectField(
        "Trilha",
        coerce=int,
        validators=[DataRequired("Selecione uma trilha.")]
    )
    descricao = TextAreaField("Descrição", validators=[
        Optional(),
        Length(max=280, message="A descrição deve ter no máximo 280 caracteres.")
    ])
    enviar = SubmitField("Criar equipe")
    def validate_nome(self, field):
        nome = field.data.strip()

        equipe_existente = Equipe.query.filter(
            db.func.lower(Equipe.nome) == nome.lower()
        ).first()
        if equipe_existente:
            raise ValidationError("Já existe uma equipe com esse nome.")
