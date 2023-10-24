---
title: Serviços e Ações
sidebar_position: 3
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Admonition from '@theme/Admonition';

# <img src={require('/img/opcional.png').default} width='35vw'/> Serviços e Ações em ROS 2

## 1. Serviços

![](/gifs/servico.gif)

[fonte](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)

Os serviços no ROS 2 são uma forma essencial de comunicação entre os nós.
Diferentemente dos tópicos, que operam no modelo de publicação-subscrição, os
serviços funcionam com base em um modelo de chamada e resposta. Isso significa
que, enquanto os tópicos permitem que os nós se inscrevam em fluxos de dados e
recebam atualizações contínuas, os serviços fornecem dados apenas quando são
especificamente chamados por um cliente. Aqui está um guia sobre como os
serviços funcionam no ROS 2:

### 2.1. Configuração
Para começar, você deve iniciar os nós do turtlesim e do turtle_teleop_key:
```
ros2 run turtlesim turtlesim_node
ros2 run turtlesim turtle_teleop_key
```

### 3.2. Listando Serviços
Para listar todos os serviços ativos no sistema, use o comando:
```
ros2 service list
```

### 3.3. Verificando o Tipo de Serviço
Cada serviço tem um tipo que descreve a estrutura dos dados de solicitação e
resposta. Para descobrir o tipo de um serviço,
use:
```
ros2 service type <nome_do_serviço>
```
Por exemplo, para o serviço `/clear`, o tipo é `std_srvs/srv/Empty`, indicando
que não envia ou recebe
dados.

### 3.4. Encontrando Serviços por Tipo
Se você quiser encontrar todos os serviços de um tipo específico, use:
```
ros2 service find <tipo_do_serviço>
```

### 3.5. Mostrando a Estrutura do Serviço
Para entender a estrutura dos argumentos de entrada de um serviço, use:
```
ros2 interface show <tipo_do_serviço>
```
Por exemplo, para o serviço `/spawn`, a estrutura inclui `x`, `y`, `theta` e
`name`.

### 3.6. Chamando um Serviço
Agora que você conhece a estrutura dos argumentos, pode chamar um serviço
usando:
```
ros2 service call <nome_do_serviço> <tipo_do_serviço> <argumentos>
```
Por exemplo, para chamar o serviço `/spawn` e criar uma nova tartaruga, use:
```
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}"
```

## 2. Ações

![](/gifs/acoes.gif)

Ações no ROS 2 são um tipo de comunicação destinado a tarefas de longa duração.
Elas são compostas por três partes: um objetivo (goal), feedback e um resultado
(result). As ações são construídas sobre tópicos e serviços, oferecendo
funcionalidades semelhantes aos serviços, mas com a capacidade de serem
canceladas e fornecerem feedback
contínuo.

### 2.1. Configuração
Antes de começar a trabalhar com ações, você precisa ter o ROS 2 e o pacote
turtlesim instalados. Inicie os nós do turtlesim e do
turtle_teleop_key:
```
ros2 run turtlesim turtlesim_node
ros2 run turtlesim turtle_teleop_key
```

### 2.2. Usando Ações
Quando você inicia o nó /teleop_turtle, ele permite que você mova a tartaruga
usando as teclas de seta e execute ações usando outras teclas. Por exemplo, as
teclas G, B, V, C, D, E, R, T permitem que você rotacione a tartaruga para
orientações específicas. A tecla F cancela uma rotação em
andamento.

### 2.3. Informações do Nó
Para ver a lista de ações que um nó fornece, use o comando `ros2 node info`. Por
exemplo:
```
ros2 node info /turtlesim
```
Isso retornará uma lista de assinantes, publicadores, serviços, servidores de
ação e clientes de ação do nó
/turtlesim.

### 2.4. Listando Ações
Para listar todas as ações ativas no sistema, use o comando:
```
ros2 action list
```
Para ver os tipos de ações, adicione a opção `-t`:
```
ros2 action list -t
```

### 2.5. Informações sobre uma Ação
Para obter informações sobre uma ação específica, como o número de clientes e
servidores de ação, use o
comando:
```
ros2 action info <nome_da_ação>
```

### 2.6. Estrutura da Ação
Para ver a estrutura de um tipo de ação, use o comando:
```
ros2 interface show <tipo_da_ação>
```
Isso mostrará a estrutura dos objetivos, resultados e feedback da ação.

### 2.7. Enviando um Objetivo para uma Ação
Para enviar um objetivo para uma ação, use o comando:
```
ros2 action send_goal <nome_da_ação> <tipo_da_ação> <valores>
```
Você pode adicionar a opção `--feedback` para ver o feedback contínuo da ação.

## 3. Exemplos

<Admonition 
    type="note" 
    icon=<img src={require('/gifs/loading.gif').default} width='20vw' />
    title="Work in progress">
</Admonition>
