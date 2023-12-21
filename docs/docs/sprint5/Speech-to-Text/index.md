---
title: Sistema de Speech-to-Text
sidebar_position: 1
---

# Documentação Avançada do Sistema de Speech to Text do Bot Telegram

## Introdução
Este documento apresenta uma visão detalhada do sistema de reconhecimento de fala (Speech to Text) integrado a um bot do Telegram. O sistema permite que usuários interajam com o bot por meio de mensagens de voz, que são convertidas em texto para processamento e resposta. Na sprint 4 já foi detalhado o funcionamento do sistema de Speech to Text ([Link para o documento da sprint 4](https://2023m8t2-inteli.github.io/grupo2/sprint4/Speech-to-Text/)), mas este documento apresenta uma visão mais aprofundada do sistema, incluindo detalhes técnicos e de implementação.

## Justificativa do Projeto
O uso de um sistema de Speech to Text em um bot do Telegram tem várias vantagens de negócios e usabilidade:
- **Acessibilidade:** Permite a interação com o bot por usuários que preferem falar ao invés de digitar.
- **Conveniência:** Facilita o uso em situações onde digitar pode ser impraticável.
- **Engajamento do Usuário:** Aumenta a interatividade e o engajamento do usuário com o bot.

## Componentes do Sistema

### TelegramNode
Este nó atua como a interface principal com o usuário, gerenciando a recepção e o envio de mensagens no Telegram.

#### Funcionalidades Detalhadas
- **Gestão de Estado de Chat:** Mantém um registro do estado atual de cada chat, permitindo um fluxo de conversa contextual.
- **Processamento de Tipos de Mensagens:** Diferencia e processa mensagens de texto e voz de forma adequada.
- **Interação Dinâmica:** Responde a consultas do usuário com informações relevantes e orientações.

### VoiceProcessingNode
Responsável por converter mensagens de voz em texto, este nó é crucial para a acessibilidade e a flexibilidade do sistema.

#### Funcionalidades Detalhadas
- **Recepção e Armazenamento de Voz:** Salva arquivos de voz recebidos e os prepara para transcrição.
- **Transcrição de Voz:** Utiliza tecnologia avançada de reconhecimento de fala para converter voz em texto.
- **Gestão de Arquivos de Áudio:** Remove arquivos de voz após a transcrição para gerenciamento eficiente do armazenamento.

## Fluxo de Processamento Detalhado
1. **Recepção de Mensagem de Voz:** Usuário envia uma mensagem de voz para o bot no Telegram.
2. **Salvamento e Roteamento:** `TelegramNode` salva a mensagem de voz e envia o caminho do arquivo para `VoiceProcessingNode`.
3. **Transcrição de Voz:** `VoiceProcessingNode` transcreve a mensagem de voz em texto.
4. **Processamento de Texto:** O texto transcrito é processado para entender a intenção do usuário.
5. **Resposta ao Usuário:** Uma resposta é gerada e enviada de volta ao usuário através do `TelegramNode`.

## Conclusão
O sistema de Speech to Text integrado ao bot do Telegram oferece uma solução interativa e acessível para a comunicação entre usuários e o bot, abrindo caminho para uma maior eficiência e engajamento do usuário.