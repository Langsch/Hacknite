from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request, url_for)

from extensions import db
from forms.contato import ContatoForm
from models import Mensagem

from rotas.admin import admin_requerido

bp = Blueprint("contato", __name__)


@bp.route("/contato", methods=["GET", "POST"])
def contato():
    form = ContatoForm()
    if request.method == "GET":
        assunto = request.args.get("assunto")
        assuntos_validos = {valor for valor, _ in form.assunto.choices}
        if assunto in assuntos_validos:
            form.assunto.data = assunto

    if form.validate_on_submit():
        mensagem = Mensagem(
            nome=form.nome.data,
            email=form.email.data,
            assunto=form.assunto.data,
            texto=form.texto.data,
        )
        db.session.add(mensagem)
        db.session.commit()
        current_app.logger.info("Nova mensagem id=%s assunto=%s",
                                mensagem.id, mensagem.assunto)
        flash("Mensagem enviada!", "success")
        return redirect(url_for("contato.contato"))

    if form.is_submitted():
        current_app.logger.debug("Formulário de contato inválido")
    return render_template("contato/form.html", form=form)


@bp.route("/admin/mensagens")
@admin_requerido
def admin_mensagens():
    mensagens = Mensagem.query.order_by(
        Mensagem.lida.asc(), Mensagem.enviada_em.desc()
    ).all()
    return render_template("contato/admin_lista.html", mensagens=mensagens)


@bp.route("/admin/mensagens/<int:id>/lida", methods=["POST"])
@admin_requerido
def alternar_lida(id):
    mensagem = db.get_or_404(Mensagem, id)
    mensagem.lida = not mensagem.lida
    db.session.commit()
    flash("Mensagem marcada como lida." if mensagem.lida
          else "Mensagem marcada como não lida.", "success")
    return redirect(url_for("contato.admin_mensagens"))


@bp.route("/admin/mensagens/<int:id>/remover", methods=["POST"])
@admin_requerido
def remover(id):
    mensagem = db.get_or_404(Mensagem, id)
    mensagem_id = mensagem.id
    db.session.delete(mensagem)
    db.session.commit()
    current_app.logger.info("Mensagem removida id=%s", mensagem_id)
    flash("Mensagem removida.", "success")
    return redirect(url_for("contato.admin_mensagens"))
