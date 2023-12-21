---
title: Sistema de Text-to-Speech
sidebar_position: 2
---

# Documentação referente ao Text to Speech do Bot Telegram

## Introdução
Este documento fornece uma visão do sistema de reconhecimento de fala (Speech to Text) e síntese de fala (Text to Speech) integrado a um bot do Telegram. O sistema permite que usuários interajam com o bot por meio de mensagens de voz, convertendo-as em texto para processamento e respondendo por meio de mensagens de voz geradas. O Speech to Text foi detalhado na sprint 4 ([Link para o documento da sprint 4](https://2023m8t2-inteli.github.io/grupo2/sprint4/Text-to-Speech/)), e agora este documento apresenta uma visão aprofundada, incluindo a integração do Text to Speech.

## Justificativa do uso no Projeto
O uso combinado de Speech to Text e Text to Speech oferece benefícios adicionais:
- **Comunicação Bidirecional:** Permite que o bot compreenda mensagens de voz dos usuários e responda também em formato de voz.
- **Experiência do Usuário Aprimorada:** Torna a interação mais natural, proporcionando uma experiência mais dinâmica.
- **Ampliação da Acessibilidade:** Oferece uma solução inclusiva, permitindo que usuários interajam com o bot de maneira acessível.

## Componentes do Sistema


### TextToSpeechNode
Adicionado ao sistema, este nó é dedicado à síntese de fala, transformando texto em áudio.

#### Funcionalidades Detalhadas
- **Síntese de Fala Avançada:** Utiliza tecnologias de Text to Speech para gerar áudio de alta qualidade a partir do texto recebido.

## Fluxo de Processamento Detalhado
1. **Recepção de Mensagem de Voz:** Usuário envia uma mensagem de voz para o bot no Telegram.
2. **Salvamento e Roteamento:** `TelegramNode` salva a mensagem de voz e envia o caminho do arquivo para `VoiceProcessingNode`.
3. **Transcrição de Voz:** `VoiceProcessingNode` transcreve a mensagem de voz em texto.
4. **Processamento de Texto:** O texto transcrito é processado para entender a intenção do usuário.
5. **Geração de Resposta:** Uma resposta em texto é gerada, e `TextToSpeechNode` a converte em áudio.
6. **Resposta ao Usuário:** O áudio gerado é enviado de volta ao usuário através do `TelegramNode`.

## Conclusão
A integração do Text to Speech ao sistema existente proporciona uma comunicação bidirecional eficaz, enriquecendo a experiência do usuário no bot do Telegram. Esse aprimoramento torna a interação mais intuitiva e acessível, consolidando a eficácia do sistema no contexto da comunicação por voz.