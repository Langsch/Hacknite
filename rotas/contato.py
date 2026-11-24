from flask import Blueprint, render_template

from rotas.admin import admin_requerido

bp = Blueprint("contato", __name__)

# TODO (parte 4): ver docs/tarefas/4-contato.md


@bp.route("/contato", methods=["GET", "POST"])
def contato():
    return render_template("em_construcao.html", titulo="Contato", parte=4)


@bp.route("/admin/mensagens")
@admin_requerido
def admin_mensagens():
    return render_template("em_construcao.html", titulo="Mensagens recebidas", parte=4)
