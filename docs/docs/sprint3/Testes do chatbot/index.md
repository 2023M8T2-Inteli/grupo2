---
title: Sistema de navegação
sidebar_position: 3
---

# Testes do chatbot

Um dos requisitos da sprint foi a testagem do chatbot construído, uma vez que um Large Language Model (LLM) foi implementado para compor a solução. Embora a integração entre o chatbot e o sistema de navegação do robô esteja prevista para a quarta sprint, é possível testar as funcionalidades do chatbot de forma isolada, a fim de verificar a eficácia do modelo de linguagem adotado pela equipe de projeto.

Até o momento, é possível realizar as validações descritas abaixo:

- O LLM é capaz de fornecer respostas que correspondam ao contexto passado para o modelo;
- O LLM é capaz de fornecer respostas baseadas no arquivo de texto utilizado para seu treinamento;
- O LLM é capaz de retornar, ao usuário, as coordenadas do item solicitado;
- O LLM é capaz de retornar uma mensagem de erro caso não tenha conseguido interpretar a solicitação do usuário.