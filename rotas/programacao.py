from flask import Blueprint, render_template

from rotas.admin import admin_requerido

bp = Blueprint("programacao", __name__)

# TODO (parte 3): ver docs/tarefas/3-programacao.md


@bp.route("/programacao")
def cronograma():
    return render_template("em_construcao.html", titulo="Programação", parte=3)


@bp.route("/admin/programacao")
@admin_requerido
def admin_lista():
    return render_template("em_construcao.html", titulo="Editar programação", parte=3)
