# Sistema de Aluguel da Arena Sebastião
## Especificação de Requisitos e Casos de Uso

*Trabalho da disciplina de programação · Base teórica: Valente (2020), Engenharia de Software Moderna, cap. 3*

## 1. Visão geral

O sistema substitui o controle manual de reservas (caderno, mensagens) da Arena Sebastião, em Palmeira dos Índios, que aluga uma quadra esportiva. O sistema é de uso exclusivo dessa empresa e atende essa única quadra, para marcar reservas e mostrar os horários disponíveis.

As reservas são feitas em blocos de 1 hora, das 08:00 às 23:00, e a reserva mínima é de 1 hora. O horário de funcionamento e os valores devem ser confirmados com o estabelecimento.

### Problema e demandas

Segundo Valente (2020), os requisitos são a ponte entre um problema do mundo real e o sistema que o resolve. Por isso, o primeiro passo é entender o problema. As demandas abaixo são hipóteses iniciais e devem ser confirmadas (ou substituídas) pelo que for observado no estabelecimento:

- Reservas anotadas à mão podem gerar dois clientes no mesmo horário;
- Não há uma visão rápida de quais horários estão livres na quadra;
- Não há controle de quem já pagou;
- O dono não tem o faturamento por período e não sabe quais horários rendem mais.

Técnicas de elicitação sugeridas: entrevista com o dono e o atendente; observação de um dia de trabalho; análise do caderno ou das conversas usadas para reservar; protótipo em papel do menu do sistema.

## 2. Papéis de usuário

- **Atendente:** registra e consulta reservas e cadastra clientes.
- **Dono:** acompanha o faturamento e o uso da quadra.
- **Cliente:** pede as reservas, mas não opera o sistema; é um stakeholder.

## 3. Requisitos funcionais

| ID | Requisito | Prioridade | MVP |
|---|---|---|---|
| RF01 | O sistema deve permitir incluir, alterar, consultar e excluir clientes (nome e telefone). | Média | Sim |
| RF02 | O sistema deve trabalhar com uma única quadra, com valor por hora pré-definido. | Alta | Sim |
| RF03 | O sistema deve oferecer horários pré-definidos, em blocos de 1 hora, das 08:00 às 23:00. | Alta | Sim |
| RF04 | O sistema deve permitir reservar a quadra em uma data, por 1 hora ou mais horas consecutivas. A duração mínima é de 1 hora. | Alta | Sim |
| RF05 | O sistema não deve permitir duas reservas na mesma data e no mesmo horário. | Alta | Sim |
| RF06 | O sistema deve calcular o valor da reserva (valor por hora × número de horas). | Alta | Sim |
| RF07 | O sistema deve permitir cancelar uma reserva, liberando seus horários. | Alta | Sim |
| RF08 | O sistema deve exibir a agenda de uma data, mostrando os horários livres e ocupados da quadra. | Alta | Sim |
| RF09 | O sistema deve gravar os dados em arquivo e recuperá-los ao ser iniciado. | Alta | Sim |
| RF10 | O sistema deve gerar o relatório de faturamento de um período, com o total geral. | Média | Sim |
| RF11 | O sistema deve permitir registrar o pagamento de uma reserva. | Média | Não |
| RF12 | O sistema deve gerar relatórios de uso: horários mais procurados e cliente com mais reservas. | Média | Não |
| RF13 | O sistema deve permitir remarcar uma reserva para outra data ou horário. | Baixa | Não |

Como o cap. 3 destaca, nem tudo que se pede é implementado na primeira versão. Por isso, os requisitos foram priorizados e a coluna MVP indica o que entra na primeira versão (seção 7).

## 4. Requisitos não-funcionais

Os requisitos não-funcionais usam métricas, em vez de termos vagos como rápido ou amigável, para que possam ser verificados.

| ID | Categoria | Requisito (com métrica) |
|---|---|---|
| RNF01 | Desempenho | Reservar, cancelar e consultar a agenda devem responder em até 1 segundo, com até 5.000 reservas armazenadas. |
| RNF02 | Confiabilidade | Após o encerramento normal do programa, 0% das reservas confirmadas devem ser perdidas. |
| RNF03 | Robustez | Entradas inválidas (campo vazio, texto no lugar de número, data inexistente) não devem encerrar o programa: 0 encerramentos inesperados em um teste com pelo menos 20 entradas inválidas. |
| RNF04 | Usabilidade | Um atendente sem experiência deve aprender a registrar uma reserva com até 15 minutos de treinamento e concluí-la em até 1 minuto. |
| RNF05 | Portabilidade | O sistema deve executar em Windows, Linux e macOS com Python 3.8 ou superior, usando apenas a biblioteca padrão (100%). |
| RNF06 | Espaço | O arquivo de dados deve ter no máximo 1 MB para 10.000 reservas, e o programa deve usar no máximo 50 MB de memória. |
| RNF07 | Restrição de implementação | O sistema deve ser escrito em Python, sem frameworks ou ferramentas pré-prontas. Se houver interface gráfica, usar apenas o Tkinter que acompanha o Python (confirmar com o professor). |
| RNF08 | Rastreabilidade | 100% dos requisitos funcionais devem poder ser ligados a pelo menos uma função do código, identificada pelo nome. |

## 5. Histórias de usuário

Formato do cap. 3: Como um [papel], eu gostaria de [ação]. Cada história é um cartão que resume o pedido; os detalhes são combinados em conversas e a história só é aceita se passar nos testes de confirmação.

### Atendente

- **HU01.** Como atendente, eu gostaria de cadastrar os clientes que alugam a quadra.
- **HU02.** Como atendente, eu gostaria de ver os horários livres e ocupados da quadra em uma data.
- **HU03.** Como atendente, eu gostaria de reservar a quadra por uma ou mais horas.
- **HU04.** Como atendente, eu gostaria de cancelar uma reserva.
- **HU05.** Como atendente, eu gostaria de registrar o pagamento de uma reserva.
- **HU06.** Como atendente, eu gostaria de remarcar uma reserva para outro horário.

### Dono

- **HU07.** Como dono, eu gostaria de ver o faturamento de um período.
- **HU08.** Como dono, eu gostaria de saber quais clientes mais alugam a quadra.
- **HU09.** Como dono, eu gostaria de saber quais horários são os mais procurados.
- **HU10.** Como dono, eu gostaria que as reservas continuassem salvas depois de fechar o programa.

### Épico (fica no fundo do backlog, fora do MVP)

- Como cliente, eu gostaria de reservar a quadra sozinho, pelo celular.

### Confirmação (testes de aceitação)

**HU02 — Ver horários**

- Em uma data sem reservas, a quadra mostra os 15 horários (08:00 a 22:00) como livres.
- Após reservar às 19:00, esse horário aparece como ocupado e os demais continuam livres.

**HU03 — Reservar quadra**

- Reservar um horário livre às 19:00 por 1 hora confirma a reserva e mostra o valor.
- Reservar às 19:00 por 2 horas ocupa 19:00 e 20:00.
- Tentar reservar um horário já ocupado é recusado, com aviso.
- Informar 0 hora é recusado (o mínimo é 1 hora).
- Reservar 2 horas começando às 22:00 é recusado, pois passa do funcionamento.

**HU07 — Faturamento**

- Em um período com uma reserva de R$ 80,00 e outra de R$ 160,00, o total é R$ 240,00 (valores de exemplo).
- Em um período sem reservas, o total é R$ 0,00.
- Se a data final for anterior à inicial, o pedido é recusado.

## 6. Casos de uso

Os casos de uso são documentos textuais, escritos do ponto de vista de um ator, com fluxo normal e extensões. O diagrama é apenas um índice gráfico deles. Seguindo as boas práticas do cap. 3, as operações de cadastro foram reunidas em um único caso de uso (Gerenciar Clientes).

### Lista de casos de uso

| ID | Caso de uso | Ator | Relacionamento |
|---|---|---|---|
| UC01 | Gerenciar Clientes | Atendente | — |
| UC02 | Consultar Agenda do Dia | Atendente | — |
| UC03 | Reservar Quadra | Atendente | inclui UC02 |
| UC04 | Cancelar Reserva | Atendente | — |
| UC05 | Registrar Pagamento | Atendente | — |
| UC06 | Emitir Relatório de Faturamento | Dono | — |
| UC07 | Emitir Relatório de Uso | Dono | — |

### Diagrama de casos de uso

O diagrama mostra os dois atores fora da fronteira do sistema, os casos de uso dentro dela e o relacionamento de inclusão entre Reservar Quadra e Consultar Agenda do Dia.

**Figura 1.** Diagrama de casos de uso do sistema (2 atores, 7 casos de uso, 1 inclusão).

**Leitura:** o atendente participa de cinco casos de uso e o dono dos dois relatórios; a linha tracejada indica que Reservar Quadra inclui Consultar Agenda do Dia.

### UC01. Gerenciar Clientes

**Ator:** Atendente

O atendente inclui, altera, consulta e exclui clientes, informando nome e telefone. Como o significado dessas quatro operações é claro, elas são descritas em um único caso de uso.

**Extensões:**

- Se o nome ou o telefone estiver vazio, solicitar o dado novamente.
- Se o cliente consultado não existir, informar que não foi encontrado.
- Se o cliente tiver reservas futuras, recusar a exclusão e informar o motivo.

### UC02. Consultar Agenda do Dia

**Ator:** Atendente

**Fluxo normal:**

1. Atendente informa a data.
2. Sistema apresenta os horários livres e ocupados da quadra.

**Extensões:**

- **1a.** Se a data for inválida, solicitar nova data.

### UC03. Reservar Quadra

**Ator:** Atendente

**Pré-condição:** o cliente está cadastrado.

**Pós-condição:** a reserva está gravada e seus horários aparecem como ocupados.

**Fluxo normal:**

1. Atendente informa o cliente.
2. Consultar Agenda do Dia (caso de uso incluído; a data informada nele vale para a reserva).
3. Atendente escolhe o horário inicial e a quantidade de horas.
4. Sistema calcula o valor total.
5. Sistema registra a reserva e informa horários e valor total.

**Extensões:**

- **1a.** Se o cliente não estiver cadastrado, o atendente o cadastra (Gerenciar Clientes) e retoma do passo 1.
- **2a.** Se a data for anterior à data atual, solicitar nova data.
- **3a.** Se a quantidade de horas for menor que 1, recusar e solicitar nova quantidade.
- **3b.** Se algum horário do período já estiver ocupado, informar qual e solicitar novo horário ou nova quantidade.
- **3c.** Se o período passar do fim do funcionamento (23:00), solicitar nova quantidade.
- **5a.** Se não for possível gravar os dados, informar o erro e não confirmar a reserva.

### UC04. Cancelar Reserva

**Ator:** Atendente

**Fluxo normal:**

1. Atendente informa a data da reserva.
2. Sistema lista as reservas da data.
3. Atendente escolhe a reserva a cancelar.
4. Sistema pede confirmação.
5. Atendente confirma.
6. Sistema remove a reserva e libera os horários.

**Extensões:**

- **2a.** Se não houver reservas na data, informar e encerrar.
- **3a.** Se a reserva escolhida não existir, solicitar nova escolha.
- **5a.** Se o atendente não confirmar, manter a reserva.

### UC05. Registrar Pagamento

**Ator:** Atendente

**Fluxo normal:**

1. Atendente informa o cliente.
2. Sistema lista as reservas do cliente ainda sem pagamento.
3. Atendente escolhe a reserva.
4. Sistema registra o pagamento e informa a confirmação.

**Extensões:**

- **1a.** Se o cliente não estiver cadastrado, solicitar novo cliente.
- **2a.** Se não houver reservas pendentes, informar e encerrar.

### UC06. Emitir Relatório de Faturamento

**Ator:** Dono

**Fluxo normal:**

1. Dono informa a data inicial e a data final.
2. Sistema soma o valor das reservas do período.
3. Sistema apresenta o total geral.

**Extensões:**

- **1a.** Se as datas forem inválidas ou a final for anterior à inicial, solicitar novas datas.
- **3a.** Se não houver reservas no período, apresentar R$ 0,00.

### UC07. Emitir Relatório de Uso

**Ator:** Dono

**Fluxo normal:**

1. Dono informa o período.
2. Sistema calcula as reservas por horário e as reservas por cliente.
3. Sistema apresenta os horários mais procurados e o cliente com mais reservas.

**Extensões:**

- **1a.** Se o período for inválido, solicitar nova informação.
- **3a.** Se não houver reservas no período, informar que não há dados.
- **3b.** Se houver empate, apresentar todos os empatados.

## 7. Produto Mínimo Viável (MVP)

**Hipótese de negócio a testar:** se os atendentes registrarem as reservas no sistema em vez de no caderno, os conflitos de horário deixam de ocorrer e o dono consegue saber o faturamento sem somar tudo à mão.

**Entra no MVP:** RF01 a RF10 (clientes, quadra e horários pré-definidos, reserva de 1 hora ou mais, bloqueio de conflito, cancelamento, agenda do dia, gravação em arquivo e faturamento).

**Fica fora do MVP:** pagamento (RF11), relatórios de uso (RF12), remarcação (RF13) e a reserva pelo celular.

### Ciclo construir, medir e aprender

Para evitar métricas de vaidade, o MVP é avaliado por métricas acionáveis:

- Conflitos de horário por semana (meta: 0);
- Tempo médio para registrar uma reserva (meta: até 1 minuto);
- Percentual das reservas registradas no sistema, e não no caderno (meta: pelo menos 90% após duas semanas de uso);
- Tempo para obter o faturamento do mês (meta: menos de 1 minuto).

Com os resultados, há três caminhos: ajustar o MVP e repetir o ciclo, investir em uma versão mais completa (se houver encaixe com o estabelecimento) ou mudar de rumo (pivô).

A qualidade mínima exigida é a que evita falsos negativos: o MVP não pode perder reservas, pois isso invalidaria o teste por motivo técnico.

## 8. Glossário

- **Atendente:** pessoa do estabelecimento que opera o sistema.
- **Dono:** responsável pelo estabelecimento.
- **Cliente:** pessoa que aluga a quadra, cadastrada com nome e telefone.
- **Quadra:** espaço esportivo alugável; no sistema, é a única quadra da Arena Sebastião.
- **Horário:** bloco de 1 hora iniciado em hora cheia (o horário 08:00 vale de 08:00 até 09:00).
- **Reserva:** aluguel da quadra em uma data, com horário inicial e duração em horas inteiras.
- **Valor da reserva:** valor por hora da quadra × duração em horas.
- **Faturamento:** soma dos valores das reservas do período, pagas ou não.

## 9. Pontos em aberto para confirmar com o estabelecimento

- Valor por hora da quadra (e se muda por dia ou horário);
- Horário real de funcionamento (e se muda aos fins de semana);
- Regras de cancelamento (prazo, multa);
- Existência de clientes mensalistas (reservas fixas toda semana).
