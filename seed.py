"""Dados de exemplo. So insere quando a tabela esta vazia."""
from datetime import date, time

from extensions import db
from models import Atividade, Equipe, Participante, Trilha


def popula_trilhas():
    if Trilha.query.count() > 0:
        return
    db.session.add_all([
        Trilha(nome="Educação", icone="mortarboard",
               descricao="Ferramentas que ajudem estudantes e professores a ensinar e aprender melhor."),
        Trilha(nome="Saúde", icone="heart-pulse",
               descricao="Soluções para acesso à informação, prevenção e cuidado em saúde."),
        Trilha(nome="Mobilidade Urbana", icone="bus-front",
               descricao="Ideias para deslocamento mais seguro, acessível e eficiente em Niterói."),
        Trilha(nome="Sustentabilidade", icone="tree",
               descricao="Tecnologia para consumo consciente, reciclagem e economia de energia."),
    ])
    db.session.commit()


def popula_equipes():
    # TODO (parte 2): completar com descricao quando o campo existir
    if Equipe.query.count() > 0:
        return
    mobilidade = Trilha.query.filter_by(nome="Mobilidade Urbana").first()
    educacao = Trilha.query.filter_by(nome="Educação").first()
    db.session.add_all([
        Equipe(nome="Bytes da Boa Viagem", trilha=mobilidade),
        Equipe(nome="Monitores Noturnos", trilha=educacao),
    ])
    db.session.commit()


def popula_participantes():
    # TODO (parte 1): completar com os campos novos (curso, instituicao, nivel...)
    if Participante.query.count() > 0:
        return
    bytes_bv = Equipe.query.filter_by(nome="Bytes da Boa Viagem").first()
    monitores = Equipe.query.filter_by(nome="Monitores Noturnos").first()
    db.session.add_all([
        Participante(nome="Ana Exemplo", email="ana@example.com", equipe=bytes_bv),
        Participante(nome="Bruno Exemplo", email="bruno@example.com", equipe=bytes_bv),
        Participante(nome="Carla Exemplo", email="carla@example.com", equipe=monitores),
    ])
    db.session.commit()


def popula_atividades():
    if Atividade.query.count() > 0:
        return
    sexta = date(2026, 12, 11)
    sabado = date(2026, 12, 12)
    db.session.add_all([
        Atividade(dia=sexta, horario=time(18), titulo="Credenciamento e recepção",
                  local="Entrada principal"),
        Atividade(dia=sexta, horario=time(19),
                  titulo="Abertura e apresentação dos desafios", local="Auditório"),
        Atividade(dia=sexta, horario=time(20),
                  titulo="Formação das equipes e início do hackathon",
                  local="Espaço de inovação"),
        Atividade(dia=sabado, horario=time(8),
                  titulo="Mentorias e desenvolvimento dos projetos",
                  local="Espaço de inovação"),
        Atividade(dia=sabado, horario=time(17),
                  titulo="Apresentações, avaliação e premiação", local="Auditório"),
    ])
    db.session.commit()


def popula_banco():
    popula_trilhas()
    popula_equipes()
    popula_participantes()
    popula_atividades()
