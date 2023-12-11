---
title: Como executar o projeto V2
sidebar_position: 5
---
import Admonition from '@theme/Admonition';

# Como executar o projeto

Para começar a executar o projeto, é necessário ter entendimento sobre a estrutura de pastas.

```bash
- docs
- src
    - maps
        - testes
    - scripts
        - chatbot
        - testes_navigation
    - workspace
        -  src
            - central
                - launch
                    - central_launch.py
                - central
                    - input_node.py
                    - llm_node.py
                    - logger_node.py
                    - regex_node.py
                    - telegram_node.py
                    - voice_processing_node.py             
            - llm
            - navigation
                - launch
                    - navigation_launch.py
                - navigation
                    - navigation.py

```

Explicando um pouco mais, a pasta `docs` contém toda a documentação do projeto, enquanto a pasta `src` contém os códigos do projeto.

Dentro da pasta `src`, temos as pastas `maps`, que contêm o mapeamento do ambiente simulado e os mapas utilizados para os testes.

Na pasta `scripts`, estão a primeira versão das funcionalidades do sistema, ou seja, o chatbot e os testes de navegação.

Descendo um pouco mais, temos o `workspace`. O que é um workspace e para que ele serve?
[Clique aqui para saber mais!!!](hhttps://rmnicola.github.io/m8-ec-encontros/sprint1/encontro3/roslaunch)

Agora, sabendo um pouco mais sobre como um workspace funciona, vamos entender a estrutura de pastas dentro do workspace.

Dentro da pasta `src`, encontramos as pastas `central` e `navigation`. Elas representam 2 pacotes do ROS, sendo cada uma delas importante no projeto.

A pasta `central` é responsável por receber as informações do chatbot e enviar para os outros pacotes, além de receber informações dos outros pacotes e enviar para o chatbot.

A pasta `navigation` é responsável pela movimentação do robô e pelo envio das informações de movimentação para a pasta `central`.

**Ok, entendi como as coisas funcionam, mas como eu executo o projeto?**

## Executando o projeto

O primeiro passso, é ter o ROS instalado. Para isso, siga os passos apenas [clicando aqui!!](https://rmnicola.github.io/m8-ec-encontros/sprint1/encontro1/setup-ubuntu)

Perfeito, configurou tudo direitinho? Agora vamos para o próximo passo.

Precisamos fazer so mais uma configuração simples, para isso, digite esse comando:
    
```bash
   echo "export OPENAI_API_KEY='Sua APIKey do chatgpt'" >> ~/.bashrc
```
   
```bash
   echo "export OPENAI_ORGANIZATION_ID='A chave da sua organização da openai'" >> ~/.bashrc
```
```bash
   echo "export TELEGRAM_API_KEY='Sua chave API do telegram'" >> ~/.bashrc
```

Esses comandos são para salvar as chaves da API e da organização da OpenAI, que são necessárias para o funcionamento do chatbot.

Agora, vamos para o próximo passo.

Para executar o projeto, é necessário ter o ROS instalado.

Agora que você já tem o ROS instalado, vamos executar o projeto.

Primeiramente, abra o terminal e digite o seguinte comando:

```bash
cd src/workspace/src
```

Esse comando é usado para entrar na pasta 'src' do workspace.

Agora, execute o seguinte comando:

```bash
colcon build
source install/setup.bash
```
Agora que temos tudo instalado, vamos para a terceira parte, que é essencial.

Estamos falando de um robô, certo? Mas onde está o robô? Para executar o simulador dele, use o seguinte comando:

```bash
ros2 launch nav2_bringup tb3_simulation_launch.py slam:=False
```
**IMPORTANTE: Certifique-se de executar este comando no robô. Caso precise de ajuda para fazer isso, podemos criar um tópico explicando como proceder.**

Agora que o robô está em execução, vamos aos comandos de navegação. Na ultima sprint, nosso sistema precisava ser rodado manualente, Nó por Nó, mas agora, com o uso dos `launchs`, podemos executar tudo de uma vez só.

```bash
ros2 launch central central_launch.py
```

e em outro terminal:

```bash
ros2 launch navigation navigation_launch.py
```

O primeiro comando roda o pacote `central`, enquanto o segundo roda o pacote `navigation`.

Com o uso do launch, podemos executar todos os nós de uma vez só, mas, caso queira executar os nós separadamente, você pode executar os seguintes comandos:

```bash
ros2 run [nome_do_pacote][node_do_nó]
```
Faça isso para cada nó para os pacotes `central` e `navigation`.

**IMPORTANTE**
Ao criar o launch navegation.launch.py, um problema que não conseguimos resolver ainda pode ser encontrado. O mapa não é carregado corretamente, sendo necessário rodar esses 2 comandos:

```bash
cd src\workspace\src\navigation\navigation\launch
```

```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=False map:=maps/circuito.yaml
```
e por ultimo:

```bash
ros2 run navigation navigation
```
Estes comandos são necessários para o funcionamento da navegação do robô caso o launch não funcione corretamente.

**Lembre-se, é necessário executar o comando de inicialização do robô (caso ainda não tenha feito, é o primeiro comando mencionado).**

<Admonition 
    type="info" 
    icon=<img src={require('/gifs/loading.gif').default} width='20vw' />
    title="Work in progress">
</Admonition>

Para facilitar a execução do projeto, vamos criar um mecanismo para executar todos os comandos de uma vez só. Para isso, crie um arquivo chamado 'launch' dentro da pasta 'src/workspace/src/[nome do pacote]>'. Estamos trabalhando nisso e em breve traremos mais informações.
