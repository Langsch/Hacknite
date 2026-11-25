from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError

from extensions import db
from models import Equipe, Participante

MAX_MEMBROS_EQUIPE = 5


def vagas_equipe(equipe):
    vagas = getattr(equipe, "vagas", None)
    if vagas is not None:
        return vagas

    limite = getattr(equipe, "MAX_MEMBROS", MAX_MEMBROS_EQUIPE)
    membros = db.session.query(
        db.func.count(Participante.id)
    ).filter(Participante.equipe_id == equipe.id).scalar() or 0
    return max(0, limite - membros)


def equipe_lotada(equipe):
    lotada = getattr(equipe, "lotada", None)
    if lotada is not None:
        return lotada
    return vagas_equipe(equipe) == 0


class InscricaoForm(FlaskForm):
    nome = StringField("Nome completo", validators=[
        DataRequired("Informe seu nome."),
        Length(min=3, max=80,
               message="O nome deve ter entre 3 e 80 caracteres."),
    ])
    email = EmailField("E-mail", validators=[
        DataRequired("Informe seu e-mail."),
        Email("Informe um e-mail válido."),
        Length(max=120, message="O e-mail deve ter no máximo 120 caracteres."),
    ])
    curso = StringField("Curso", validators=[
        DataRequired("Informe seu curso."),
        Length(max=80, message="O curso deve ter no máximo 80 caracteres."),
    ])
    instituicao = StringField("Instituição", default="UFF", validators=[
        DataRequired("Informe sua instituição."),
        Length(max=80,
               message="A instituição deve ter no máximo 80 caracteres."),
    ])
    nivel = SelectField("Nível de experiência", choices=[
        ("iniciante", "Iniciante — estou começando a programar"),
        ("intermediario", "Intermediário — já tenho alguma experiência"),
        ("avancado", "Avançado — tenho bastante experiência"),
    ], validators=[DataRequired("Selecione seu nível de experiência.")])
    equipe_id = SelectField("Equipe", coerce=int)
    aceite = BooleanField("Li e aceito as regras do evento", validators=[
        DataRequired("Você precisa aceitar as regras do evento."),
    ])
    enviar = SubmitField("Confirmar inscrição")

    def validate_email(self, field):
        email = field.data.lower()
        participante_id = db.session.query(Participante.id).filter(
            db.func.lower(Participante.email) == email
        ).first()
        if participante_id:
            raise ValidationError("Este e-mail já possui uma inscrição.")

    def validate_equipe_id(self, field):
        if field.data == 0:
            return

        equipe = Equipe.query.filter_by(id=field.data).first()
        if equipe is None:
            raise ValidationError("A equipe selecionada não existe.")
        if equipe_lotada(equipe):
            raise ValidationError("Esta equipe está lotada.")
