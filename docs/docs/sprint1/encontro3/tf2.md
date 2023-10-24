---
title: Utilizando o TF2
sidebar_position: 5
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Utilizando
transformadas em
ROS2

## 1. Introdução ao TF2 

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

[Introdução ao
TF2](https://docs.ros.org/en/humble/Tutorials/Intermediate/Tf2/Introduction-To-Tf2.html)

</Admonition>

O TF2 (Transform Library 2) é uma biblioteca no ROS que permite que você
mantenha o controle de múltiplos frames de coordenadas ao longo do tempo. Em
robótica, é crucial entender como diferentes partes do seu robô ou diferentes
robôs em um sistema estão posicionados e orientados em relação uns aos outros. O
TF2 ajuda a manter o controle dessas relações, fornecendo ferramentas para
transformar coordenadas de um frame para outro, independentemente de quando as
medições foram feitas. Isso é crucial para tarefas como navegação, planejamento
de movimento e percepção, onde você precisa alinhar informações de diferentes
sensores e atuadores que podem não estar fisicamente alinhados ou que se movem
ao longo do
tempo.

Imagine que você tem um robô com uma câmera e um braço robótico. A câmera vê um
objeto e você quer que o braço pegue esse objeto. A câmera fornece a posição do
objeto em seu próprio frame de coordenadas, mas para mover o braço para a
posição correta, você precisa transformar essas coordenadas para o frame de
coordenadas do braço. O TF2 permite que você faça essa transformação de forma
precisa, mesmo que a câmera e o braço estejam se
movendo.

**Resumo do tutorial acima**
1. **Instalação do Demo**: Instruções para instalar o pacote do tutorial e suas
dependências.
2. **Execução do Demo**: Passos para rodar o demo, incluindo comandos para
iniciar o turtlesim e controlar a tartaruga central usando as setas do teclado.
Uma das tartarugas seguirá continuamente a
outra.
3. **Explicação do que está Acontecendo**: O demo utiliza a biblioteca tf2 para
criar três frames de coordenadas (world, turtle1, turtle2) e demonstra como um
broadcaster tf2 pode publicar os frames de coordenadas, enquanto um listener tf2
calcula a diferença entre os frames das tartarugas e move uma para seguir a
outra.
4. **Ferramentas tf2**: Introdução a ferramentas como `view_frames` e `tf2_echo`
para visualizar e entender o que está acontecendo nos bastidores com os frames e
transformações do
tf2.
5. **RViz e TF2**: Uso do RViz, uma ferramenta de visualização, para examinar os
frames do tf2 em
ação.

## 2. Broadcasters

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

[Criando um Broadcaster
](https://docs.ros.org/en/humble/Tutorials/Intermediate/Tf2/Writing-A-Tf2-Static-Broadcaster-Py.html)

</Admonition>

Um **broadcaster** no contexto do TF2 (Transform Library 2) no ROS (Robot
Operating System) é uma entidade que publica transformações entre frames de
coordenadas. Estas transformações podem ser dinâmicas (mudando ao longo do
tempo, como um robô em movimento) ou estáticas (fixas, como a relação entre um
sensor e a base de um robô). O broadcaster é responsável por fornecer
informações sobre como um frame de coordenadas se relaciona com outro em um
determinado momento.

Agora, vamos ao tutorial do link fornecido:

**Resumo do tutorial acima**
1. **Contexto**: Publicar transformações estáticas é útil para definir a relação
entre a base de um robô e seus sensores ou partes não móveis. Por exemplo, é
mais fácil raciocinar sobre medidas de um scanner a laser em um frame no centro
do
scanner.
2. **Pré-requisitos**: O tutorial assume que você já sabe como criar um espaço
de trabalho e um pacote no
ROS.
3. **Tarefas**:
   - **Criar um pacote**: Um pacote chamado `learning_tf2_py` é criado, que será
usado neste tutorial e nos seguintes.
   - **Escrever o nó broadcaster estático**: O código é fornecido para criar um
broadcaster estático que publica a transformação de um frame "world" para um
frame de tartaruga estática.
   - **Construção**: Antes de construir o pacote, é uma boa prática verificar as
dependências ausentes. Depois, o pacote é construído.
   - **Execução**: O nó `static_turtle_tf2_broadcaster` é executado, definindo
uma pose de tartaruga que flutua 1 metro acima do solo.
4. **A maneira correta de publicar transformações estáticas**: Embora o tutorial
mostre como usar o `StaticTransformBroadcaster` para publicar transformações
estáticas, na prática, você deve usar a ferramenta `static_transform_publisher`
fornecida pelo `tf2_ros`. Esta ferramenta pode ser usada como uma ferramenta de
linha de comando ou como um nó em arquivos de
lançamento.

## 3. Listeners 
