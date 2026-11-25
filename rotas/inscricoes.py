from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request, url_for)

from extensions import db
from forms.inscricao import InscricaoForm, vagas_equipe
from models import Equipe, Participante

bp = Blueprint("inscricoes", __name__)


def _opcoes_equipes(equipes):
    opcoes = [(0, "Ainda não tenho equipe")]
    for equipe in equipes:
        vagas = vagas_equipe(equipe)
        rotulo_vagas = "vaga" if vagas == 1 else "vagas"
        opcoes.append(
            (equipe.id, f"{equipe.nome} — {vagas} {rotulo_vagas} disponíveis")
        )
    return opcoes


@bp.route("/inscricao", methods=["GET", "POST"])
def inscricao():
    form = InscricaoForm()
    equipes = Equipe.query.order_by(Equipe.nome).all()
    form.equipe_id.choices = _opcoes_equipes(equipes)

    if request.method == "GET":
        equipe_id = request.args.get("equipe", type=int)
        ids_equipes = {equipe.id for equipe in equipes}
        form.equipe_id.data = equipe_id if equipe_id in ids_equipes else 0

    if form.validate_on_submit():
        equipe = next(
            (item for item in equipes if item.id == form.equipe_id.data), None
        )
        participante = Participante(
            nome=form.nome.data,
            email=form.email.data,
            curso=form.curso.data,
            instituicao=form.instituicao.data,
            nivel=form.nivel.data,
            equipe=equipe,
        )
        db.session.add(participante)
        db.session.commit()
        current_app.logger.info("Nova inscricao id=%s", participante.id)
        flash(
            "Inscrição confirmada! Guarde seu código para consultar ou cancelar.",
            "success",
        )
        return redirect(url_for("inscricoes.minha", codigo=participante.codigo))

    if form.is_submitted():
        current_app.logger.debug("Formulário inválido ao criar inscrição")

    return render_template(
        "inscricoes/form.html",
        form=form,
    )


@bp.route("/inscricao/consulta")
def consulta():
    codigo = request.args.get("codigo", "").strip().upper()
    participante = (
        Participante.query.filter_by(codigo=codigo).first() if codigo else None
    )
    if participante is None:
        current_app.logger.debug("Consulta de inscrição sem resultado")
        flash("Não encontramos uma inscrição com esse código.", "warning")
        return redirect(url_for("inscricoes.inscricao"))
    return redirect(url_for("inscricoes.minha", codigo=participante.codigo))


@bp.route("/inscricao/<codigo>")
def minha(codigo):
    participante = Participante.query.filter_by(
        codigo=codigo.strip().upper()
    ).first_or_404()
    return render_template("inscricoes/minha.html", participante=participante)


@bp.route("/inscricao/<codigo>/cancelar", methods=["POST"])
def cancelar(codigo):
    participante = Participante.query.filter_by(
        codigo=codigo.strip().upper()
    ).first_or_404()
    participante_id = participante.id
    db.session.delete(participante)
    db.session.commit()
    current_app.logger.info("Inscricao cancelada id=%s", participante_id)
    flash("Sua inscrição foi cancelada.", "success")
    return redirect(url_for("inscricoes.inscricao"))
