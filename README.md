# HackNite 2026

Site do hackathon HackNite 2026 (UFF), feito em Flask. Trabalho 2 da disciplina Introdução ao Web Avançado (2026-2), que transforma o site estático do Trabalho 1 em uma aplicação com banco de dados.

**Aplicação no ar:** _a preencher (link do PythonAnywhere)_

## Grupo

**Nome do grupo:** _a preencher_

| Integrante | Parte |
|---|---|
| Langsch | Infraestrutura (estrutura do projeto, layout base, configuração, log, área da organização), revisão e deploy |
| Ananias | Inscrições |
| _a preencher_ | Equipes |
| VictorCCruz1 | Programação |
| _a preencher_ | Contato e guia do usuário |

Descrição de cada parte em [`docs/tarefas/`](docs/tarefas/).

## Organização da aplicação

```
Hacknite/
├── app.py              cria o app Flask, configura o log, registra os blueprints e trata erros 404/500
├── config.py           lê as configurações do arquivo .env (python-dotenv)
├── extensions.py       instâncias do SQLAlchemy (db) e do CSRFProtect
├── seed.py             dados de exemplo inseridos quando o banco está vazio
├── requirements.txt
├── .env.example        modelo do .env (o .env de verdade não vai para o git)
│
├── models/             tabelas (SQLAlchemy)
│   ├── equipe.py           Trilha e Equipe
│   ├── participante.py     Participante
│   ├── atividade.py        Atividade (programação)
│   └── mensagem.py         Mensagem (contato)
│
├── forms/              formulários (Flask-WTF)
│   ├── inscricao.py        InscricaoForm
│   ├── equipe.py           EquipeForm
│   ├── atividade.py        AtividadeForm
│   ├── contato.py          ContatoForm
│   └── admin.py            LoginForm
│
├── rotas/              um blueprint por área do site
│   ├── principal.py        Home e página do evento
│   ├── inscricoes.py       inscrição, consulta e cancelamento
│   ├── equipes.py          lista, detalhe e criação de equipes
│   ├── programacao.py      programação pública e edição pela organização
│   ├── contato.py          formulário de contato e leitura das mensagens
│   └── admin.py            login da organização e decorator admin_requerido
│
├── templates/          páginas (Jinja2)
│   ├── base.html           layout com navbar e rodapé
│   ├── _macros.html        macros campo(), breadcrumb() e botao_post()
│   ├── index.html, evento.html, erro.html
│   ├── admin/              login e painel da organização
│   └── inscricoes/, equipes/, programacao/, contato/
│
├── static/             CSS e JavaScript
├── trabalho1/          site estático entregue no Trabalho 1 (referência)
└── docs/               enunciado, tarefas e guia de contribuição
```

Arquivos gerados ao rodar (fora do git): `instance/hacknite.db` (banco SQLite) e `logs/hacknite.log` (log).

## Como executar

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python app.py                     # http://127.0.0.1:5000
```

Para apagar e recriar o banco com os dados de exemplo: `flask --app app reset-db`.

## Guia do usuário

_a preencher_
