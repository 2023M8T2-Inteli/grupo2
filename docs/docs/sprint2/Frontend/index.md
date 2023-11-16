---
title: Frontend
sidebar_position: 4
---

# Frontend

Durante a fase atual de desenvolvimento do projeto de Robô de Autoatendimento do Almoxarifado da AMBEV, nossa equipe focou em criar uma experiência de usuário eficiente e adaptável. Compreendendo a diversidade de cenários de uso e a importância de uma interação intuitiva, desenvolvemos dois frontends distintos: um para fins de demonstração e outro como uma solução completa de interação com o usuário.

O primeiro frontend é um script de linha de comando, command_line.py, que serve como uma ferramenta de demonstração rápida e eficaz. Projetado para ser executado em um terminal de comando, este frontend permite aos desenvolvedores e stakeholders testarem e demonstrarem as funcionalidades do sistema de autoatendimento em um ambiente controlado. Ele oferece uma maneira simplificada de simular a interação do usuário com o robô de autoatendimento, ideal para apresentações e validação rápida de conceitos.

O segundo frontend é um chatbot interativo hospedado na plataforma do Telegram. Utilizando o script telegram_api.py, este frontend avançado oferece uma interface rica e acessível que permite aos usuários finais fazerem pedidos, consultarem o estoque e o status dos pedidos, e visualizarem itens disponíveis através de uma aplicação de mensagens popular e de fácil uso. Este bot não só eleva a experiência do usuário, mas também se integra perfeitamente com o fluxo de trabalho do almoxarifado, garantindo uma transição suave das requisições para as ações executadas pelo robô autônomo.

Ambos os frontends foram criados com o intuito de atender às diferentes necessidades do projeto. Enquanto o frontend de linha de comando almeja simplificar as demonstrações e o teste de funcionalidades, o chatbot do Telegram é a ponte entre o sistema de autoatendimento e os usuários, proporcionando uma solução robusta e pronta para o uso no dia a dia do almoxarifado. A seguir, você encontrará a documentação detalhada de ambos os frontends, cada um com suas características, usos recomendados, e informações técnicas.

## **Frontend de Linha de Comando**

### **Descrição Geral:**
O `command_line.py` é um frontend baseado em terminal que permite a demonstração do sistema de autoatendimento através de uma interface de linha de comando. Destina-se a simular a experiência do usuário ao interagir com o sistema de autoatendimento, fornecendo um meio direto e simplificado para fazer pedidos de itens do almoxarifado.

### **Funcionalidades:**
- **Simulação de Pedidos:** Usuários podem solicitar itens comandando diretamente no terminal. Os itens disponíveis são parafusos, chaves de fenda e pregos.
- **Feedback Imediato:** Após a inserção do pedido, o script identifica a intenção e fornece um retorno textual, simulando a trajetória que o robô executará para buscar o item.

### **Uso:**
Ao executar o script, os usuários são recebidos com uma lista de itens disponíveis. Eles inserem o item desejado e recebem uma confirmação textual que simula a ação do robô de autoatendimento.

### **Detalhes Técnicos:**
- Utiliza expressões regulares para identificar a intenção do usuário com base no comando inserido.
- Associa cada intenção reconhecida a uma função correspondente que retorna a ação simulada do robô.

### **Testes e Validação:**
- A precisão do mapeamento das intenções e as respostas fornecidas devem ser rigorosamente testadas.
- Esta interface é principalmente para fins de demonstração e testes conceituais rápidos.

## **Chatbot do Telegram**

### **Descrição Geral:**
O script `telegram_api.py` localizado em `/src/scripts/chatbot/telegram_api.py` é um frontend interativo que emprega um chatbot do Telegram. Ele foi projetado para facilitar a comunicação entre o usuário e o sistema de autoatendimento do almoxarifado, permitindo solicitações de itens e gerenciamento de pedidos através de comandos de texto.

### **Integração com o Sistema de Autoatendimento:**
- O chatbot atua como ponto de entrada para as solicitações de itens, que são processadas pelo sistema e executadas pelo robô autônomo.
- Comandos específicos são interpretados pelo bot e mapeados para ações no sistema que direcionam o robô no almoxarifado.

### **Uso e Comandos:**
- O usuário inicia uma conversa com o bot que oferece uma saudação inicial e uma lista de comandos disponíveis.
- Os comandos permitem ao usuário fazer pedidos, verificar o estoque, consultar o status do pedido e visualizar a lista de itens disponíveis.
- Cada comando é processado por funções definidas no script que geram respostas adequadas.

### **Razões para a Utilização do Chatbot do Telegram:**
- **Acessibilidade e Conveniência:** A plataforma é amplamente utilizada e familiar aos usuários, proporcionando acesso fácil e interação direta a partir de dispositivos móveis.
- **Interação Intuitiva e Experiência do Usuário:** A interface do chatbot simula uma conversa, facilitando o uso e melhorando a eficiência.
- **Redução de Erros e Melhoria de Eficiência:** Automatiza o processo de pedidos e respostas, diminuindo a possibilidade de erros humanos e melhorando a gestão de inventário.
- **Escalabilidade e Manutenção:** Permite atender a um número maior de usuários simultaneamente com menos custos de manutenção em comparação com um atendimento humano.
- **Integração e Personalização:** O bot pode ser personalizado para se integrar com sistemas existentes e adaptado para refletir processos específicos do negócio.
- **Dados e Análise:** Fornece dados valiosos sobre as interações dos usuários que podem ser analisados para otimizar as operações.
- **Segurança e Conformidade:** Utiliza práticas de segurança robustas para proteger a chave da API e dados dos usuários, garantindo comunicações seguras.
- **Resiliência e Confiabilidade:** A infraestrutura do Telegram garante a disponibilidade e a consistência do serviço.

### **Funcionalidades do Chatbot:**
- **Recepção de Pedidos:** Os usuários podem realizar pedidos utilizando comandos específicos como `/Parafuso

`.
- **Fluxo de Diálogo:** O bot orienta o usuário através de um fluxo estruturado de comandos para completar o processo de pedido.
- **Listagem de Itens:** Uma função do bot proporciona uma visão geral dos itens disponíveis para pedido.

### **Detalhes Técnicos:**
- O bot é desenvolvido utilizando a biblioteca `telebot`, que facilita a criação de um sistema de comando e resposta.
- Uma função de verificação assegura que todas as mensagens sejam validadas e direcionadas apropriadamente.
- A função `answer` responde a todas as mensagens não associadas a comandos, introduzindo as opções ao usuário.

### **Segurança:**
- A chave da API é crítica para a autenticação do serviço do bot no Telegram e deve ser protegida adequadamente.

### **Testes e Validação:**
- Testes são realizados para confirmar que o bot responde corretamente aos comandos e gerencia as interações de forma eficaz.
- A validação inclui a correta direção dos pedidos para o sistema de autoatendimento.

**Manutenção e Atualizações:**
- A documentação deve ser mantida atualizada com quaisquer mudanças no bot.
- Monitoramento contínuo é essencial para a eficácia e precisão das respostas e ações do bot.
