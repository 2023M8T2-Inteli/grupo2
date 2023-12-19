---
title: Sistema de Navegação e Mapeamento Simultâneo
sidebar_position: 1
---

## Introdução 

 Nessa seção é apresentado um sistema inovador de navegação e mapeamento simultâneo para o projeto que desempenha funções essenciais para navegação do robô.

O sistema é composto por uma arquitetura baseada no ROS2 (Robot Operating System 2) que utiliza nós interconectados para comunicação eficiente. O chatbot, dotado de um documento de contexto que contém a localização detalhada das peças no almoxarifado, é um ponto central na interação entre usuários e o sistema.

Para a navegação do AMR, um nó específico recebe as coordenadas das peças solicitadas pelo chatbot. Essas coordenadas são então processadas por meio de um lançador, que ativa um nó de navegação. Este nó, por sua vez, inicia o RViz, uma ferramenta de visualização, e carrega o mapa previamente salvo do ambiente. Com base nessas informações, o sistema orienta o robô até as coordenadas fornecidas, permitindo que o AMR localize e colete as peças desejadas no almoxarifado de forma autônoma e eficaz.

Esse sistema integrado de chatbot, mapeamento e navegação possibilita uma gestão ágil e precisa do estoque, garantindo a eficiência na localização e obtenção das peças solicitadas, além de reduzir significativamente o tempo dedicado à logística de manuseio de materiais.

## Funcionamento da navegação
No vídeo abaixo é possível ver a navegação do robô com a definição de pontos no mapa:
<iframe width="560" height="315" src="https://www.youtube.com/embed/raEjiScBLww?si=LWchqNsOgfs0wcSm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Detalhamento das etapas 

Caso deseje entender mais como funciona cada processo específico do mapeamento e navegação é válido olhar os seguintes pontos que são cruciais para o entendimento completo do projeto. 

[Sistema de mapeamento](https://2023m8t2-inteli.github.io/grupo2/sprint2/Mapeamento/)

[Sistema de navegação](https://2023m8t2-inteli.github.io/grupo2/sprint3/Sistema%20de%20navega%C3%A7%C3%A3o/)

[]