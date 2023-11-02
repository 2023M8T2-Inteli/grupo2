# Design Patterns

Para a operacionalização do robô autônomo que localizará itens em um almoxarifado será utilizado o Sistema Operacional de Robôs, ou ROS (Robot Operating System). No ROS, o padrão de design publicador-inscrito (publisher-subscriber) é utilizado para a comunicação de abstrações chamadas de Nós. Esses Nós em ROS podem publicar mensagem para tópicos específicos, assim como outros Nós podem se inscrever nesses mesmos tópicos para receber as mesmas mensagens. Esse padrão de design permite a construção de sistemas de robótica modulares e distribuídos, ideal para o cenário de aplicação do projeto e sua futura escalabilidade. 

## Padrão de Design ROS Publisher-Subscriber para Navegação Autônoma

### 1. Nó publicador de navegação

É responsável por publicar a informação de navegação, como a posição e velocidade do robô em um determinado instante e até mesmo as coordenadas x e y de seu destino. 

### 2. Nó de inscrição de navegação

Será responsável por se inscrever no tópico de navegação, receber suas atualizações e disparar ações pré-programadas, como mensagem na tela presente no robô e mensagens de áudio, bem como cuidar do acionamento dos motores.

### 3. Tipagem de mensagem

Define um padrão estrutural para a transmissão das informações entre os Nós. Esta comporta as informações de coordenadas, velocidade, etc.

## Vantagens

1. Desacoplamento: Uma vez que os nós de Publicação e de Inscrição são desacoplados, o sistema pode ser modificado e/ou reparado com a remoção e substituição de determinados Nós com mínimos efeitos no sistema como um todo.

2. Escalabilidade: Vantagem derivada do padrão de design que permite o desacoplamento, uma vez que mais Nós podem ser adicionados ao sistema, aumentando sua funcionalidade.

3. Interoperabilidade: Dada a comunicação utilizada pelo ROS, os Nós podem ser desenvolvidos em diferentes linguagens de programação, fazendo com que cada função possa ser otimizada de acordo com a linguagem adequada. E.g.: Um nó de visão computacional desenvolvido em C++ publicando as coordenadas de um marcador de calibração posicional para o resto da aplicação em Python.
