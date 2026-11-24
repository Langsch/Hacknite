# Parte 3 — Programação

**Responsável:** _a preencher (uma pessoa)_
**Branch:** `parte-3-programacao`

No T1 a programação era uma tabela fixa no HTML, e ainda passava de 20:00 direto para 08:00 sem dizer que tinha virado o dia. Agora ela vem do banco, separada por dia, e a organização consegue editar pela área `/admin`.

O login da organização já está pronto: é só usar `@admin_requerido`.

## Arquivos

| Arquivo | O que fazer |
|---|---|
| `models/atividade.py` | completar o model `Atividade` |
| `forms/atividade.py` | `AtividadeForm` |
| `rotas/programacao.py` | rotas abaixo (já existe o blueprint `programacao`) |
| `templates/programacao/cronograma.html` | criar (página pública) |
| `templates/programacao/admin_lista.html` | criar |
| `templates/programacao/form.html` | criar (serve para criar e editar) |
| `seed.py` | completar `popula_atividades()` |

## Model `Atividade`

| Campo | Tipo | Observação |
|---|---|---|
| `dia` | `Date`, obrigatório | |
| `horario` | `Time`, obrigatório | |
| `titulo` | `String(100)`, obrigatório | |
| `local` | `String(60)`, obrigatório | |
| `descricao` | `String(280)` | opcional |

Também um `@classmethod cronograma()` que devolve tudo ordenado por `dia` e `horario`, igual ao `pendentes()` do exemplo do professor.

## Form `AtividadeForm`

`dia` (`DateField`), `horario` (`TimeField`), `titulo`, `local` (obrigatórios) e `descricao` (`TextAreaField`, opcional, máximo de 280).

## Rotas

| Rota | Método | O que faz |
|---|---|---|
| `/programacao` | GET | pública. Uma tabela por dia, com título tipo "Sexta, 11/12". Para agrupar: `itertools.groupby(atividades, key=lambda a: a.dia)` |
| `/admin/programacao` | GET | lista as atividades com botões Editar e Remover, e o botão "Nova atividade" |
| `/admin/programacao/nova` | GET, POST | cria |
| `/admin/programacao/<id>/editar` | GET, POST | edita. `AtividadeForm(obj=atividade)` já preenche o form, igual ao `editar_recado` do professor, e `form.populate_obj(atividade)` salva |
| `/admin/programacao/<id>/remover` | POST | remove (usar `botao_post` com confirmação) |

As rotas de `/admin/...` levam `@admin_requerido`. Manter os endpoints `programacao.cronograma` e `programacao.admin_lista`, porque a navbar e o painel usam.

Para mostrar o dia da semana em português, crie um filtro no próprio blueprint:

```python
@bp.app_template_filter("dia_semana")
def dia_semana(d):
    ...
```

Log: `info` ao criar, editar e remover atividade.

## Seed

Passar a tabela do T1 (`trabalho1/programacao.html`) para o `popula_atividades()`:

- sexta 11/12/2026: 18:00, 19:00 e 20:00
- sábado 12/12/2026: 08:00 e 17:00

Se quiser, acrescente uma ou duas atividades que façam sentido (ex.: pizza à meia-noite).

## Pronto quando

- [ ] `/programacao` mostra as atividades do banco separadas por dia e em ordem
- [ ] Organização consegue criar, editar e remover; sem login cai na tela de senha
- [ ] Form mostra erro com campo vazio ou data inválida
- [ ] Log registra criar, editar e remover
- [ ] `seed.py` com a programação do T1
- [ ] Tabela não quebra no celular (`table-responsive`)

## Não precisa

- Calendário visual, exportar para .ics
- Inscrição em atividade específica
