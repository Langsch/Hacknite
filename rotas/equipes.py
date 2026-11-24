from flask import Blueprint, render_template

bp = Blueprint("equipes", __name__)

# TODO (parte 2): ver docs/tarefas/2-equipes.md


@bp.route("/equipes")
def lista():
    return render_template("em_construcao.html", titulo="Equipes", parte=2)


@bp.route("/equipes/<int:id>")
def detalhe(id):
    return render_template("em_construcao.html", titulo="Equipe", parte=2)


@bp.route("/equipes/nova", methods=["GET", "POST"])
def nova():
    return render_template("em_construcao.html", titulo="Criar equipe", parte=2)
