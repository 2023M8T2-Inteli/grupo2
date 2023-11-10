# Chatbot do Telegram

## **Descrição Geral:**
O script `telegram_api.py` localizado em `/src/scripts/chatbot/telegram_api.py` foi projetado para ser a interface de comunicação entre o usuário e o sistema de autoatendimento do almoxarifado. Ele emprega um chatbot do Telegram para receber comandos de texto e para fornecer respostas automáticas que facilitam a solicitação e gerenciamento de pedidos de itens do almoxarifado.

## **Integração com o Sistema de Autoatendimento:**
- O chatbot serve como um ponto de entrada para solicitações de itens, que são posteriormente processadas pelo sistema de autoatendimento e executadas pelo robô autônomo.
- As mensagens de comando são mapeadas para ações correspondentes no sistema que guiam o robô no almoxarifado.

## **Uso e Comandos:**
- O usuário inicia uma conversa com o bot, que responde com uma mensagem de boas-vindas e apresenta opções de comandos.
- Os comandos incluem opções para fazer pedidos, verificar estoque, verificar o status de um pedido e visualizar itens disponíveis.
- A resposta para cada comando é definida dentro de funções específicas no script.

## **Razões para a Utilização do Chatbot do Telegram**

### **Acessibilidade e Conveniência:**
A escolha do chatbot do Telegram como interface de usuário foi impulsionada pela sua facilidade de acesso e uso generalizado. O Telegram é uma plataforma amplamente adotada com uma base de usuários ativa, que permite aos usuários interagir com o sistema de autoatendimento de uma maneira conveniente e familiar. A acessibilidade móvel do Telegram significa que os usuários podem fazer pedidos e consultar informações de qualquer lugar, a qualquer hora, diretamente de seus smartphones.

### **Interação Intuitiva e Experiência do Usuário:**
Os chatbots fornecem uma experiência de usuário interativa e guiada que pode simular uma conversa natural. Isso minimiza a curva de aprendizado para os usuários novos e melhora a eficiência para os usuários recorrentes. O uso de comandos e prompts claros ajuda a evitar erros de comunicação e acelera o processo de pedido.

### **Redução de Erros e Melhoria de Eficiência:**
Ao automatizar a recepção de pedidos e as respostas às consultas, o chatbot reduz a possibilidade de erros humanos. A precisão e a consistência das respostas do bot contribuem para uma melhor gestão do inventário e uma maior eficiência operacional. Isso é crucial em um ambiente onde a rapidez e a precisão são fundamentais, como no almoxarifado da AMBEV.

### **Escalabilidade e Manutenção:**
O chatbot é facilmente escalável, permitindo que mais usuários façam pedidos simultaneamente sem a necessidade de recursos adicionais de atendimento ao cliente. Manter o bot é menos oneroso em comparação com o treinamento e gerenciamento de uma equipe de atendimento ao cliente, resultando em economia de custos e em um sistema mais sustentável a longo prazo.

### **Integração e Personalização:**
A plataforma do Telegram permite uma integração fácil com sistemas existentes através de APIs e Webhooks. Isso permite uma personalização profunda do chatbot para atender às necessidades específicas do projeto. O chatbot pode ser ajustado para refletir o vocabulário e os processos do almoxarifado, criando uma experiência de usuário altamente adaptada e eficiente.

### **Dados e Análise:**
O uso do chatbot fornece a oportunidade de coletar dados sobre as interações dos usuários, que podem ser analisados para melhorar continuamente o processo de atendimento e entender melhor as necessidades dos usuários. Essa análise de dados pode levar a insights que ajudam a otimizar as operações do almoxarifado.

### **Segurança e Conformidade:**
A implementação do chatbot no Telegram também permite o controle sobre a segurança e a privacidade das comunicações. A chave da API e os dados sensíveis podem ser protegidos usando práticas recomendadas de segurança de TI. Além disso, o Telegram oferece criptografia de ponta a ponta, garantindo que a comunicação entre o usuário e o sistema seja segura e em conformidade com as políticas de privacidade da empresa.

### **Resiliência e Confiabilidade:**
O chatbot no Telegram é apoiado pela infraestrutura robusta e confiável do Telegram, que garante alta disponibilidade e desempenho consistente. Isso é essencial para garantir que o sistema de autoatendimento esteja sempre disponível para os usuários quando necessário, sem interrupções.

## **Funcionalidades do Chatbot:**
1. **Recepção de Pedidos:** Através de comandos específicos, como `/Parafuso`, o usuário pode realizar pedidos diretamente pelo chat.
2. **Fluxo de Diálogo:** O bot guia o usuário por meio de uma série de opções e comandos para facilitar o processo de pedido, verificação de estoque e acompanhamento do status de pedidos.
3. **Listagem de Itens:** O chatbot fornece uma lista de itens que podem ser solicitados e informações sobre como fazer esses pedidos.

## **Detalhes Técnicos:**
- O bot é construído usando a biblioteca `telebot`, que permite a criação de comandos e o manejo de mensagens.
- Há uma função de verificação (`verify`) que valida todas as mensagens recebidas, direcionando-as para o manipulador de mensagens adequado.
- A função `answer` é responsável por responder a todas as mensagens que não são comandos específicos, apresentando ao usuário as opções iniciais.

## **Segurança:**
- A chave da API é utilizada para autenticar o bot no serviço do Telegram. Em ambientes de produção, é recomendável que esta chave seja armazenada de forma segura e não diretamente no código.

## **Testes e Validação:**
- Testes devem ser realizados para assegurar que o bot responde corretamente aos comandos e gerencia eficientemente as interações dos usuários.
- A validação deve incluir a verificação de que o bot direciona os pedidos corretamente para o sistema de autoatendimento.

**Manutenção e Atualizações:**
- A documentação do script deve ser revisada e atualizada regularmente para refletir quaisquer alterações no funcionamento do bot.
- O monitoramento contínuo do bot é essencial para garantir a eficácia e a precisão das respostas e ações.