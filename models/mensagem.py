from datetime import datetime

from extensions import db


class Mensagem(db.Model):
    """Mensagem enviada pela página de contato."""
    __tablename__ = "mensagem"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    assunto = db.Column(db.String(20), nullable=False)
    texto = db.Column(db.String(1000), nullable=False)
    enviada_em = db.Column(db.DateTime, nullable=False, default=datetime.now)
    lida = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<Mensagem {self.id}>"
