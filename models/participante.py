from extensions import db


class Participante(db.Model):
    __tablename__ = "participante"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    # participante pode se inscrever sem equipe
    equipe_id = db.Column(db.Integer, db.ForeignKey("equipe.id"), nullable=True)
    equipe = db.relationship("Equipe", back_populates="participantes")

    # TODO (parte 1): campos curso, instituicao, nivel, codigo e inscrito_em

    def __repr__(self):
        return f"<Participante {self.id}: {self.nome}>"
