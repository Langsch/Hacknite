from datetime import date
from itertools import groupby

from flask import (Blueprint, current_app, flash, redirect, render_template,
                   url_for)

from extensions import db
from forms.atividade import AtividadeForm
from models import Atividade
from rotas.admin import admin_requerido

bp = Blueprint("programacao", __name__)


@bp.app_template_filter("dia_semana")
def dia_semana(dia: date):
    nomes = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
    return nomes[dia.weekday()].capitalize()


@bp.route("/programacao")
def cronograma():
    atividades = Atividade.cronograma()
    dias = [
        (dia, list(itens))
        for dia, itens in groupby(atividades, key=lambda atividade: atividade.dia)
    ]
    return render_template("programacao/cronograma.html", dias=dias)


@bp.route("/admin/programacao")
@admin_requerido
def admin_lista():
    return render_template("programacao/admin_lista.html",
                           atividades=Atividade.cronograma())


@bp.route("/admin/programacao/nova", methods=["GET", "POST"])
@admin_requerido
def nova():
    form = AtividadeForm()
    if form.validate_on_submit():
        atividade = Atividade()
        form.populate_obj(atividade)
        db.session.add(atividade)
        db.session.commit()
        current_app.logger.info("Nova atividade id=%s", atividade.id)
        flash("Atividade criada.", "success")
        return redirect(url_for("programacao.admin_lista"))
    if form.is_submitted():
        current_app.logger.debug("Formulário inválido ao criar atividade")
    return render_template("programacao/form.html", form=form, atividade=None)


@bp.route("/admin/programacao/<int:id>/editar", methods=["GET", "POST"])
@admin_requerido
def editar(id):
    atividade = db.get_or_404(Atividade, id)
    form = AtividadeForm(obj=atividade)
    if form.validate_on_submit():
        form.populate_obj(atividade)
        db.session.commit()
        current_app.logger.info("Atividade editada id=%s", atividade.id)
        flash("Atividade atualizada.", "success")
        return redirect(url_for("programacao.admin_lista"))
    if form.is_submitted():
        current_app.logger.debug("Formulário inválido ao editar atividade id=%s",
                                 atividade.id)
    return render_template("programacao/form.html", form=form, atividade=atividade)


@bp.route("/admin/programacao/<int:id>/remover", methods=["POST"])
@admin_requerido
def remover(id):
    atividade = db.get_or_404(Atividade, id)
    atividade_id = atividade.id
    db.session.delete(atividade)
    db.session.commit()
    current_app.logger.info("Atividade removida id=%s", atividade_id)
    flash("Atividade removida.", "success")
    return redirect(url_for("programacao.admin_lista"))
