# Parte 2 — Equipes

**Responsável:** _a preencher (uma pessoa)_
**Branch:** `parte-2-equipes` (toda a parte é feita nesta branch, e só nela)

Página onde dá para ver as equipes inscritas, filtrar por trilha, ver quem está em cada uma e criar equipe nova. As trilhas já estão prontas no banco (`Trilha`, com 4 cadastradas no `seed.py`).

## Arquivos

| Arquivo | O que fazer |
|---|---|
| `models/equipe.py` | completar o model `Equipe` (não precisa mexer em `Trilha`) |
| `forms/equipe.py` | `EquipeForm` |
| `rotas/equipes.py` | rotas abaixo (já existe o blueprint `equipes`) |
| `templates/equipes/lista.html` | criar |
| `templates/equipes/detalhe.html` | criar |
| `templates/equipes/form.html` | criar |
| `seed.py` | completar `popula_equipes()` |

## Model `Equipe`

Já existem `id`, `nome`, `trilha_id`/`trilha` e `participantes`. Falta acrescentar:

| Campo | Tipo | Observação |
|---|---|---|
| `descricao` | `String(280)` | pode ser vazia (default `""`) |
| `criada_em` | `DateTime` | default `datetime.now` |

E também:

- uma constante `MAX_MEMBROS = 5` no topo do arquivo;
- as properties `total_membros`, `vagas` e `lotada` (`True` quando `vagas == 0`).

A parte 1 usa `lotada` e `vagas` no form de inscrição, então mantenham esses nomes.

## Form `EquipeForm`

- `nome`: `StringField`, obrigatório, de 3 a 60 caracteres. Não pode repetir nome, nem com maiúscula/minúscula diferente (`validate_nome` comparando com `db.func.lower`).
- `trilha_id`: `SelectField(coerce=int)` com as trilhas do banco (montar na rota)
- `descricao`: `TextAreaField`, opcional, máximo de 280

## Rotas

| Rota | Método | O que faz |
|---|---|---|
| `/equipes` | GET | lista em cards: nome, trilha, vagas (badge "Completa" quando lotada). Aceita `?trilha=<id>` para filtrar; botões de filtro no topo |
| `/equipes/<id>` | GET | detalhe: descrição, trilha e integrantes (só o **primeiro nome** e o curso, nunca o e-mail). Se tiver vaga, botão "Entrar nesta equipe" → `url_for('inscricoes.inscricao', equipe=equipe.id)` |
| `/equipes/nova` | GET, POST | cria a equipe. `?trilha=<id>` já seleciona a trilha. Se der certo: `flash`, log e redirect para a inscrição com a equipe nova selecionada |

Manter os endpoints `equipes.lista`, `equipes.detalhe` e `equipes.nova`, porque a navbar e a Home usam.

Log: `info` quando uma equipe for criada.

## Templates

- Cards no mesmo estilo da Home (`info-card`).
- Formulário em `content-panel`, com a macro `campo()`.
- Breadcrumb: Home › Equipes › (nome da equipe).

Pode também colocar um link "Ver equipes" em cada card de trilha em `templates/evento.html` (`url_for('equipes.lista', trilha=t.id)`). É uma mudança pequena em arquivo da infra, então avise no PR.

## Pronto quando

- [ ] Lista mostra as equipes do seed e as novas
- [ ] Filtro por trilha funciona
- [ ] Detalhe mostra os integrantes sem expor e-mail; id inexistente dá 404
- [ ] Criar equipe valida nome repetido e campos obrigatórios
- [ ] Depois de criar, vai para a inscrição com a equipe já escolhida
- [ ] Log registra criação
- [ ] `seed.py` com descrição nas equipes de exemplo

## Não precisa

- Editar ou apagar equipe pelo site (se alguém da organização precisar, faz pelo banco)
- Líder de equipe, senha de equipe, convite
