---
title: Sistema de Navegação e Mapeamento Simultâneo
sidebar_position: 3
---

## Introdução 

Nessa seção, é apresentado um sistema inovador de navegação e mapeamento simultâneo para o projeto que desempenha funções essenciais para navegação do robô.

O sistema é composto por uma arquitetura baseada no ROS2 (Robot Operating System 2) que utiliza nós interconectados para comunicação eficiente. O chatbot, dotado de um documento de contexto que contém a localização detalhada das peças no almoxarifado, é um ponto central na interação entre os usuários e o sistema.

Para a navegação do AMR, um nó específico recebe as coordenadas das peças solicitadas via chatbot. Essas coordenadas são, posteriormente, processadas por meio de um lançador, que ativa um nó de navegação. Este nó, por sua vez, inicia o RViz, uma ferramenta de visualização, e carrega o mapa previamente salvo do ambiente de simulação. Com base nessas informações, o sistema orienta o robô até as coordenadas fornecidas, permitindo que o AMR localize e colete as peças desejadas no almoxarifado de forma autônoma e eficaz.

O sistema possibilita que, ao implementar a solução, o mapeamento do almoxarifado possa ser feito de forma ágil. Considerando a integração entre os componentes do sistema, o mapa correspondente ao ambiente de atuação do robô será reconhecido pelo nó de navegação do ambiente ROS, permitindo que o produto seja utilizado de forma integrada. Desse modo, o tempo dedicado à busca por peças é reduzido, e a rotina dos trabalhadores que interagem com o almoxarifado ‒ seja em sua gestão ou na procura por itens relevantes ‒ passa a ser facilitada.

## Demonstração do sistema de navegação

No vídeo abaixo, é possível visualizar a navegação do robô em funcionamento em uma simulação de busca de peças localizadas em coordenadas pré-definidas no mapa:

<iframe width="560" height="315" src="https://www.youtube.com/embed/raEjiScBLww?si=LWchqNsOgfs0wcSm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Detalhamento das etapas

Ao longo das cinco sprints pelas quais se desenvolveu o projeto, foi elaborado um sistema de navegação robusto e replicável em diferentes ambientes. Para a concretização desse objetivo, foram percorridas as seguintes etapas:

**1. Configuração do workspace ROS:** criação e organização de diretórios correspondentes ao pacote de navegação. 

**2. Configuração do Turtlebot3:** instalação e configuração do sistema operacional no microcontrolador acoplado ao robô.

**3. Mapeamento do circuito simulado:** movimentação do robô através do circuito físico simulado para mapear o ambiente via Nav2.

**4. Construção e implementação do nodo de navegação:** desenvolvimento de script de recebimento de coordenadas e movimentação.

**5. Integração entre o nodo de navegação e o nodo do chatbot:** criação de lançador para execução simultânea dos nós da solução.

No que concerne ao estudo e implementação dos componentes do sistema de navegação do robô, será necessário conferir o código-fonte do projeto. Abaixo, é possível acessar o repositório em que está contido o projeto.

[Sistema de mapeamento](https://2023m8t2-inteli.github.io/grupo2/sprint2/Mapeamento/)

[Sistema de navegação](https://2023m8t2-inteli.github.io/grupo2/sprint3/Sistema%20de%20navega%C3%A7%C3%A3o/)
