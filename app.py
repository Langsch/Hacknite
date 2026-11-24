import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, request, session

from config import Config
from extensions import csrf, db
from rotas import admin, contato, equipes, inscricoes, principal, programacao
from rotas.admin import ip_cliente
from seed import popula_banco

app = Flask(__name__)
app.config.from_object(Config)

csrf.init_app(app)   # exige o token CSRF em todo POST
db.init_app(app)

for modulo in (principal, inscricoes, equipes, programacao, contato, admin):
    app.register_blueprint(modulo.bp)


# ---------------------------------------------------------------- log
os.makedirs(app.config["LOG_DIR"], exist_ok=True)
arquivo_log = RotatingFileHandler(os.path.join(app.config["LOG_DIR"], "hacknite.log"),
                                  maxBytes=1_000_000, backupCount=3, encoding="utf-8")
arquivo_log.setFormatter(logging.Formatter(
    "%(asctime)s %(levelname)s [%(module)s:%(lineno)d] %(message)s"))
app.logger.addHandler(arquivo_log)
app.logger.setLevel(app.config["LOG_LEVEL"])


@app.after_request
def registra_requisicao(resposta):
    if request.endpoint != "static":
        app.logger.info("%s %s %s -> %s", ip_cliente(), request.method,
                        request.full_path.rstrip("?"), resposta.status_code)
    return resposta


# ---------------------------------------------------------------- templates
@app.context_processor
def variaveis_globais():
    return {"admin_logado": session.get("admin", False), "ano": datetime.now().year}


@app.template_filter("data_br")
def data_br(valor):
    return valor.strftime("%d/%m/%Y")


@app.template_filter("data_hora_br")
def data_hora_br(valor):
    return valor.strftime("%d/%m/%Y %H:%M")


# ---------------------------------------------------------------- erros
@app.errorhandler(404)
def nao_encontrado(erro):
    app.logger.debug("404 em %s", request.path)
    return render_template("erro.html", codigo=404,
                           mensagem="A página que você procura não existe."), 404


@app.errorhandler(500)
def erro_interno(erro):
    db.session.rollback()
    return render_template("erro.html", codigo=500,
                           mensagem="Algo deu errado do nosso lado. Tente de novo."), 500


# ---------------------------------------------------------------- banco
@app.cli.command("reset-db")
def reset_db():
    """Apaga e recria todas as tabelas (use depois de mudar um model)."""
    db.drop_all()
    db.create_all()
    popula_banco()
    print("Banco recriado com os dados de exemplo.")


with app.app_context():
    db.create_all()   # cria as tabelas que ainda nao existem
    popula_banco()
    if not app.config["ADMIN_PASSWORD"]:
        app.logger.warning("ADMIN_PASSWORD vazio no .env: area /admin desativada")


if __name__ == "__main__":
    app.run(debug=True)
