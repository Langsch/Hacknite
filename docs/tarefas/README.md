# Tarefas

Cada parte tem **um único responsável**. Escreva o seu nome em uma linha só e não divida a parte com outra pessoa, porque o README final precisa mostrar quem fez o quê.

| Parte | Arquivo | Branch | Responsável |
|---|---|---|---|
| 0 — Infraestrutura, revisão e deploy | — | `main` | Langsch |
| 1 — Inscrições | [1-inscricoes.md](1-inscricoes.md) | `parte-1-inscricoes` | Ananias |
| 2 — Equipes | [2-equipes.md](2-equipes.md) | `parte-2-equipes` | _a preencher_ |
| 3 — Programação | [3-programacao.md](3-programacao.md) | `parte-3-programacao` | VictorCCruz1 |
| 4 — Contato e guia do usuário | [4-contato.md](4-contato.md) | `parte-4-contato` | _a preencher_ |

**Uma branch por tarefa:** cada parte é feita só na sua branch e entra na `main` por um único Pull Request. Ninguém faz commit direto na `main`.

## Prazos

| Data | O quê |
|---|---|
| 01/12 | PR de cada parte aberto |
| 02/12 | merges e ajustes de integração |
| 03/12 | deploy no PythonAnywhere e README final |
| 04/12 até 21:59 | entrega no Classroom |

## Dependências entre as partes

- **1 e 2** se encostam: o participante escolhe uma equipe no form de inscrição, e a página da equipe manda para a inscrição já com a equipe escolhida. O relacionamento `Participante.equipe` / `Equipe.participantes` já existe, então dá para cada um trabalhar sem esperar o outro. Combinem só o nome da propriedade `Equipe.lotada` (a parte 2 cria; a parte 1 usa).
- **3 e 4** usam o login da organização, que já está pronto (`@admin_requerido`).

Antes de começar, leia [como-contribuir.md](../como-contribuir.md).
