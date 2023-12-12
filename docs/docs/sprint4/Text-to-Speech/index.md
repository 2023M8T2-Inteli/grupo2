---
title: Text-to-Speech
sidebar_position: 2
---

## Text-to-Speech

Durante a quarta sprint do ciclo de desenvolvimento, fizemos a implementação do sistema text-to-speech, fazendo uso da API fornecida pela OpenAI. Nesse contexto, o processo inicia-se com a recepção da requisição recebida do sistema de resposta. A origem dessa demanda é o nó específico do Telegram, por meio do qual os usuários interagem com nossa aplicação.

Assim que a solicitação de resposta chega, ela é encaminhada para a API da OpenAI. Essa interação é crucial, pois é nesse ponto que o conteúdo textual é submetido ao mecanismo de conversão em áudio proporcionado pela OpenAI. A transformação do texto em um formato sonoro ocorre de maneira dinâmica.

Ao adotar essa abordagem, nosso sistema adquire a capacidade de fornecer respostas auditivas, agregando uma camada adicional de interatividade e acessibilidade à experiência do usuário. 

Além disso, a integração da tecnologia text-to-speech da OpenAI amplia consideravelmente o escopo de aplicação do nosso sistema, permitindo-nos atender a uma variedade mais ampla de usuários e casos de uso. A utilização desta API não só enriquece a experiência do usuário, mas também demonstra nosso compromisso contínuo com a entrega da solução.
