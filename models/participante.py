import secrets
from datetime import datetime

from extensions import db


class Participante(db.Model):
    __tablename__ = "participante"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    curso = db.Column(db.String(80), nullable=False)
    instituicao = db.Column(db.String(80), nullable=False, default="UFF")
    nivel = db.Column(db.String(20), nullable=False)
    codigo = db.Column(db.String(10), nullable=False, unique=True,
                       default=lambda: secrets.token_hex(5).upper())
    inscrito_em = db.Column(db.DateTime, default=datetime.now)

    # participante pode se inscrever sem equipe
    equipe_id = db.Column(db.Integer, db.ForeignKey("equipe.id"), nullable=True)
    equipe = db.relationship("Equipe", back_populates="participantes")

    @property
    def primeiro_nome(self):
        return self.nome.split(maxsplit=1)[0] if self.nome else ""

    def __repr__(self):
        return f"<Participante {self.id}: {self.nome}>"
