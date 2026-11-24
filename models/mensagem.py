from extensions import db


class Mensagem(db.Model):
    """Mensagem enviada pela pagina de contato."""
    __tablename__ = "mensagem"

    id = db.Column(db.Integer, primary_key=True)

    # TODO (parte 4): campos nome, email, assunto, texto, enviada_em e lida

    def __repr__(self):
        return f"<Mensagem {self.id}>"
