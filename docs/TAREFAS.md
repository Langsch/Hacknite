# Divisão de tarefas — 5 integrantes

> Sugestão inicial; o grupo pode trocar os nomes e ajustar o escopo.
> Cada pessoa fica com uma parte completa (model, form, rotas e templates da sua área). Assim todo mundo mexe em Flask de verdade e o README consegue mostrar a divisão com clareza.

| # | Integrante | Área | Entrega para os requisitos |
|---|---|---|---|
| 1 | _(nome)_ | Base do app e infraestrutura | dotenv, log, layout base |
| 2 | _(nome)_ | Inscrições | 1 model, 1 form, rotas |
| 3 | _(nome)_ | Equipes e trilhas | 2 models, 1 form, rotas |
| 4 | _(nome)_ | Programação e contato | 2 models, 1 form, rotas |
| 5 | _(nome)_ | Deploy, README e testes | PythonAnywhere, GitHub, README |

---

## 1. Base do app e infraestrutura
Precisa sair primeiro, porque é a base de todo o resto.
- [ ] Estrutura do projeto Flask (`app.py`, `models.py`, `forms.py`, `templates/`, `static/`)
- [ ] `requirements.txt`
- [ ] Configuração com **python-dotenv** (`.env` + `.env.example`: `SECRET_KEY`, banco, nível de log)
- [ ] **Log** em arquivo (requisições, erros, ações importantes)
- [ ] Converter o layout do Trabalho 1 (`trabalho1/`) em `base.html` com navbar e rodapé num só lugar
- [ ] Mover CSS/JS para `static/` e corrigir os bugs de CSS conhecidos (ver abaixo)
- [ ] Páginas de erro 404/500

## 2. Inscrições
- [ ] Model `Participante`
- [ ] Form de inscrição com validações (Flask-WTF)
- [ ] Rotas: formulário de inscrição e página de confirmação
- [ ] Templates correspondentes

## 3. Equipes e trilhas
- [ ] Models `Equipe` e `Trilha` (relacionamento 1:N)
- [ ] Form para criar equipe
- [ ] Rotas: listar equipes, detalhe da equipe e criar equipe
- [ ] Ligar participante a equipe (combinar com a pessoa 2)

## 4. Programação e contato
- [ ] Model `Atividade`: a programação passa a vir do banco
- [ ] Model `Mensagem` e form de contato
- [ ] Rotas: programação (separada por dia) e contato
- [ ] _(opcional)_ Área simples da organização para editar a programação e ler as mensagens

## 5. Deploy, documentação e testes
- [ ] Criar o repositório no GitHub e dar acesso a todos
- [ ] Deploy no **PythonAnywhere** (virtualenv, arquivo WSGI, `.env` no servidor)
- [ ] `README.md`: preâmbulo (grupo, integrantes, divisão), organização dos diretórios e arquivos, guia do usuário
- [ ] Testar todas as rotas e forms antes da entrega e abrir issues para os bugs
- [ ] Fazer a entrega no Classroom (links do PythonAnywhere e do GitHub)

---

## Cronograma sugerido (entrega em 04/12, 21:59)

| Até | Marco |
|---|---|
| 26/11 | Base pronta (pessoa 1) e repositório no GitHub (pessoa 5) |
| 01/12 | Funcionalidades das pessoas 2, 3 e 4 integradas |
| 03/12 | Deploy funcionando e README completo |
| 04/12 | Revisão final e entrega |

## Pendências herdadas do Trabalho 1
- `assets/js/script.js` não é carregado por nenhuma página e procura classes que não existem
- CSS: `border: 1px solid var(--line)` fica inválido (`--line` já contém espessura, estilo e cor)
- CSS: o bloco `.schedule-wrap .table` está duplicado, e o segundo anula o primeiro
- Bootstrap Icons só é carregado no `index.html`
- A programação não separa os dois dias (passa de 20:00 direto para 08:00)
