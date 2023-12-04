---
title: Funcionalidades do sistema
sidebar_position: 7
---

# Funcionalidades do Sistema

Nas três primeiras iterações do projeto, a equipe concentrou seus esforços no desenvolvimento de três componentes-chave: o LLM, o robô autônomo e o chatbot.


**Robô Autônomo**

O uso central do projeto reside no robô autônomo, onde o Turtlebot3 foi configurado para atender aos requisitos de movimentação e navegação autônoma. Até agora, o robô demonstrou habilidades impressionantes, conseguindo navegar por um circuito físico, realizar o mapeamento do ambiente e navegar de acordo com o mapa gerado. Além disso, seu hardware é capaz de seguir waypoints por meio de um script de controle.

Recentemente, um workspace em ROS2 foi estabelecido para receber pontos identificados pelo LLM, permitindo que o robô seja direcionado até a localização da ferramenta escolhida pelo usuário.

Funcionalidades:
- Navegação autônoma
- Trabalho com waypoints
- Arquitetura modular em pacotes

**Chatbot**

O chatbot representa a interface de comunicação entre o usuário e o dispositivo autônomo de hardware. Até agora, o chatbot foi integrado com o LLM para atender às necessidades do cliente, incluindo requisição de ferramentas e dúvidas sobre as mesmas.

Atualmente, os usuários podem interagir com o chatbot por meio da interface do Telegram, que foi integrada à aplicação. As funcionalidades do chatbot serão aprimoradas nas próximas iterações. No momento, os usuários podem digitar uma sentença, e o chatbot retornará a localização da ferramenta solicitada.

Ainda não foi feita a integração entre o chatbot e o robô, deste modo ainda não é possível a movimentação do robô para um determinado ponto descrito no chat.

Funcionalidades:
- Uso de expressões regulares
- Arquitetura modular em pacotes
- Respostas contextualizadas à ferramenta solicitada

**LLM**

Na última iteração, foi implementado um modelo chamado Ollama para o LLM, porém será alterado para o modelo da OpenAI. Este modelo consome informações de um arquivo txt contendo ferramentas e suas respectivas localizações. Adicionalmente, um contexto foi adicionado para aprimorar a precisão das respostas, garantindo uma localização assertiva da ferramenta. A funcionalidade de requisitar uma informação sobre alguma peça ainda não foi criada porém será desenvolvida durante as próximas sprints.



Funcionalidades:
- Leitura e interpretação de arquivos
- Modularização da resposta conforme a solicitação do usuário
- Arquitetura em pacote

**Sistema em Funcionamento**

No link abaixo, é possível ver como funciona a interação do usuário com o chatbot. Um detalhe importante é que, nesta sprint, não foi possível realizar a conexão dos nós com o robô. Dessa forma, apenas o chatbot está funcionando.

<iframe width="560" height="315" src="https://www.youtube.com/embed/aWsOsiPD0m8?si=GJ-1G5MNajlRRN3l" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>