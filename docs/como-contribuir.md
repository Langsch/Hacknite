# Como contribuir

Leia isto antes de começar a sua parte. A tarefa de cada um está em [`docs/tarefas/`](tarefas/).

## Rodando o projeto

```bash
git clone <url do repositorio>
cd Hacknite
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env              # Windows: copy .env.example .env
python app.py                     # http://127.0.0.1:5000
```

- O banco SQLite é criado sozinho em `instance/hacknite.db` com dados de exemplo.
- A área da organização fica em `/admin`. Localmente a senha é a do `.env` (`admin123`).
- O log fica em `logs/hacknite.log`.

**Mudou algum model?** O `create_all()` não altera tabela que já existe. Rode:

```bash
flask --app app reset-db
```

Isso apaga o banco e recria tudo com os dados de exemplo do `seed.py`.

## Onde fica cada coisa

| Caminho | O que é | Quem mexe |
|---|---|---|
| `app.py` | cria o app, log, erros, registra os blueprints | infra |
| `config.py`, `extensions.py`, `.env.example` | configuração, `db` e `csrf` | infra |
| `models/` | um arquivo por parte | cada um no seu |
| `forms/` | um arquivo por parte | cada um no seu |
| `rotas/` | um blueprint por parte | cada um no seu |
| `templates/<parte>/` | templates da parte | cada um no seu |
| `templates/base.html`, `_macros.html` | layout e macros compartilhados | infra |
| `static/` | CSS e JS | infra (pode pedir classe nova) |
| `seed.py` | dados de exemplo, uma função por parte | cada um na sua função |
| `trabalho1/` | site estático do Trabalho 1, só referência | ninguém |

Cada parte já tem as rotas criadas mostrando uma página "em construção". É só trocar pela implementação de verdade. Os pontos para completar estão marcados no código com `TODO (parte N)`.

Se precisar mudar arquivo de outra parte ou da infra, fala no grupo antes. Assim ninguém pisa no código do outro e não dá conflito.

## Padrão do código

A base é o exemplo do professor das aulas 7 a 9: <https://github.com/jviterbo/UFF-DevWeb-Aula07e08-Exemplo>. Na dúvida sobre como fazer alguma coisa, faça igual a ele.

- Nomes de variáveis, funções, rotas e tabelas em **português**, sem acento (`inscrito_em`, `nova_equipe`).
- Model: `db.Column`, `db.ForeignKey`, `db.relationship(back_populates=...)`, como em `models/equipe.py`.
- Busca por id: `db.get_or_404(Model, id)`.
- Formulários sempre com **Flask-WTF** (`forms/`), com validadores e mensagens em português.
- No template, use a macro `campo()` de `_macros.html` para renderizar os campos (label, classes e erros já saem prontos).
- Depois de um POST que deu certo: `flash("mensagem", "success")` seguido de `redirect(...)`. Não renderize direto.
- Tudo que **altera** dados (remover, cancelar, marcar) é **POST**, nunca link GET. Para isso existe a macro `botao_post()`, que já manda o token CSRF e aceita `confirmar="Tem certeza?"`.
- Rotas da organização levam `@admin_requerido` (de `rotas/admin.py`).
- **Log** (é requisito do trabalho): use `current_app.logger` nas ações importantes da sua parte.
  - `info`: algo foi criado ou removido (`"Nova inscricao id=%s"`).
  - `debug`: detalhe útil para achar bug (form inválido, busca sem resultado).
  - `warning`: algo estranho (tentativa repetida, dado inconsistente).
  - Não coloque senha nem e-mail completo no log.
- Templates estendem `base.html` e usam os blocos `titulo`, `breadcrumb` e `conteudo`. Reaproveite as classes que já existem: `content-panel`, `info-card`, `page-heading`, `hero-panel`, `schedule-wrap`.
- Não adicione biblioteca nova no `requirements.txt` sem combinar.
- Comentário só onde ajuda a entender alguma coisa que não é óbvia.

## Git

```bash
git checkout main
git pull
git checkout -b parte-2-equipes        # nome da branch: parte-N-assunto
# ... trabalha, testa ...
git add models/equipe.py rotas/equipes.py ...
git commit -m "lista de equipes com filtro por trilha"
git push -u origin parte-2-equipes
```

- Faça vários commits pequenos com mensagem dizendo o que mudou, não um commitzão no final.
- Quando a parte estiver pronta, abra um **Pull Request para a `main`**. Alguém da infra revisa e faz o merge.
- Se a `main` andou enquanto você trabalhava: `git pull origin main` na sua branch e resolva os conflitos, se houver.
- **Nunca** faça commit de `.env`, `venv/`, `instance/` ou `logs/` (o `.gitignore` já barra).

## Antes de abrir o PR

- [ ] `flask --app app reset-db` e `python app.py` rodam sem erro
- [ ] Todas as rotas da sua parte abrem e os forms mostram os erros de validação
- [ ] Testou no celular (ou com o DevTools em modo responsivo)
- [ ] As ações importantes aparecem em `logs/hacknite.log`
- [ ] Não sobrou `TODO (parte N)` da sua parte nem a página "em construção"
- [ ] Atualizou a sua função no `seed.py`
