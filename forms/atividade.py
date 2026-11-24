from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField, TextAreaField, TimeField
from wtforms.validators import DataRequired, Length, Optional


class AtividadeForm(FlaskForm):
    dia = DateField("Dia", validators=[DataRequired("Informe o dia.")])
    horario = TimeField("Horário", validators=[DataRequired("Informe o horário.")])
    titulo = StringField("Atividade", validators=[
        DataRequired("Informe o título."),
        Length(max=100, message="O título deve ter no máximo 100 caracteres."),
    ])
    local = StringField("Local", validators=[
        DataRequired("Informe o local."),
        Length(max=60, message="O local deve ter no máximo 60 caracteres."),
    ])
    descricao = TextAreaField("Descrição", validators=[
        Optional(),
        Length(max=280, message="A descrição deve ter no máximo 280 caracteres."),
    ])
    enviar = SubmitField("Salvar")
