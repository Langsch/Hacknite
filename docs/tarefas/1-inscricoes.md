# Parte 1 — Inscrições

**Responsável:** _a preencher (uma pessoa)_
**Branch:** `parte-1-inscricoes` (toda a parte é feita nesta branch, e só nela)

Hoje o botão "Inscreva-se" do T1 só abria um `mailto:`. A ideia é ter uma inscrição de verdade, salva no banco, em que a pessoa consegue depois consultar e cancelar usando um código.

## Arquivos

| Arquivo | O que fazer |
|---|---|
| `models/participante.py` | completar o model `Participante` |
| `forms/inscricao.py` | `InscricaoForm` |
| `rotas/inscricoes.py` | rotas abaixo (já existe o blueprint `inscricoes`) |
| `templates/inscricoes/form.html` | criar |
| `templates/inscricoes/minha.html` | criar |
| `seed.py` | completar `popula_participantes()` |

## Model `Participante`

Já existem `id`, `nome`, `email` e `equipe_id`/`equipe`. Falta acrescentar:

| Campo | Tipo | Observação |
|---|---|---|
| `curso` | `String(80)`, obrigatório | |
| `instituicao` | `String(80)`, obrigatório | default `"UFF"` |
| `nivel` | `String(20)`, obrigatório | `iniciante`, `intermediario` ou `avancado` |
| `codigo` | `String(10)`, obrigatório, `unique` | gerado sozinho: `secrets.token_hex(5).upper()` (passa uma função no `default=`) |
| `inscrito_em` | `DateTime` | default `datetime.now` |

Também vale uma property `primeiro_nome`, porque a página da equipe (parte 2) mostra só o primeiro nome dos integrantes.

## Form `InscricaoForm`

- `nome`: `StringField`, obrigatório, de 3 a 80 caracteres
- `email`: `EmailField`, obrigatório, validador `Email()`. Se o e-mail já estiver inscrito, mostrar erro no campo (método `validate_email`).
- `curso` e `instituicao`: `StringField`, obrigatórios
- `nivel`: `SelectField` com as 3 opções, mostrando um texto bonito para cada uma (ex.: "Iniciante — estou começando a programar")
- `equipe_id`: `SelectField(coerce=int)`
  - As opções vêm do banco e são montadas na rota, como o `opcoes_categorias()` do exemplo do professor.
  - A primeira opção é `(0, "Ainda não tenho equipe")`.
  - Mostrar quantas vagas cada equipe tem.
  - Se a equipe escolhida estiver lotada, dar erro no campo.
- `aceite`: `BooleanField("Li e aceito as regras do evento")`, obrigatório

## Rotas

| Rota | Método | O que faz |
|---|---|---|
| `/inscricao` | GET, POST | formulário. Se a URL vier com `?equipe=3`, já deixa a equipe 3 selecionada (a página da equipe manda para cá assim). Se der certo: salva, `flash`, log e redirect para a página da inscrição |
| `/inscricao/<codigo>` | GET | mostra os dados da inscrição e o código em destaque (`first_or_404`) |
| `/inscricao/consulta` | GET | recebe `?codigo=` de um campinho na página de inscrição e redireciona para `/inscricao/<codigo>`. Se não achar, `flash` de aviso e volta |
| `/inscricao/<codigo>/cancelar` | POST | apaga a inscrição (usar `botao_post` com confirmação) |

Endpoint `inscricoes.inscricao` tem que continuar com esse nome, porque a navbar usa.

Gravar no log (`current_app.logger.info`) cada inscrição nova e cada cancelamento, com o id e não com o e-mail.

## Templates

- `form.html`: o formulário em `content-panel` e, do lado, um card "Já se inscreveu?" com o campo do código (form GET para `/inscricao/consulta`). Usar a macro `campo()`.
- `minha.html`: dados da inscrição, código bem visível, link para a equipe (se tiver) e o botão de cancelar.

## Pronto quando

- [ ] Inscrição salva no banco e aparece no contador da Home
- [ ] Form vazio ou inválido mostra os erros em cada campo
- [ ] Não deixa inscrever o mesmo e-mail duas vezes
- [ ] Não deixa entrar em equipe lotada
- [ ] `?equipe=<id>` pré-seleciona a equipe
- [ ] Consulta por código funciona, e o código errado dá mensagem
- [ ] Cancelar pede confirmação e apaga
- [ ] Log registra inscrição e cancelamento
- [ ] `seed.py` com os campos novos

## Não precisa

- Mandar e-mail de confirmação
- Login de participante (o código já resolve)
- Editar a inscrição (quem quiser mudar cancela e faz de novo)
