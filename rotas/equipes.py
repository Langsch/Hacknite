from flask import (
    Blueprint, current_app, flash, redirect, render_template,
    request, url_for,
)

from extensions import db
from forms.equipe import EquipeForm
from models import Equipe, Trilha

bp = Blueprint("equipes", __name__)




@bp.route("/equipes")
def lista():
    trilhas = Trilha.query.order_by(Trilha.nome).all()
    trilha_id = request.args.get("trilha", type=int)

    consulta = Equipe.query

    if trilha_id is not None:
        consulta = consulta.filter_by(trilha_id=trilha_id)

    equipes = consulta.order_by(Equipe.nome).all()

    return render_template(
        "equipes/lista.html",
        equipes=equipes,
        trilhas=trilhas,
        trilha_selecionada=trilha_id,
    )


@bp.route("/equipes/<int:id>")
def detalhe(id):
    equipe = db.get_or_404(Equipe, id)

    return render_template("equipes/detalhe.html", equipe=equipe)


@bp.route("/equipes/nova", methods=["GET", "POST"])
def nova():
    form = EquipeForm()
    trilhas = Trilha.query.order_by(Trilha.nome).all()

    form.trilha_id.choices = [
        (trilha.id, trilha.nome)
        for trilha in trilhas
    ]

    if request.method == "GET":
        trilha_id = request.args.get("trilha", type=int)
        ids_validos = {trilha.id for trilha in trilhas}

        if trilha_id in ids_validos:
            form.trilha_id.data = trilha_id

    if form.validate_on_submit():
        equipe = Equipe(
            nome=form.nome.data.strip(),
            trilha_id=form.trilha_id.data,
            descricao=form.descricao.data.strip(),
        )

        db.session.add(equipe)
        db.session.commit()

        current_app.logger.info("Nova equipe id=%s", equipe.id)
        flash("Equipe criada!", "success")

        return redirect(
            url_for("inscricoes.inscricao", equipe=equipe.id)
        )

    if form.is_submitted():
        current_app.logger.debug("Formulário inválido ao criar equipe")

    return render_template(
        "equipes/form.html",
        form=form,
        trilhas=trilhas,
    )
