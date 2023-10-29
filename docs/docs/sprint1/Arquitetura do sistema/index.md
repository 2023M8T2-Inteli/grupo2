# ARQUITETURA DO SISTEMA 

O sistema consiste em uma arquitetura baseada em ROS que integra um Nodo Central com módulos de processamento de voz e texto a um Robô Autônomo. O objetivo é permitir que o robô interprete e execute comandos relacionados à busca de peças em um ambiente, utilizando tanto entradas de teclado quanto comandos de voz.

![Arquitetura do sistema](../../assets/arquitetura.png)

## Componentes:

1. **Nodo Central**:
    - **Script identificador de palavras-chaves**: Este script é responsável por determinar a natureza do comando, seja ele simples ou complexo. Os comandos podem ser inseridos através do teclado ou por voz.

    - **Buscador de coordenadas da peça**: Depois que um comando é interpretado, este módulo busca no banco de dados a localização exata da peça solicitada.

2. **Nodo de voz**:
    - **Conversão de voz para texto (Speech-to-Text)**: Este módulo, utilizando o Whisper, é responsável por converter os comandos de voz do usuário em texto para que possam ser processados pelo sistema.

3. **Nodo de LLM**:
    - **LLM de extração do código da peça**: Após a identificação do comando, se for complexo, o LLM (representado pelo Llama 2) é usado para extrair informações mais detalhadas do texto fornecido, como o código específico de uma peça.

4. **Robô Autônomo**:
    - **Interface física**: Constitui o corpo do robô, permitindo que ele se mova pelo ambiente.
    
    - **Sensor Lidar**: Sensor responsável pelo mapeamento do ambiente e detecção de obstáculos.
    
    - **Tela LCD**: Fornece feedback visual ao usuário, mostrando informações como status atual, comandos recebidos, entre outros.

## Fluxo:

1. O usuário insere um comando através do **teclado** ou **microfone**.
   
2. O comando é enviado ao Nodo Central onde é determinado se é um comando **simples** ou **complexo**.

3. Se o comando for **simples**, o **Buscador de coordenadas da peça** procura diretamente no banco de dados a localização da peça.

4. Se o comando for **complexo**, o **Nodo de LLM** processa o texto para extrair informações detalhadas, como o código da peça.

5. Uma vez obtida a localização da peça, as coordenadas são enviadas ao **Robô Autônomo** através do **ROS**.

6. O Robô Autônomo se move para a localização fornecida e realiza a tarefa designada.

# REQUISITOS FUNCIONAIS E NÃO FUNCIONAIS

Para garantir que o projeto atende às necessidades do cliente especificada em entrevista de levantamento de requisitos em sala de aula, os requisitos foram divisidos em requisitos de hardware e software. Tal divisão se deu pela característica multitécnica do projeto, que envolve componentes de software e hardware, na figura de um artefato robótico. Dentre os requisitos de hardware e software, esses foram classificados entre funcionais (descrição do requisito) e não funcionais (qual é métrica de desempenho que cada requisito funcional deve atingir). Além disso, cada um dos requisitos foi classificado como "obrigatório" ou "desejável", o que auxiliará a equipe de desenvolvimento a estabelecer uma hierarquia de prioridades para sua implementação.

## Requisitos funcionais de software

| ID  | DESCRIÇÃO                                                                                  | CATEGORIA  |
|-----|---------------------------------------------------------------------------------------------|------------|
| RFS1| O sistema deve traduzir voz em texto mediante “wake up world” ou acionamento via interface.  | Obrigatório|
| RFS2| O modelo de linguagem natural implementado deve ser capaz de compreender qual componente e sua quantidade que usuário deseja. | Obrigatório|
| RFS3| O sistema também deve ser capaz de receber comandos via texto.                                | Obrigatório|
| RFS4| O sistema deve ser capaz de avaliar se o input de texto deve passar pelo LLM ou se possui instruções diretas, que serão extraídas com script de processamento de texto mais simples. | Obrigatório|
| RFS5| O sistema deve ser capaz de exibir o número de componentes disponíveis no estoque uma vez identificado. | Obrigatório|
| RFS6| O sistema deve ser capaz de armazenar as coordenadas de todos os componentes que podem ser solicitados. | Obrigatório|
| RFS7| O sistema deve ser capaz de mapear o ambiente no qual o robô irá navegar.                       | Obrigatório|
| RFS8| O sistema deve ser capaz de guiar o robô até as coordenadas do item solicitado.                | Obrigatório|
| RFS9| O sistema deve ser capaz de modificar a quantidade de itens disponíveis uma vez que este for retirado do estoque. | Desejável  |
| RFS10| O sistema deve ser capaz de retornar o robô para seu ponto de origem.                         | Obrigatório|
| RFS11| O sistema deve ser capaz de exibir uma animação de face antropomórfica na tela presente no robô. | Desejável|
| RFS12| O sistema deve ser capaz de exibir a foto da peça solicitada tanto na tela presente no robô quanto no mecanismo de busca. | Desejável|

## Requisitos não funcionais de software

| ID | DESCRIÇÃO | MÉTRICA | CATEGORIA |
|-----|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|------------|
| RNFS1 |O software deve ser otimizado para uso eficiente dos recursos computacionais disponíveis no hardware do robô.|Uso de CPU e Memória RAM| Obrigatório|
| RNFS2 |O robô de serviço deve ser capaz de compreender e responder a comandos de voz em Português com uma precisão de pelo menos 95%, garantindo uma interação eficaz com os operadores no almoxarifado. |Feedback de erros e acertos| Desejável|
| RNFS3 |O sistema de transcrição de speech-to-text, precisa ter um WER (Word Error Rate) abaixo de 5. | WER | Desejável|
| RNFS4 |O sistema de navegação do robô deverá ser capaz de posicioná-lo em determinada coordenada com uma incerteza de, no máximo, 1 metro para ambas as coordenadas.|Cálculo do erro dos pontos das coordenadas|Desejável|
| RNFS5 | O software deve ser robusto e capaz de lidar com exceções e situações não previstas sem falhar.| Cálculo de erros de recuperação de falhas | Obrigatório|
| RNFS6 | A comunicação com o sistema ROS2 deve ter baixa latência para garantir a sincronia entre o robô e o sistema de controle central. | Medida em ms ou em s | Obrigatório|
| RNFS7 | O software deve ser modular, permitindo a fácil manutenção e expansão de funcionalidades. | Medida pela facilidade de adicionar, remover ou modificar módulos sem afetar o funcionamento geral do sistema. | Obrigatório|
| RNFS8 | A interface de usuário e os comandos de voz devem ser intuitivos para os usuários e operadores do sistema.| Testes de usabilidade | Obrigatório |
| RNFS9 | O software deve ser compatível e interagir de forma eficaz com o ROS2 e outros sistemas e dispositivos de hardware necessários para a operação do robô. | Pode ser avaliada pela capacidade de se integrar com diferentes sistemas e dispositivos| Desejável |
| RNFS10| Deve fornecer algoritmos de navegação eficazes para que o robô possa se mover com segurança no ambiente do almoxarifado | Avaliada pela precisão das trajetórias do robô em comparação com as trajetórias planejadas | Obrigatório |



 

## Requisitos funcionais de hardware

| ID  | DESCRIÇÃO                                                                                                   | CATEGORIA   |
|-----|--------------------------------------------------------------------------------------------------------------|-------------|
| RFH1| O robô deve ser alimentado por bateria recarregável.                                                          | Obrigatório |
| RFH2| O robô deve ser capaz de se movimentar para frente, para trás e rotacionar no sentido horário e anti-horário. | Obrigatório |
| RFH3| O robô deve possuir um sensor capaz de mapear seus arredores, bem como detectar obstáculos.                   | Obrigatório |
| RFH4| O robô deve possuir um monitor capaz de exibir informações úteis para o processo que irá desempenhar.          | Obrigatório |
| RFH5| O computador do operador do sistema deve ter entrada de áudio capaz de capturar sua voz, para a modalidade comandada por voz do sistema. | Obrigatório |
| RFH6| O robô deve possuir acesso à internet por meio de tecnologia Wifi.                                           | Obrigatório |


## Requisitos não funcionais de hardware 

| ID | DESCRIÇÃO | MÉTRICA | CATEGORIA |
|-----|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|------------|
|RNFH1| O robô deve ter uma velocidade mínima de 0,22 m/s  em terrenos planos e a mesma não pode ser menor que 0,10 m/s  em terrenos que tenham declividade de 1 a 5 %. | velocidade | Obrigatório |
|RNFH2| O robô deve ser capaz de se comunicar com redes Wi-Fi. | Wi-Fi | Obrigatório|
|RNFH3| O envelope de sensoriamento do LIDAR do robô deve ser capaz de detectar objetos em um raio de, no mínimo, 3 m e 360 graus. | Valores do sensor | Desejável |
|RNFH4| O robô não deverá ser utilizado por tempo superior a duas horas e trinta minutos contínuos. Quando a bateria atingir um estado crítico, a operação do robô deve ser interrompida e a bateria deve ser colocada. No caso do Turtlebot3 Burger, o tempo de uso estimado é de duas horas e meia, sendo que a carga completa da bateria também deve durar duas horas e meia. | Bateria | Obrigatório|
|RNFH5| O microfone deve ser capaz de captar a voz humana com no mínimo 50 db a uma distância de 40 cm.| Valores sensor| Desejável |

# APRESENTAÇÃO DE DESIGN PATTERNS

Para a operacionalização do robô autônomo que localizará itens em um almoxarifado será utilizado o Sistema Operacional de Robôs, ou ROS (Robot Operating System). No ROS, o padrão de design publicador-inscrito (publisher-subscriber) é utilizado para a comunicação de abstrações chamadas de Nós. Esses Nós em ROS podem publicar mensagem para tópicos específicos, assim como outros Nós podem se inscrever nesses mesmos tópicos para receber as mesmas mensagens. Esse padrão de design permite a construção de sistemas de robótica modulares e distribuídos, ideal para o cenário de aplicação do projeto e sua futura escalabilidade. 

## Padrão de Design ROS Publisher-Subscriber para Navegação Autônoma

### 1. Nó publicador de navegação

É responsável por publicar a informação de navegação, como a posição e velocidade do robô em um determinado instante e até mesmo as coordenadas x e y de seu destino. 

### 2. Nó de inscrição de navegação

Será responsável por se inscrever no tópico de navegação, receber suas atualizações e disparar ações pré-programadas, como mensagem na tela presente no robô e mensagens de áudio, bem como cuidar do acionamento dos motores.

### 3. Tipagem de mensagem

Define um padrão estrutural para a transmissão das informações entre os Nós. Esta comporta as informações de coordenadas, velocidade, etc.

## Vantagens

1. Desacoplamento: Uma vez que os nós de Publicação e de Inscrição são desacoplados, o sistema pode ser modificado e/ou reparado com a remoção e substituição de determinados Nós com mínimos efeitos no sistema como um todo.

2. Escalabilidade: Vantagem derivada do padrão de design que permite o desacoplamento, uma vez que mais Nós podem ser adicionados ao sistema, aumentando sua funcionalidade.

3. Interoperabilidade: Dada a comunicação utilizada pelo ROS, os Nós podem ser desenvolvidos em diferentes linguagens de programação, fazendo com que cada função possa ser otimizada de acordo com a linguagem adequada. E.g.: Um nó de visão computacional desenvolvido em C++ publicando as coordenadas de um marcador de calibração posicional para o resto da aplicação em Python.
