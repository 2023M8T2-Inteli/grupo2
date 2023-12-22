---
title: Roadmap para Próximos Passos
sidebar_position: 5
---

## Roadmap para próximos passos

A presente seção do documento é dedicada à sugestão de um roadmap para os próximos passos no que concerne à implementação da iniciativa, uma vez que a solução, embora contemple todas as funcionalidades requeridas pelo escopo do projeto, pode ser aprimorada futuramente, se for conveniente ao parceiro de projeto.

### Implementação da solução

Para implementar a solução no almoxarifado da Ambev, será necessário realizar o mapeamento do ambiente utilizando o Nav2, uma vez que o mapa do espaço se faz necessário para que o sistema de navegação do robô seja utilizado de forma bem-sucedida. Além disso, de acordo com a escala do mapa gerado, o arquivo de texto responsável pelo armazenamento das coordenadas dos itens do almoxarifado deverá ser modificado, a fim de que cada artefato do local tenha sua localização indicada de forma correta no documento. Realizados os procedimentos descritos, basta executar os dois lançadores do projeto: um deles referente ao pacote de navegação e, o outro, referente ao chatbot do Telegram. Os passos indicados são explicitados no manual do usuário, documento que contempla as instruções necessárias para a execução completa do projeto.

### Sistema de logs da solução

A solução desenvolvida pela equipe Bring Beers & Bots foca em uma das duas personas contempladas pelo projeto: os técnicos de manutenção que, cotidianamente, precisam acessar o almoxarifado da Ambev em busca de itens para realizar reparos no maquinário da fábrica. Desse modo, o projeto conta com uma interface de interação simples, responsável por, principalmente, guiar o usuário até a peça desejada. Contudo, é possível, também, escalar o projeto de modo a contemplar nossa segunda persona: o colaborador responsável pela gestão do almoxarifado. Utilizando o sistema de logs da solução, contido no nodo central do projeto, é possível construir ferramentas de visualização de dados, em forma de um dashboard, que possibilitem uma administração eficiente do espaço.

O sistema de logs da solução, atualmente, é caracterizado pelo registro das interações entre usuário e chatbot. Dessa forma, fica armazenado em um arquivo de texto toda entrada inserida pelo usuário e toda saída retornada pelo chatbot. Com base nas informações extraídas, seria possível ter controle acerca de uma série de informações relevantes, que poderiam facilitar a rotina de trabalho dos funcionários responsáveis pela gestão do local. Algumas dessas informações permitiriam responder às seguintes perguntas:

- Quais peças são solicitadas com maior frequência?
- Quais peças estão em falta no almoxarifado?
- Quantos usuários acessam a aplicação por dia?
- Quantos atendimentos o robô realiza por dia?
- Quantas requisições são bem-sucedidas? Quantas apresentaram falhas?

### Solicitação de compra de peças via chatbot

Recomenda-se, também, que seja implementado um sistema de requisição de compra de peças que estejam em falta no almoxarifado. Para isso, foi idealizado, pela equipe de projeto, o seguinte fluxo: o usuário solicita um item que não foi identificado no espaço, uma vez que não se encontra disponível no documento de coordenadas para as quais o robô pode guiar o usuário. Dessa forma, o chatbot informa ao colaborador que o item em questão está em falta, questionando-o se ele deseja realizar uma requisição de compra da peça. Caso o usuário opte por realizar a requisição de compra, um e-mail de solicitação é enviado de forma automática para o setor responsável pela compra de novos itens.