---
title: Sistema de Logs 
sidebar_position: 4
---

# Sistema de Logs

Um dos requisitos da sprint foi a  criação de um sistema de logs, ou seja registrar as mais diversas interações que o usúario tem com o sistema e respostas do sistema. O objetivo dos logs é ter um histórico das interações e a hora em que tais inputs e outputs foram recebidos. 

O sistema de logs foi pensado em ser um nó ROS da mesma forma que os inputs, LLM e telegram também sâo. Isso cria uma solução desacoplada e mais completa em todos os aspectos. 
Para conferir o resultado dos logs é necessário entrar na pasta de resource e entrar no arquivo log.txt 
O caminho para acessar os logs é o seguinte : 
<code>src/workspace/src/central/resource</code>

Atualmente, são regristadas as seguintes informações :

- O LLM recebeu determinada mensagem do usúario.
- O LLM retornou determinada mensagem ao usúario.
- O Telegram recebeu determinada mensagem do usúario.
- O Telegram retornou determinada mensagem ao usúario.


Para registrar os logs é necessária  a execução dos pacotes correspondentes ao script de input do usuário, LLM, logs e Telegram. Os comandos do usuário podem ser enviados de duas maneiras distintas: pelo terminal ou pelo chatbot. Isto é, é possível interagir com o modelo de linguagem por meio de dois diferentes pacotes do nodo central do  workspace ROS: o pacote <code>input</code> e o pacote <code>telegram</code>. Enquanto o Telegram configura a interface escolhida para o chatbot, permitindo uma interação fluida com o usuário, o pacote de input representa uma interface mais simples, via terminal, ideal para realizarmos as validações e testes necessários.
Então,para gravar todos os logs, é necessário executar os seguintes pacotes de forma paralela <code>input</code>,<code>llm</code>,<code>telegram</code> e <code>logs</code>.



**1.** Abrir o workspace ROS no terminal

```bash
cd grupo2/src/workspace
```

**2.** Construir os pacotes localmente

```bash
colcon build
```

**3.** Executar o comando de setup local

```bash
source install/local_setup.zsh
```

**4.** Executar o pacote <code>input</code>, para enviar os comandos ao LLM

```bash
ros2 run central input
```

**5.** Executar o pacote <code>llm</code>, para receber os comandos e retornar as respostas do modelo

```bash
ros2 run central llm
```
**6.** Executar o pacote <code>telegram</code>, para receber os comandos e retornar as respostas do modelo via telegram

```bash
ros2 run central telegram
```
**7.** Executar o pacote <code>logs</code>, para criar os logs

```bash
ros2 run central logs
```

Após a interação com os nós como foi explicado na seção de descrição dos testes é possível conferir o resultado dos logs no seguinte arquivo. 

```bash
cd 'src/workspace/src/logs.txt'

```

Um exemplo de como os logs funcionam é o seguinte : 

```
LLM recebeu: "OLá como você vai ? " | 2023-11-29 17:22:51.351542

LLM retornou: "Desculpe, não entendi sua pergunta. Por favor, faça uma pergunta relacionada às ferramentas listadas no arquivo de contexto." | 2023-11-29 17:22:57.703547

LLM recebeu: "Olá, seria possível pegar uma tela LED ? " | 2023-11-29 17:23:29.259778

LLM retornou: "[(x:250), (y:250)]" | 2023-11-29 17:23:31.859764

Telegram recebeu mensagem do tipo: "text" | 2023-11-29 17:25:46.617703

Telegram recebeu mensagem: "gostaria de uma correia em v" | 2023-11-29 17:25:46.619345

Telegram enviou para a LLM: "gostaria de uma correia em v" | 2023-11-29 17:25:46.620673

LLM recebeu: "gostaria de uma correia em v" | 2023-11-29 17:25:46.621908

LLM retornou: "[(x:100), (y:50)]" | 2023-11-29 17:25:48.655218

Telegram recebeu da LLM: "[(x:100), (y:50)]" | 2023-11-29 17:25:48.656767

Mensagem enviada via bot do telegram: "[(x:100), (y:50)]" | 2023-11-29 17:25:48.658077

Telegram recebeu mensagem do tipo: "text" | 2023-11-29 17:26:30.662016

Telegram recebeu mensagem: "me explique onde está a tela led ?" | 2023-11-29 17:26:30.663844

Telegram enviou para a LLM: "me explique onde está a tela led ?" | 2023-11-29 17:26:30.665485

LLM recebeu: "me explique onde está a tela led ?" | 2023-11-29 17:26:30.666950

LLM retornou: "[(x:250), (y:250)]" | 2023-11-29 17:26:33.019136

Telegram recebeu da LLM: "[(x:250), (y:250)]" | 2023-11-29 17:26:33.021234

Mensagem enviada via bot do telegram: "[(x:250), (y:250)]" | 2023-11-29 17:26:33.022666

Telegram recebeu mensagem do tipo: "voice" | 2023-11-29 17:26:36.798424
```