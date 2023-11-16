---
title: Funcionalidades do sistema
sidebar_position: 5
---

# Funcionalidades do Sistema

Durante as duas primeiras sprints do projeto, a equipe se dedicou a desenvolver os dois principais componentes da solução proposta.
As funcionalidades presentes no sistema atualmente são descritas abaixo.

**Robô autônomo**

O uso do robô autônomo se encontra no cerne do projeto. Até então, o Turtlebot3 foi configurado de modo a atender aos requisitos de movimentação e navegação autônoma. O robô já é capaz de navegar através de um circuito físico, realizar seu mapeamento e navegar pelo mapa renderizado. Além disso, o dispositivo de hardware é capaz de navegar através de waypoints por meio de um script de controle.

**Chatbot**

O chatbot representa a interface de comunicação entre o usuário e o dispositivo autônomo de hardware. Até então, o chatbot foi desenvolvido por meio de um script que utiliza expressões regulares, atendendo às necessidades do cliente no que concerne à visualização da listagem de itens do almoxarifado, à solicitação de itens do almoxarifado, à consulta de disponibilidade de itens do almoxarifado e ao status de solicitações já realizadas. O usuário, no atual momento, pode iteragir com a funcionalidade via linha de comando ou na aplicação Telegram, com a qual o chatbot foi integrado. A funcionalidade será refinada nas sprints posteriores, em que um Large Language Model (LLM) será implementado e possibilidades alternativas ao Telegram serão exploradas.