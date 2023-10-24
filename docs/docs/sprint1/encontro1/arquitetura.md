---
title: Engenharia de software
sidebar_position: 5
---

# Acoplamento e Coesão em Engenharia de Software

:::info Autoestudo

Coesão e acoplamento

:::

**Autoestudo de coesão e acoplamento**

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/eiDyK_ofPPM" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>
<br/>

O desenvolvimento de software eficaz e sustentável depende muito de como as 
partes individuais do software interagem entre si. Dois conceitos centrais nesse

contexto são acoplamento e coesão. Tratam-se de conceitos de alto nível que, 
em linhas gerais, descrevem o quão fácil é modificar ou ampliar o seu código.

## 1. Coesão

Coesão refere-se à medida em que as responsabilidades de um módulo ou classe 
são estreitamente relacionadas. Uma classe coesa faz "uma coisa e faz bem". 
Quando a coesão é alta, o módulo ou a classe tem um propósito bem definido, 
o que torna o software mais compreensível, fácil de manter e menos propenso a
erros.

**Exemplo de Coesão**:

No vídeo acima, o interlocutor usa o exemplo a seguir para demonstrar um código 
com baixa coesão:

```python showLineNumbers title="codigo-baguncado.py"
def handle_stuff(d: Data,
                quantity: int, screen: int, screen:int,
                status: int, c: Color, ...):
    update_corporate_database(d, q, status)
    for i in range(0, quantity):
        profit[i] = revenue[i] - expense[i] * status
    new_color = c 
    status = SUCCESS 
    display_profits(screenX, screenY, status, d, c)
```

O problema já começa no nome da função. Na programação, uma função geralmente 
esta atrelada a uma ação. Sendo assim, o nome dessa função deve refletir a ação.


Vamos olhar com mais cuidado para essa função:

```python showLineNumbers title="codigo-baguncado.py"
def handle_stuff(d: Data,
                quantity: int, screen: int, screen:int,
                status: int, c: Color, ...):
    # red
    update_corporate_database(d, q, status)
    # blue
    for i in range(0, quantity):
        # blue
        profit[i] = revenue[i] - expense[i] * status
    # green
    new_color = c 
    # purple
    status = SUCCESS 
    # blue
    display_profits(screenX, screenY, status, d, c)
```

Nota-se que há **quatro** tipos de ações, aparentemente desconexas, acontecendo
em

uma mesma função. Isso é um futuro pesadelo para manter e expandir.

A classe abaixo, por outro lado, é um exemplo de implementação coesa:

```python title="calculadora.py" showLineNumbers
class Calculadora:

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b
```

Ela faz um coisa, é clara com relação ao que está fazendo e não tem nada fora do

lugar devido.

## 2. Acoplamento

Acoplamento refere-se ao grau em que um módulo ou classe depende de outros
módulos ou classes. O objetivo é ter o menor acoplamento possível, ou seja, cada
módulo ou classe deve operar de forma tão independente quanto possível. Um baixo
acoplamento facilita a manutenção, o teste e a reutilização do
código.

**Exemplo de Acoplamento**:

Imagine que temos duas classes, uma para armazenar detalhes do usuário e outra
para gerenciar
autenticação:

```python showLineNumbers title="auth.py"
class DetalhesUsuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Autenticacao:
    def login(self, usuario):
        if usuario.nome == "admin":
            return True
        return False
```

Se, no futuro, a estrutura ou os métodos da classe `DetalhesUsuario` forem
alterados, pode haver um impacto direto na classe `Autenticacao`, pois ela está
acoplada à classe `DetalhesUsuario` através do uso direto do atributo
`nome`.

**Reduzindo Acoplamento**:

Uma maneira de reduzir o acoplamento é através da injeção de dependência. 
Em vez de a classe `Autenticacao` depender diretamente de `DetalhesUsuario`, 
podemos passar a dependência como um parâmetro:

```python showLineNumbers title="auth_injected.py"
class Autenticacao:
    def login(self, nome_usuario):
        if nome_usuario == "admin":
            return True
        return False
```

Agora, a classe `Autenticacao` não depende diretamente da estrutura de
`DetalhesUsuario`.

Outra técnica útil para diminuir o acoplamento do seu código é usando inversão 
de dependência.

## 3. Inversão de dependência

:::info Autoestudo

Inversão de dependência

:::

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/Kv5jhbSkqLE" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>
<br/>

A **Inversão de Dependência** é um dos cinco princípios SOLID do design 
orientado a objetos, e refere-se a uma forma específica de reduzir o acoplamento

entre módulos ou classes de um software. A ideia principal é que módulos de 
alto nível, que fornecem funcionalidades complexas, não devem depender de 
módulos de baixo nível, que fornecem operações detalhadas. Em vez disso, 
ambos devem depender de abstrações.

Para implementar a inversão de dependência, geralmente seguimos dois princípios
fundamentais:

1. Módulos de alto nível não devem depender de módulos de baixo nível. Ambos
devem depender de
abstrações.
2. Abstrações não devem depender de detalhes. Detalhes devem depender de
abstrações.

Isso é frequentemente alcançado através do uso de interfaces (em linguagens que
suportam) ou classes
abstratas.

**Exemplo em Python**:

Imagine um sistema de notificação em que os usuários podem ser notificados por
diferentes meios, como e-mail ou mensagem
SMS.

**Sem Inversão de Dependência**:

```python showLineNumbers title="notifier.py"
class EmailNotifier:
    def enviar(self, message):
        print(f"Enviando email: {message}")

class SMSNotifier:
    def enviar(self, message):
        print(f"Enviando SMS: {message}")

class Notificacao:
    def __init__(self, tipo):
        self.tipo = tipo

    def notificar(self, message):
        if self.tipo == "email":
            notifier = EmailNotifier()
        else:
            notifier = SMSNotifier()
        notifier.enviar(message)
```

O problema com o design acima é que a classe `Notificacao` está fortemente 
acoplada às classes `EmailNotifier` e `SMSNotifier`. 
Se quisermos adicionar outro meio de notificação, teríamos que modificar a
classe
`Notificacao`.

**Com Inversão de Dependência**:

Vamos usar uma abstração para desacoplar `Notificacao` dos meios de notificação:

```python showLineNumbers title="notifier-inverted.py"
from abc import ABC, abstractmethod

class Notifier(ABC):

    @abstractmethod
    def enviar(self, message):
        pass

class EmailNotifier(Notifier):
    def enviar(self, message):
        print(f"Enviando email: {message}")

class SMSNotifier(Notifier):
    def enviar(self, message):
        print(f"Enviando SMS: {message}")

class Notificacao:
    def __init__(self, notifier):
        self.notifier = notifier

    def notificar(self, message):
        self.notifier.enviar(message)
```

Agora, a classe `Notificacao` depende de uma abstração (`Notifier`) e não 
das implementações concretas. Para adicionar outro meio de notificação, 
apenas criamos uma nova classe que implementa a abstração, 
sem a necessidade de modificar a classe `Notificacao`.

Ao aplicar a inversão de dependência, tornamos nosso sistema mais modular e 
flexível, reduzindo o acoplamento e tornando-o mais adaptável a mudanças
futuras.
