# Parte 4 — Contato e guia do usuário

**Responsável:** _a preencher (uma pessoa)_
**Branch:** `parte-4-contato` (toda a parte é feita nesta branch, e só nela)

No T1 a página de contato era só um `mailto:`. Agora vira um formulário que salva a mensagem no banco, e a organização lê as mensagens na área `/admin`. Essa parte também escreve o **guia do usuário** do README, que é item obrigatório da entrega.

O login da organização já está pronto: é só usar `@admin_requerido`.

## Arquivos

| Arquivo | O que fazer |
|---|---|
| `models/mensagem.py` | completar o model `Mensagem` |
| `forms/contato.py` | `ContatoForm` |
| `rotas/contato.py` | rotas abaixo (já existe o blueprint `contato`) |
| `templates/contato/form.html` | criar |
| `templates/contato/admin_lista.html` | criar |
| `README.md` | seção "Guia do usuário" |

## Model `Mensagem`

| Campo | Tipo | Observação |
|---|---|---|
| `nome` | `String(80)`, obrigatório | |
| `email` | `String(120)`, obrigatório | |
| `assunto` | `String(20)`, obrigatório | `duvida`, `inscricao`, `patrocinio` ou `outro` |
| `texto` | `String(1000)`, obrigatório | |
| `enviada_em` | `DateTime` | default `datetime.now` |
| `lida` | `Boolean` | default `False` |

## Form `ContatoForm`

- `nome` e `email`: obrigatórios, com validador `Email()` no e-mail
- `assunto`: `SelectField` com as 4 opções, com texto legível ("Dúvida sobre o evento", "Quero patrocinar"…)
- `texto`: `TextAreaField`, de 10 a 1000 caracteres

O link "Quero patrocinar" da página do evento poderia abrir o form já com o assunto `patrocinio`, por exemplo aceitando `?assunto=patrocinio` na URL. O link fica em `templates/evento.html`, que é arquivo da infra, então é só avisar no PR.

## Rotas

| Rota | Método | O que faz |
|---|---|---|
| `/contato` | GET, POST | formulário. Se der certo: salva, `flash("Mensagem enviada!")`, log e redirect para `/contato` |
| `/admin/mensagens` | GET | lista as mensagens, não lidas primeiro e depois as mais novas. Badge "Nova" nas não lidas |
| `/admin/mensagens/<id>/lida` | POST | alterna lida/não lida |
| `/admin/mensagens/<id>/remover` | POST | remove (com confirmação) |

As rotas de `/admin/...` levam `@admin_requerido`. Manter os endpoints `contato.contato` e `contato.admin_mensagens`, porque a navbar e o painel usam.

Log: `info` quando chega mensagem nova (id e assunto, sem o texto) e quando uma é removida.

## Guia do usuário (README)

Fazer quando as outras partes estiverem mais ou menos prontas (a partir de 01/12). Escrever passo a passo, com prints se der:

1. Navegar pelo site (Home, Evento, Programação)
2. Criar uma equipe
3. Fazer a inscrição (com e sem equipe) e guardar o código
4. Consultar e cancelar a inscrição
5. Mandar mensagem pelo contato
6. Área da organização: entrar, editar a programação, ler as mensagens

## Pronto quando

- [ ] Mensagem é salva e a pessoa vê a confirmação
- [ ] Form inválido mostra os erros em cada campo
- [ ] Organização vê as mensagens, marca como lida e remove; sem login cai na tela de senha
- [ ] Log registra mensagem nova e remoção
- [ ] Guia do usuário escrito no README

## Não precisa

- Enviar e-mail de verdade
- Responder a mensagem pelo site (o admin clica no e-mail e responde pelo próprio e-mail)
