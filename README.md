# Projeto-INDIVIDUAL-2-AV---Linguagem-de-Programa-o---Reserva-de-quadras-
# Sistema de Aluguel de Quadras: Especificação de Requisitos

*Trabalho da disciplina de Programação · Base teórica: Valente (2020),
Engenharia de Software Moderna, capítulo 3.*

## 1. Visão geral

O sistema substitui o controle manual de reservas (caderno e mensagens)
de um estabelecimento que aluga quadras esportivas. O estabelecimento
trabalha com reservas em blocos de 1 hora, das 08:00 às 23:00, e a
reserva mínima é de 1 hora. O horário de funcionamento e os valores
devem ser confirmados com o estabelecimento.

### Problema e demandas

Segundo Valente (2020), os requisitos são a ponte entre um problema do
mundo real e o sistema que o resolve. Por isso, o primeiro passo é
entender o problema.

-   Reservas anotadas à mão podem gerar dois clientes no mesmo horário.
-   Não há uma visão rápida de quais horários estão livres em cada
    quadra.
-   Não há controle de quem já pagou.
-   O dono não tem acesso ao faturamento por período e não sabe qual
    quadra ou horário rende mais.

**Técnicas de elicitação sugeridas:**

-   Entrevista com o dono e o atendente.
-   Observação de um dia de trabalho.
-   Análise do caderno ou das conversas usadas para reservar.
-   Protótipo em papel do menu do sistema.

## 2. Papéis de usuário

-   **Atendente:** registra e consulta reservas e cadastra clientes.
-   **Dono:** acompanha o faturamento e o uso da quadra.
-   **Cliente:** solicita reservas, mas não opera o sistema; é um
    stakeholder.

## 3. Requisitos funcionais

  ----------------------------------------------------------------------------
          ID          Requisito            Prioridade              MVP
  ------------------- ---------------- ------------------- -------------------
         RF01         O sistema deve          Média                Sim
                      permitir                             
                      incluir,                             
                      alterar,                             
                      consultar e                          
                      excluir clientes                     
                      (nome e                              
                      telefone).                           

         RF02         O sistema deve          Alta                 Sim
                      trabalhar apenas                     
                      com uma quadra                       
                      com valor                            
                      pré-definido.                        

         RF03         O sistema deve          Alta                 Sim
                      oferecer                             
                      horários                             
                      pré-definidos,                       
                      em blocos de 1                       
                      hora, das 08:00                      
                      às 23:00.                            

         RF04         O sistema deve          Alta                 Sim
                      permitir                             
                      reservar a                           
                      quadra, em uma                       
                      data, por 1 hora                     
                      ou mais horas                        
                      consecutivas. A                      
                      duração mínima é                     
                      de 1 hora.                           

         RF05         O sistema não           Alta                 Sim
                      deve permitir                        
                      duas reservas                        
                      para a mesma                         
                      data e no mesmo                      
                      horário.                             

         RF06         O sistema deve          Alta                 Sim
                      calcular o valor                     
                      da reserva                           
                      (valor por hora                      
                      × número de                          
                      horas).                              

         RF07         O sistema deve          Alta                 Sim
                      permitir                             
                      cancelar uma                         
                      reserva,                             
                      liberando seus                       
                      horários.                            

         RF08         O sistema deve          Alta                 Sim
                      exibir a agenda                      
                      de uma data,                         
                      mostrando os                         
                      horários livres                      
                      e ocupados.                          

         RF09         O sistema deve          Alta                 Sim
                      gravar os dados                      
                      em arquivo e                         
                      recuperá-los ao                      
                      ser iniciado.                        

         RF10         O sistema deve          Média                Sim
                      gerar o                              
                      relatório de                         
                      faturamento de                       
                      um período, com                      
                      o total geral.                       

         RF11         O sistema deve          Média                Não
                      permitir                             
                      registrar o                          
                      pagamento de uma                     
                      reserva.                             

         RF12         O sistema deve          Média                Não
                      gerar relatórios                     
                      de uso: quadra                       
                      mais alugada,                        
                      horários mais                        
                      procurados e                         
                      cliente com mais                     
                      reservas.                            

         RF13         O sistema deve          Baixa                Não
                      permitir                             
                      remarcar uma                         
                      reserva para                         
                      outra data ou                        
                      horário.                             
  ----------------------------------------------------------------------------

Como o capítulo 3 destaca, nem tudo que é solicitado precisa ser
implementado na primeira versão. Por isso, os requisitos foram
priorizados, e a coluna **MVP** indica o que será incluído na primeira
versão (seção 7).
