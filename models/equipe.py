from extensions import db
from datetime import datetime


MAX_MEMBROS = 5


class Trilha(db.Model):
    __tablename__ = "trilha"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False, unique=True)
    descricao = db.Column(db.String(280), nullable=False)
    icone = db.Column(db.String(40), nullable=False, default="lightbulb")  # nome do Bootstrap Icon

    equipes = db.relationship("Equipe", back_populates="trilha")

    def __repr__(self):
        return f"<Trilha {self.nome}>"


class Equipe(db.Model):
    __tablename__ = "equipe"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False, unique=True)
    descricao = db.Column(db.String(280), nullable=False, default="")
    criada_em = db.Column(db.DateTime, nullable=False, default=datetime.now)

    trilha_id = db.Column(db.Integer, db.ForeignKey("trilha.id"), nullable=False)
    trilha = db.relationship("Trilha", back_populates="equipes")

    participantes = db.relationship("Participante", back_populates="equipe")

    @property
    def total_membros(self):
        return len(self.participantes)

    @property
    def vagas(self):
        return max(0, MAX_MEMBROS - self.total_membros)

    @property
    def lotada(self):
        return self.vagas == 0

    def __repr__(self):
        return f"<Equipe {self.nome}>"
