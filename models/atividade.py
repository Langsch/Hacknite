from extensions import db


class Atividade(db.Model):
    """Item da programacao do evento."""
    __tablename__ = "atividade"

    id = db.Column(db.Integer, primary_key=True)

    # TODO (parte 3): campos dia, horario, titulo, local e descricao
    #                 + consulta cronograma() ordenada por dia e horario

    def __repr__(self):
        return f"<Atividade {self.id}>"
