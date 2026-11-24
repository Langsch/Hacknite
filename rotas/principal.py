from flask import Blueprint, render_template

from models import Equipe, Participante, Trilha

bp = Blueprint("principal", __name__)


@bp.route("/")
def index():
    numeros = {
        "inscritos": Participante.query.count(),
        "equipes": Equipe.query.count(),
        "trilhas": Trilha.query.count(),
    }
    trilhas = Trilha.query.order_by(Trilha.nome).all()
    return render_template("index.html", numeros=numeros, trilhas=trilhas)


@bp.route("/evento")
def evento():
    trilhas = Trilha.query.order_by(Trilha.nome).all()
    return render_template("evento.html", trilhas=trilhas)
