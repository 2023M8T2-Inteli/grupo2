---
title: Análise Financeira
sidebar_position: 5
---
# Análise Financeira

Construir uma análise financeira para o projeto é de fundamental importância para que o cliente possa avaliar a viabilidade de sua implementação. Desse modo, os componentes do projeto foram segmentados em *hardware*, *software*, *equipe de desenvolvimeto* e *equipe de manutenção*, e foram precificados de acordo com referências do mercado atual. 

**1. Componentes de hardware**

Primeiramente, foram idealizados e precificados os componentes de hardware necessários para o desenvolvimento do projeto. Na tabela, encontram-se um robô autônomo de escala industrial, o robô Turtlebot3 Burger utilizado para a construção de uma prova de conceito, a tela LCD que ficará acoplada ao robô e será utilizada como interface de interação e, por fim, uma impressora 3D e o filamento necessário para a impressão do suporte para o LCD.

<table>
  <thead>
    <tr>
      <th colSpan="4">Componentes de hardware</th>
    </tr>
    <tr>
      <th>Componente</th>
      <th>Descrição</th>
      <th>Quantidade</th>
      <th>Valor (R$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Robô autônomo</td>
      <td>Robô que irá desempenhar a função no almoxarifado</td>
      <td>1x</td>
      <td>$175,000.00</td>
    </tr>
    <tr>
      <td>Turtlebot3 Burger</td>
      <td>Robô que representa veículo autônomo para Proof of Concept</td>
      <td>1x</td>
      <td>$3,260.00</td>
    </tr>
    <tr>
      <td>LCD Screen</td>
      <td>Interface de acesso ao software que será acoplada ao robô</td>
      <td>1x</td>
      <td>$240.00</td>
    </tr>
    <tr>
      <td>Impressora 3D Creality K1</td>
      <td>Impressão 3D de peças para suporte no robô</td>
      <td>1x</td>
      <td>$4,950.00</td>
    </tr>
    <tr>
      <td>Rolo de filamento</td>
      <td>Material para impressão 3D do suporte do LCD</td>
      <td>1x</td>
      <td>$98.00</td>
    </tr>
  </tbody>
</table>

**2. Componentes de software**

O único componente de software que poderá gerar custo para o parceiro será a API do modelo de LLM construído. Como referência, foi utilizado o preço da API do GPT 3.5. Foram calculados, respectivamente, o valor por requisição feita para o modelo, o valor mensal e o valor anual, considerando a estimativa de uso de 5.000 requisições por mês.

<table>
  <thead>
    <tr>
      <th colSpan="5">Componentes de software</th>
    </tr>
    <tr>
      <th>Componente</th>
      <th>Descrição</th>
      <th>Valor por solicitação (R$)</th>
      <th>Valor mensal (R$)</th>
      <th>Valor anual (R$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>API GPT 3.5</td>
      <td>Processamento de linguagem utilizando modelos GPT</td>
      <td>$0.20</td>
      <td>$1,000.00</td>
      <td>$12,000.00</td>
    </tr>
  </tbody>
</table>

**3. Equipe de desenvolvimento**

A equipe responsável por desenvolver o projeto representa o maior custo identificado. A equipe é composta por profissionais de múltiplas áreas, de modo a contemplar as diferentes partes do produto. A tabela abaixo apresenta os profissionais que compõem a equipe de desenvolvimento, suas funções, o tempo de trabalho necessário para a construção do projeto, a quantidade de profissionais necessários para a execução do projeto, a remuneração mensal de cada profissional e o valor total que será pago para cada profissional ao longo do projeto.

<table>
  <thead>
    <tr>
      <th colSpan="6">Equipe de desenvolvimento</th>
    </tr>
    <tr>
      <th>Profissão</th>
      <th>Função</th>
      <th>Tempo</th>
      <th>Quantidade</th>
      <th>Remuneração</th>
      <th>Total (R$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>UI/UX designer</td>
      <td>Construção do design da interface de usuário</td>
      <td>1 mês</td>
      <td>1x</td>
      <td>$8,000.00</td>
      <td>$8,000.00</td>
    </tr>
    <tr>
      <td>Quality Assurance</td>
      <td>Análise da qualidade do produto por meio de testes</td>
      <td>2 meses</td>
      <td>2x</td>
      <td>$7,000.00</td>
      <td>$14,000.00</td>
    </tr>
    <tr>
      <td>Engenheiro de ML</td>
      <td>Construção do modelo de LLM utilizado no chatbot</td>
      <td>8 meses</td>
      <td>2x</td>
      <td>$20,000.00</td>
      <td>$320,000.00</td>
    </tr>
    <tr>
      <td>Engenheiro de software</td>
      <td>Construção da aplicação com chatbot integrado</td>
      <td>10 meses</td>
      <td>2x</td>
      <td>$11,000.00</td>
      <td>$220,000.00</td>
    </tr>
    <tr>
      <td>Engenheiro de computação</td>
      <td>Programação do veículo autônomo, integração com software</td>
      <td>10 meses</td>
      <td>2x</td>
      <td>$12,000.00</td>
      <td>$240,000.00</td>
    </tr>
    <tr>
      <td>Engenheiro de automação e controle</td>
      <td>Configuração e manutenção do robô</td>
      <td>10 meses</td>
      <td>1x</td>
      <td>$1,600,000</td>
      <td>$160,000.00</td>
    </tr>
    <tr>
      <td>Engenheiro mecatrônico</td>
      <td>Implementação do projeto de hardware</td>
      <td>2 meses</td>
      <td>2x</td>
      <td>$6,000.00</td>
      <td>$24,000.00</td>
    </tr>
    <tr>
      <td>Gerente de projetos</td>
      <td>Gerência do projeto</td>
      <td>12 meses</td>
      <td>1x</td>
      <td>$18,000.00</td>
      <td>$216,000.00</td>
    </tr>
  </tbody>
</table>

**4. Equipe de manutenção**

Uma vez que o projeto é implementado, o cliente deverá arcar com os custos referentes à manutenção do sistema. Para isso, será necessário contratar um profissional de engenharia mecatrônica para realizar a manutenção periódica do veículo autônomo. A tabela abaixo apresenta a função do profissional em questão, a periodicidade com a qual a manutenção deve ser realizada e a remuneração do profissional por manutenção. Por fim, é apresentado o valor anual que será gasto com a manutenção do hardware.

<table>
  <thead>
    <tr>
      <th colSpan="6">Equipe de manutenção</th>
    </tr>
    <tr>
      <th>Profissão</th>
      <th>Função</th>
      <th>Periodicidade</th>
      <th>Quantidade</th>
      <th>Remuneração</th>
      <th>Total anual (R$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Engenheiro mecatrônico</td>
      <td>Manutenção periódica do veículo autônomo</td>
      <td>3 meses</td>
      <td>1x</td>
      <td>$6,000.00</td>
      <td>$24,000.00</td>
    </tr>
  </tbody>
</table>

**5. Custo de implementação do projeto**

A tabela abaixo apresenta o custo total de implementação do projeto, considerando os componentes de hardware, software e equipe de desenvolvimento. O valor total do projeto, desconsiderando impostos, é de R$1,397,548.00. Considerando o imposto cobrado por dentro (18%), o valor total do projeto passa a ser de R$1,704,326.83.

<table>
  <thead>
    <tr>
      <th colSpan="2">Custo de implementação (1º ano)</th>
    </tr>
    <tr>
      <th>Setor</th>
      <th>Valor total (R$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Componentes de hardware</td>
      <td>$183,548.00</td>
    </tr>
    <tr>
      <td>Componentes de software</td>
      <td>$12,000.00</td>
    </tr>
    <tr>
      <td>Equipe de desenvolvimento</td>
      <td>$1,202,000.00</td>
    </tr>
    <tr>
      <td>Valor total do projeto</td>
      <td>$1,397,548.00</td>
    </tr>
    <tr>
      <td>Total com imposto (18%)</td>
      <td>$1,704,326.83</td>
    </tr>
  </tbody>
</table>

**6. Custo de manutenção anual**

Por fim, dispõe-se abaixo o custo de manutenção anual do projeto. O valor total anual é de R$24,000.00, correspondente à remuneração do profissional responsável pela realização periódica da manutenção.

<table>
  <thead>
    <tr>
      <th colSpan="2">Custo de manutenção (anual)</th>
    </tr>
    <tr>
      <th>Setor</th>
      <th>Valor total (R$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Manutenção</td>
      <td>$24,000.00</td>
    </tr>
  </tbody>
</table>


### Referências

Abaixo, encontram-se as referências utilizadas para precificar os componentes do projeto na análise financeira.

Custo da API: https://hackernoon.com/pt/pre%C3%A7os-de-chatgpt-abertos-ais-explicados-quanto-custa-usar-modelos-gpt

Custo do robô autônomo: https://mwpvl.com/html/locus_robotics_-_independent_consultant_review.html#:~:text=With%20an%20all%2Din%20price,out%20of%20the%20starting%20gates.

Custo do Turtlebot: https://www.robotis.us/turtlebot-3-burger-us/

Custo da impressora 3D: https://www.loja2n.com.br/MLB-3415060649-creality-k1-impressora-3d-220x220x250mm-300-c-600mms-_JM?variation=178508584298&gclid=CjwKCAjw1t2pBhAFEiwA_-A-NK60xXdh48rXe7s94QUc0wvQXDf_u-jWNbOb5dARem4tRiMY2b8WzhoCmCMQAvD_BwE

Custo do LCD: https://www.waveshare.com/7inch-hdmi-lcd-h.htm

Custo do rolo de filamento: https://3dlab.com.br/produto/filamento-pla-branco/?attribute_pa_peso=1kg&attribute_pa_diametro=175mm&utm_source=google&utm_medium=cpc&utm_campaign=17534382192&utm_term=&utm_content=&adgroupid=&feeditemid=&targetid=&loc_interest_ms=&loc_physical_ms=1001773&matchtype=&network=x&device=c&devicemodel=&placement=&target=&adposition=&gad=1&gclid=CjwKCAjw1t2pBhAFEiwA_-A-NIVkqbMECuFVeP2KCZ5tcboG96d3DlWMk964UGNzssiGWqOZk-MudRoCxGMQAvD_BwE

Remunerações: https://www.glassdoor.com.br/Sal%C3%A1rios