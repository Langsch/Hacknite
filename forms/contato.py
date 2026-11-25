from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContatoForm(FlaskForm):
    nome = StringField("Nome", validators=[
        DataRequired("Informe seu nome."),
        Length(max=80, message="O nome deve ter no máximo 80 caracteres."),
    ])
    email = StringField("E-mail", validators=[
        DataRequired("Informe seu e-mail."),
        Email(message="Informe um e-mail válido."),
        Length(max=120, message="O e-mail deve ter no máximo 120 caracteres."),
    ])
    assunto = SelectField("Assunto", choices=[
        ("duvida", "Dúvida sobre o evento"),
        ("inscricao", "Dúvida sobre inscrição"),
        ("patrocinio", "Quero patrocinar"),
        ("outro", "Outro assunto"),
    ], validators=[DataRequired("Selecione um assunto.")])
    texto = TextAreaField("Mensagem", validators=[
        DataRequired("Escreva sua mensagem."),
        Length(min=10, max=1000,
               message="A mensagem deve ter entre 10 e 1000 caracteres."),
    ])
    enviar = SubmitField("Enviar mensagem")
