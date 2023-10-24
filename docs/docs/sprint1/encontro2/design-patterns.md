---
title: Design Patterns
sidebar_position: 1
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Design patterns em Python

A utilização de *design patterns* é essencial para promover o baixo acoplamento 
e a alta coesão em sistemas de software. Padrões como Singleton, Factory,
Strategy e Dependency Injection são técnicas que incentivam a separação de
responsabilidades e a dependência em interfaces ou abstrações, permitindo que
componentes interajam sem depender diretamente uns dos outros. Isso leva à
redução do acoplamento. Por outro lado, padrões como Composite, Observer e
Command incentivam a criação de componentes com funções bem definidas e
limitadas, reforçando a coesão. Ao adotar esses padrões, os desenvolvedores
podem construir sistemas mais modulares, escaláveis e fáceis de
manter.

## 1. Strategy pattern 
<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/WQ8bNdxREHU" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

O **Strategy Pattern** é um padrão de projeto que permite que você defina uma
família de algoritmos, encapsule cada um deles e os torne intercambiáveis. Isso
significa que você pode alterar o comportamento de uma classe sem alterar seu
código, apenas trocando a "estratégia" ou algoritmo que ela
usa.

A Inversão de Dependência é um princípio da programação orientada a objetos que
sugere que módulos de alto nível não devem depender de módulos de baixo nível,
mas ambos devem depender de abstrações. Em outras palavras, em vez de depender
de detalhes concretos, seu código deve depender de interfaces ou classes
abstratas.

### 1.1. Exemplo: Calculadora de Descontos

<Tabs
  defaultValue="antes"
  values={[
    {label: 'Antes', value: 'antes'},
    {label: 'Depois', value: 'depois'},
  ]}>

<TabItem value="antes">

```python showLineNumbers title="Antes do strategy pattern"
class Order:
    def __init__(self, total, discount_type):
        self.total = total
        self.discount_type = discount_type

    def final_price(self):
        if self.discount_type == "fixed":
            return self.total - 10
        elif self.discount_type == "percentage":
            return self.total * 0.9
```

</TabItem>

<TabItem value="depois">

```python showLineNumbers title="Depois do strategy pattern"
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total):
        pass

class FixedDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total - 10

class PercentageDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total * 0.9

class Order:
    def __init__(self, total, discount_strategy):
        self.total = total
        self.discount_strategy = discount_strategy

    def final_price(self):
        return self.discount_strategy.apply_discount(self.total)
```

</TabItem>
</Tabs>

Neste exemplo, a classe `Order` é responsável por calcular o preço final com
base no tipo de desconto. Este design é rígido e não é fácil adicionar novos
tipos de desconto sem modificar a classe
`Order`.

Após a aplicação do *strategy pattern*, em vez de a classe `Order` decidir como
aplicar o desconto, ela simplesmente usa a estratégia fornecida. Para adicionar 
um novo tipo de desconto, apenas uma nova estratégia é necessária.

### 1.2. Diferença entre Strategy e Inversão de dependência

Se para você agora os conceitos de strategy pattern e inversão de dependência 
estão parecendo a mesma coisa, é pelo fato de que **na maioria dos casos, o 
strategy pattern só faz sentido em conjunto com a inversão de dependência**. E,
 por sua vez, **a inversão de dependência geralmente é aplicada através do 
 strategy pattern**.

Vamos ver um outro exemplo, agora dividindo-o em `antes`, `strategy` e 
`strategy+inversão`:

<Tabs
  defaultValue="antes"
  values={[
    {label: 'Antes', value: 'antes'},
    {label: 'Strategy', value: 'strategy'},
    {label: 'Strategy+Inversão', value: 'strategy2'},
  ]}>

<TabItem value="antes">

```python showLineNumbers title="Antes"
class CloudUploader:
    def __init__(self, service):
        self.service = service

    def upload(self, file):
        if self.service == "S3":
            # código para upload no S3
            print("Uploading to S3...")
        elif self.service == "GCP":
            # código para upload no GCP
            print("Uploading to GCP...")
```

</TabItem>

<TabItem value="strategy">

```python showLineNumbers title="Strategy"
class S3Strategy():
    def upload(self, file):
        # código para upload no S3
        print("Uploading to S3...")

class GCPStrategy():
    def upload(self, file):
        # código para upload no GCP
        print("Uploading to GCP...")

class CloudUploader:
    def __init__(self, service):
        self.service = service

    def upload(self, file):
        if self.service == "S3":
            S3Strategy().upload(file)
        elif self.service == "GCP":
            GCPStrategy().upload(file)
```

</TabItem>

<TabItem value="strategy2">

```python showLineNumbers title="Strategy+Inversão"
from abc import ABC, abstractmethod

class CloudStrategy(ABC):
    @abstractmethod
    def upload(self, file):
        pass

class S3Strategy(CloudStrategy):
    def upload(self, file):
        # código para upload no S3
        print("Uploading to S3...")

class GCPStrategy(CloudStrategy):
    def upload(self, file):
        # código para upload no GCP
        print("Uploading to GCP...")

class CloudUploader:
    def __init__(self, strategy: CloudStrategy):
        self.strategy = strategy

    def upload(self, file):
        self.strategy.upload(file)

```

</TabItem>

</Tabs>

É possível notar que o exemplo intermediário, em que temos apenas o strategy 
pattern sendo utilizado, ainda não resolve o problema do acoplamento. Podemos 
concluir, portanto, que nesse exemplo e na esmagadora maioria dos casos em que 
utilizamos o strategy pattern, **não faz sentido utilizar strategy pattern sem 
inversão de dependência**. Em resumo:

* O strategy pattern é definido pelo uso de diferentes estratégias de
implementação de um algoritmo, seccionados por classes ou funções.
* A inversão de dependência determina que uma classe dependa não de outras
classes

concretas, mas sim de uma classe abstrata para a sua implementação.

As duas estratégias são comumente utilizadas juntas.

## 2. Observer pattern 

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/oNalXg67XEE" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

O **Observer Pattern** é um padrão de projeto que define uma dependência entre
objetos, de modo que quando um objeto muda de estado, todos os seus dependentes
são automaticamente notificados e atualizados. É amplamente usado em sistemas
que requerem que um componente mantenha outros componentes informados sobre
mudanças.

### 2.1. Exemplo: Sistema de Notificação

Imagine um sistema simples onde um blog posta novos artigos e precisa informar
todos os assinantes sobre o novo conteúdo.

<Tabs
  defaultValue="antes"
  values={[
    {label: 'Antes', value: 'antes'},
    {label: 'Depois', value: 'depois'},
  ]}>

<TabItem value="antes">

```python showLineNumbers title="Blog antes"
class Blog:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber_email):
        self.subscribers.append(subscriber_email)

    def publish_article(self, article):
        print(f"Published: {article}")
        for subscriber in self.subscribers:
            # enviar email diretamente
            print(f"Sent email to {subscriber} about new article!")
```

</TabItem>

<TabItem value="depois">

```python showLineNumbers title="Blog Observer"
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class EmailSubscriber(Observer):
    def __init__(self, email):
        self.email = email

    def update(self, message):
        print(f"Sent email to {self.email} with message: {message}")

class Blog:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def publish_article(self, article):
        print(f"Published: {article}")
        for subscriber in self.subscribers:
            subscriber.update(f"New article published: {article}")
```

</TabItem>

</Tabs>

### 2.2. Efeito em termos de Coesão e Acoplamento

- **Coesão**: O uso do Observer Pattern aumenta a coesão, já que as
responsabilidades estão mais claramente definidas. No exemplo, a lógica de
notificação é claramente separada da lógica de
publicação.

- **Acoplamento**: O padrão reduz o acoplamento, pois a classe `Blog` agora não
precisa saber os detalhes de como notificar cada assinante. Ela apenas comunica
que um evento ocorreu, e é responsabilidade de cada observador decidir como
responder.

### 2.3. Observer pattern no ROS

O Robot Operating System (ROS) utiliza uma variante do Observer Pattern em sua
infraestrutura de comunicação. Em ROS, os "publishers" publicam mensagens em
tópicos, e os "subscribers" se inscrevem nesses tópicos para receber as
mensagens. A relação entre publishers e subscribers em ROS é semelhante à
relação entre observáveis e observadores no Observer
Pattern.

Vamos ver um exemplo simplificado de como isso funcionaria em um cenário
hipotético, onde um subscriber força sua adição a um publisher quando se
inscreve em um tópico:

```python showLineNumbers title="Observer ROS"
class Publisher:
    def __init__(self, topic_name):
        self.topic_name = topic_name
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def publish(self, message):
        for subscriber in self.subscribers:
            subscriber.receive(message)

class Subscriber:
    def __init__(self, topic_name, master):
        self.topic_name = topic_name
        self.master = master
        self.master.subscribe(self, topic_name)

    def receive(self, message):
        print(f"Received message: {message}")

class ROSMaster:
    def __init__(self):
        self.publishers = {}

    def register_publisher(self, topic_name, publisher):
        self.publishers[topic_name] = publisher

    def subscribe(self, subscriber, topic_name):
        publisher = self.publishers.get(topic_name)
        if publisher:
            publisher.add_subscriber(subscriber)
```

**Uso:**
```python
master = ROSMaster()
```

**Publisher registra seu tópico no master**
```python
pub = Publisher("sensor_data")
master.register_publisher("sensor_data", pub)
```

**Subscriber se inscreve no tópico e é automaticamente adicionado ao publisher**
```python
sub = Subscriber("sensor_data", master)
```

**Quando o publisher publica uma mensagem, o subscriber a recebe**
```python
pub.publish("data from sensors")
```

No exemplo acima:

- Um `Publisher` pode publicar mensagens.
- Um `Subscriber` se inscreve em um tópico através do `ROSMaster`, que age como
um mediador.
- Quando um `Subscriber` é criado e se inscreve em um tópico, ele é
automaticamente adicionado à lista de subscribers do `Publisher`
apropriado.

Embora este seja um exemplo simplificado e o ROS real tenha uma implementação
muito mais complexa e robusta, o conceito subjacente é semelhante. O ROS utiliza
o padrão para permitir comunicações flexíveis e descentralizadas entre nós em um
sistema
robótico.
