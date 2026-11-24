from flask import Blueprint, render_template

bp = Blueprint("inscricoes", __name__)

# TODO (parte 1): ver docs/tarefas/1-inscricoes.md


@bp.route("/inscricao", methods=["GET", "POST"])
def inscricao():
    return render_template("em_construcao.html", titulo="Inscrição", parte=1)
