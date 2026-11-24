# Trabalho 2 — Enunciado e requisitos

**Disciplina:** Introdução ao Web Avançado (2026-2) — Prof. José Viterbo Filho
**Valor:** 100 pontos · **Entrega:** 4 de dezembro de 2026, 21:59
**Peso:** P = (P1 + 2·P2) / 3 — este trabalho é o P2 e vale o dobro do Trabalho 1.

## Enunciado (texto do professor)

> Esta atividade deve ser realizada em grupos, considerando os mesmos grupos do Trabalho 1.
>
> Cada grupo deverá transformar o site apresentado no Trabalho 1 em uma aplicação Web, implementando páginas e funcionalidades dinâmicas com persistência de dados. Deve-se utilizar o framework Flask e suas tecnologias associadas (Jinja2, Flask-WTF, SQLAlchemy, Dotenv, etc.).

## Checklist de requisitos

### Aplicação
- [ ] Flask + Jinja2 (templates)
- [ ] Flask-WTF (formulários)
- [ ] SQLAlchemy (persistência)
- [ ] python-dotenv (configuração via `.env`)
- [ ] **No mínimo 5 rotas**
- [ ] **No mínimo 3 models**
- [ ] **No mínimo 2 forms**
- [ ] **Log** com registro de informações para debug

### Entrega (feita por 1 único membro do grupo)
- [ ] Link da aplicação rodando no **PythonAnywhere**
- [ ] Link do código no **GitHub**

### README.md no GitHub (obrigatório)
- [ ] Preâmbulo: nome do grupo, lista de componentes e **divisão de tarefas**
- [ ] Descrição detalhada da organização da aplicação (diretórios e arquivos)
- [ ] Guia do usuário da aplicação

## Material de referência

- Exemplo das aulas 7, 8 e 9 (app "Meus Recados"): <https://github.com/jviterbo/UFF-DevWeb-Aula07e08-Exemplo>
  - Organização: `app.py` (rotas), `models.py`, `forms.py`, `templates/`, `requirements.txt`
  - Usa Flask-SQLAlchemy, Flask-WTF com `CSRFProtect`, `flash()`, `get_or_404` e `errorhandler(404)`
  - **Não tem** dotenv nem log; esses dois itens precisam ser feitos por nós
- Versão rodando no PythonAnywhere: <https://viterbo.pythonanywhere.com/>
