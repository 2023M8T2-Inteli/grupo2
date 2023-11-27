---
title: Arquitetura do sistema
sidebar_position: 1
---
# ARQUITETURA DO SISTEMA 

![Arquitetura do sistema](../../assets/arquitetura_do_sistema.png)

## Visão Geral
Este sistema utiliza a plataforma ROS para automatizar a busca e identificação de itens em almoxarifados. O objetivo é permitir que o robô interprete e execute comandos relacionados à busca de peças em um ambiente, permitindo que os usuários enviem comandos de texto ou voz para localizar itens com a ajuda de um robô autônomo.

### Frontend
- **Telegram**: Interface de usuário para enviar comandos de texto ou voz.
- **Teclado**: Permite a entrada de comandos de texto.
- **Microfone**: Permite a entrada de comandos de voz, que são convertidos em texto.

### Processamento de Comandos
- **Nó do Regex**: Processa expressões regulares para identificar intenções do usuário, como pesquisa de um item ou requisição de informações sobre peças.
- **Nó do LLM (Large Language Model)**: Identifica a intenção do usuário e acessa informações relevantes para a tarefa.

### Conversão de Voz
- **Nó de Voz (Whisper)**: Converte mensagens de voz em texto para processamento.

### Robô Autônomo
- **Interface Física**: Equipado com Sensor LiDAR para navegação e Tela LCD para feedback.
- **Operação**: Executa ações com base nos comandos processados e informações do sistema.

### Integração de Dados
- **PDF de Peças**: Contém informações sobre peças, quantidade em estoque e localização para contextualização da conversa.

## Fluxo de Dados
1. O usuário envia um comando pelo Telegram (texto ou voz).
2. O nó de LLM processa o comando e envia para o nó de Regex.
2. O nó de REGEX identifica a intenção do usuário.
3. O robô autônomo é direcionado para localizar e identificar o item solicitado. 
4. O feedback é apresentado ao usuário através do Telegram e da Tela LCD do robô.

## Tecnologias e Ferramentas
- **ROS (Robot Operating System)**: Framework de robótica que gerencia a comunicação entre os nós.
- **Telegram API**: Interface para comunicação com o usuário.
- **Whisper**: Tecnologia de conversão de voz para texto.
- **Sensor LiDAR**: Para mapeamento e navegação do robô.
