import hmac
from functools import wraps

from flask import (Blueprint, current_app, flash, redirect, render_template, request, session,
                   url_for)

from forms.admin import LoginForm

bp = Blueprint("admin", __name__)


def admin_requerido(view):
    """Decorator para rotas que so a organizacao pode acessar."""
    @wraps(view)
    def protegida(*args, **kwargs):
        if not session.get("admin"):
            flash("Faça login para acessar a área da organização.", "warning")
            return redirect(url_for("admin.login", next=request.path))
        return view(*args, **kwargs)
    return protegida


def ip_cliente():
    # no PythonAnywhere o IP de verdade vem nesse cabecalho
    return request.headers.get("X-Real-IP", request.remote_addr)


@bp.route("/admin/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    senha = current_app.config["ADMIN_PASSWORD"]
    if form.validate_on_submit():
        if senha and hmac.compare_digest(form.senha.data, senha):
            session["admin"] = True
            current_app.logger.info("Login de admin (IP %s)", ip_cliente())
            destino = request.args.get("next", "")
            # so aceita caminho interno, para nao redirecionar para outro site
            if not destino.startswith("/") or destino.startswith("//"):
                destino = url_for("admin.painel")
            return redirect(destino)
        current_app.logger.warning("Senha de admin errada (IP %s)", ip_cliente())
        flash("Senha incorreta.", "danger")
    return render_template("admin/login.html", form=form, admin_ativo=bool(senha))


@bp.route("/admin/logout", methods=["POST"])
def logout():
    session.pop("admin", None)
    flash("Você saiu da área da organização.", "info")
    return redirect(url_for("principal.index"))


@bp.route("/admin")
@admin_requerido
def painel():
    return render_template("admin/painel.html")
