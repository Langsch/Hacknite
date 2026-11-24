from extensions import db


class Atividade(db.Model):
    """Item da programacao do evento."""
    __tablename__ = "atividade"

    id = db.Column(db.Integer, primary_key=True)
    dia = db.Column(db.Date, nullable=False)
    horario = db.Column(db.Time, nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    local = db.Column(db.String(60), nullable=False)
    descricao = db.Column(db.String(280))

    @classmethod
    def cronograma(cls):
        return cls.query.order_by(cls.dia, cls.horario).all()

    def __repr__(self):
        return f"<Atividade {self.id}>"
