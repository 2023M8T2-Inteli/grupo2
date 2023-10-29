# Arquitetura do sistema

![Arquitetura do sistema](../../assets/arquitetura.png)

## Resumo:

O sistema consiste em uma arquitetura baseada em ROS que integra um Nodo Central com módulos de processamento de voz e texto a um Robô Autônomo. O objetivo é permitir que o robô interprete e execute comandos relacionados à busca de peças em um ambiente, utilizando tanto entradas de teclado quanto comandos de voz.

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
