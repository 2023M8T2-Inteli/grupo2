---
title: Testes e Avaliação dos Requisitos
sidebar_position: 2
---

# Testes e Avaliação dos Requisitos do Sprint

Durante o sprint corrente, a equipe se dedicou a testar componentes essenciais do sistema de autoatendimento robótico para o Almoxarifado da AMBEV. Os testes realizados foram desenhados para avaliar a comunicação, mapeamento de ambiente e movimentação simples do robô, além de diferentes formatos de frontend. A seguir, apresentaremos uma análise detalhada desses testes, considerando os requisitos do projeto e discutindo a adequação dos sistemas desenvolvidos.

## Testes Realizados

### 1. Teste de Comunicação com o Robô
#### Descrição:
O teste de comunicação com o robô envolveu a conexão direta via SSH e a execução de comandos no terminal do robô. Este teste foi fundamental para validar a capacidade de controle remoto e a resposta do robô às instruções enviadas a partir de uma estação de trabalho.

#### Requisitos Atendidos:
- **Conectividade:** Verificou-se que o robô pode ser acessado remotamente, um requisito crítico para operações autônomas e monitoramento.
- **Controle e Comando:** A execução de comandos no terminal confirmou que o robô responde de maneira adequada às instruções, alinhando-se com as expectativas de controle do sistema.

#### Discussão e Melhorias:
A comunicação via SSH é robusta, porém, para operações em tempo real e em escala, a equipe pode explorar interfaces de comunicação mais avançadas, como APIs dedicadas ou conexões de rede seguras e resilientes.

### 2. Teste de Mapeamento de Ambiente
#### Descrição:
Utilizando a package do ROS Cartographer, a equipe construiu um modelo de ambiente fechado para mapear o espaço. Esse mapeamento é crucial para permitir a navegação autônoma futura usando o Nav2, direcionando o robô para pontos específicos dentro do ambiente.

#### Requisitos Atendidos:
- **Mapeamento e Navegação:** O mapeamento bem-sucedido do ambiente é um passo crucial para a navegação autônoma, satisfazendo os requisitos de autoatendimento do projeto.
- **Integração de Sistema:** A utilização do ROS Cartographer está alinhada com a arquitetura do sistema proposto, garantindo compatibilidade e integração.

#### Discussão e Melhorias:
O mapeamento atual foi realizado em um ambiente controlado e pequeno. Para avançar, recomenda-se expandir os testes para ambientes maiores e mais complexos, que simulem as condições reais do almoxarifado da AMBEV. Também será necessário otimizar o mapeamento para lidar com mudanças dinâmicas no ambiente.

### 3. Teste de Movimentação Simples
#### Descrição:
O robô foi submetido a um teste de movimentação simples, usando a package Teleop do ROS, que transforma um teclado em um dispositivo de entrada para movimentação, semelhante a um joystick.

#### Requisitos Atendidos:
- **Controle de Movimentação:** O robô demonstrou capacidade de se movimentar em resposta a comandos diretos, um requisito para a funcionalidade de autoatendimento.
- **Interatividade:** O uso de Teleop para controlar o robô fornece uma base para futuras implementações de controle mais intuitivas e interativas.

#### Discussão e Melhorias:
Enquanto a movimentação controlada por teclado é eficaz para testes iniciais, ela não representa a interação final esperada para o robô autônomo. Deve-se trabalhar na integração dos sistemas de navegação autônoma para permitir que o robô execute movimentos complexos e navegue de forma independente dentro do almoxarifado.

Além dos testes de comunicação, mapeamento e movimentação, a equipe também conduziu testes focados na interação do usuário com o sistema através de dois frontends distintos: um terminal de comando e um chatbot do Telegram. Estes testes são essenciais para assegurar que os frontends atendam às necessidades dos usuários, mantendo a funcionalidade e a usabilidade em consonância com os objetivos do projeto.

### 4. Teste de Script de Navegação
#### Descrição:
Este teste submeteu o robô a um procedimento de navegação com um Script "nav_waypoints" que define pontos iniciais no mapa gerado pelo Cartographer e o manda seguir para pontos definidos no mapa previamente salvo e carregado com o pacote Navigation2.

#### Requisitos Atendidos:
- **Controle de Movimentação:** O script desenvolvido permitiu que o robô respondesse de maneira eficaz a comandos diretos, validando a capacidade de movimentação essencial para a funcionalidade de autoatendimento.
- **Interatividade:** A utilização da package Navigation2 para guiar o robô estabeleceu uma base sólida para futuras implementações de controle mais intuitivas e interativas.

#### Discussão e Melhorias:
Embora a movimentação controlada por teclado tenha se mostrado eficaz para testes iniciais, é importante ressaltar que essa abordagem não representa a interação final esperada para um robô autônomo. O próximo passo deve incluir o desenvolvimento e integração de sistemas de navegação autônoma como o teste realizado com o Script de navegação propõe. Essa evolução possibilitará ao robô executar movimentos mais complexos e navegar de forma independente dentro do ambiente do almoxarifado.


## Testes Adicionais Realizados

### 5. Teste de Chatbot com Terminal de Comando
#### Descrição:
Este teste envolveu o uso de um script de linha de comando para simular a interação do usuário com o sistema de autoatendimento, como um meio de demonstrar a funcionalidade do chatbot sem a necessidade de uma interface gráfica.

#### Requisitos Atendidos:
- **Simulação de Interface de Usuário:** O teste confirmou que os usuários podem interagir com o sistema através de comandos de texto simples, validando a funcionalidade do chatbot em um ambiente controlado.
- **Feedback e Resposta do Sistema:** O sistema forneceu respostas adequadas aos comandos do usuário, o que é crucial para garantir uma experiência do usuário positiva.

#### Discussão e Melhorias:
Embora o terminal de comando ofereça um meio eficaz para demonstrações e testes rápidos, ele não reflete a interface final que será utilizada pelos operadores do almoxarifado. Sugerimos o desenvolvimento de uma interface mais amigável, que possa simular a experiência completa do usuário final, incluindo GUIs ou integração com sistemas existentes para testes mais representativos.

### 6. Teste de Chatbot com Telegram
#### Descrição:
O chatbot do Telegram foi testado para validar sua funcionalidade em um ambiente realista de mensagens. Foi utilizado para processar solicitações de usuários, verificar estoques e fornecer atualizações de status de pedidos.

#### Requisitos Atendidos:
- **Interatividade e Usabilidade:** O chatbot funcionou conforme esperado, oferecendo uma interface interativa e fácil de usar para os usuários finais.
- **Integração com o Sistema de Autoatendimento:** O bot demonstrou ser capaz de se integrar efetivamente ao sistema de autoatendimento, facilitando a realização de tarefas essenciais.

#### Discussão e Melhorias:
O teste mostrou que o chatbot do Telegram é uma ferramenta robusta para o frontend do usuário. No entanto, é importante considerar a implementação de uma análise mais profunda de linguagem natural para aprimorar a compreensão e o processamento das solicitações dos usuários. Além disso, a inclusão de respostas automáticas mais dinâmicas e personalizadas pode melhorar ainda mais a experiência do usuário.


## Conclusão e Próximos Passos

Os testes realizados demonstram progressos significativos em direção aos requisitos do projeto, porém, também destacam áreas que necessitam de desenvolvimento adicional. A comunicação, o mapeamento e a movimentação do robô são fundamentais para a operação do sistema de autoatendimento, e cada um desses componentes precisa ser refinado para assegurar que o robô opere de maneira eficiente, segura e autônoma no ambiente de trabalho real da AMBEV.

A equipe deve agora focar em:


- Desenvolver uma estratégia de comunicação mais robusta para operações em tempo real.
- Ampliar os testes de mapeamento para ambientes que reflitam com maior precisão o espaço do almoxarifado.
- Integrar sistemas de navegação autônoma para avançar além da movimentação manual simples.
- Refinar a interface do usuário do terminal de comando para torná-la mais amigável e representativa do ambiente de uso final.
- Expandir as capacidades do chatbot do Telegram com processamento de linguagem natural avançado e respostas automatizadas personalizadas.
- Continuar a integração dos testes com o desenvolvimento contínuo do sistema de autoatendimento, assegurando que todos os componentes funcionem harmoniosamente.

Este processo contínuo de testes, avaliação e melhoria garantirá que o sistema desenvolvido não só atenda, mas exceda os requisitos do projeto, resultando em uma solução de autoatendimento eficaz para o almoxarifado da AMBEV.