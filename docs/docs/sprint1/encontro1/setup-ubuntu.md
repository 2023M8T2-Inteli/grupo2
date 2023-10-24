---
title: Instalação do Ubuntu
sidebar_position: 2
---

# Instalação do Ubuntu em cartão SD

## 1. Criando um pen drive de boot

Para poder seguir esse tutorial, você vai precisar de:
```markdown
* Um pen drive com pelo menos 2GB de espaço total (ele vai ser formatado!);
* Um cartão SD com pelo menos 16GB de espaço (sugerido 32GB ou mais); e
* O seu computador (precisa ter porta USB e SD, claro =D).
```

Para instalar o Ubuntu, de longe a maneira mais fácil é usando um pen drive. 
Esse pen drive vai guardar uma versão portátil do Ubuntu. Nessa versão portátil 
temos acesso a várias das ferramentas do SO completo, incluindo uma ferramenta de 
instalação.

Para criar esse pen drive, que vamos chamar de `live boot`, precisamos utilizar 
uma ferramenta capaz de gravar uma imagem do formato `iso` diretamente no pen 
drive. A ferramenta que costumo utilizar para isso no Windows é o `Balena Etcher`.

Vamos primeiro baixar a imagem do live boot. Para isso, clique [nesse link](https://releases.ubuntu.com/22.04.3/ubuntu-22.04.3-desktop-amd64.iso).

A seguir, vamos instalar o Balena Etcher. Para isso, vamos usar o instalador
que você pode encontrar [nesse link](https://github.com/balena-io/etcher/releases/download/v1.18.11/balenaEtcher-Setup-1.18.11.exe).

Siga o setup de instalação do Balena Etcher e execute a aplicação. O vídeo a seguir 
exibe o processo completo para gravar a imagem do Ubuntu em um pen drive. Esse processo 
resume-se em:
1. Encontrar o arquivo `iso` no diretório onde você baixou;
2. Escolher o pen drive na lista de drives do sistema; e 
3. Clicar em `flash`.

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/hjgOSuDbVoU"
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

## 2. Bootando no pen drive 

A seguir, vai ser necessário reiniciar o seu computador. Logo após o splash screen 
da fabricante da sua placa mãe/laptop, você deve apertar uma tecla especial para 
entrar no menu de boot. Essa tecla tipicamente é o `F12`. Esse menu é diferente para 
cada fabricante, mas a ideia é que você possa manualmente selecionar, a partir de uma lista, 
qual dispositivo de armazenamento será utilizando pelo bootloader da placa mãe do seu 
computador. No nosso caso, precisaremos selecionar o pen drive que acabamos de configurar.
Como saber qual item é o pen drive? Geralmente é possível ver o nome da fabricante no 
nome do dispositivo, mas talvez acabe virando um processo de tentativa e erro.

## 3. Instalando o Ubuntu

:::danger
ATENÇÃO!! Quando estiver instalando o Ubuntu, as duas primeiras opções de 
instalador serão para criar um dual boot com Windows e apagar a partição Windows 
completamente. Não vamos usar **nenhuma dessas opções**. Vamos escolher a terceira 
opção, que é a instalação customizada.
:::

A seguir, vai ser necessário reiniciar o computador com o disco de boot plugado
em sua porta USB. Durante o processo de inicialização, você precisará apertar a 
tecla `F12` para entrar no menu de `boot`. Você precisará escolher o dispositivo
que vai usar para o boot do sistema. Escolha o seu disco que acabou de usar para
gravar o Ubuntu.

Se tudo deu certo, você vai ser levado direto para a tela de instalação do 
Ubuntu. A partir daí, siga as instruções abaixo:

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/SVK0ONyTnS8" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

### 3.1. Particionando o cartão SD 

Ao criar as partições do cartão SD, sugiro a seguinte configuração mínima:

* Partição do tipo EFI com `500MB`. Essa partição serve para que o firmware da 
placa mãe consiga iniciar o processo de boot do sistema operacional. O bootloader 
utilizado vai ser instalado aqui (no caso do Ubuntu, GRUB).
* Partição do tipo EXT4 com o restante do tamanho do cartão SD com mountpoint 
em `/`. Essa partição é a raíz do seu sistema operacional.

Considerações sobre SWAP e partição montada em `/home`:

* A partição de SWAP serve para armazenar o que está na memória RAM no momento 
em que o sistema entra em modo de hibernação. Como o cartão SD que estamos 
usando tem 64GB e os notebooks comumente tem 16GB de RAM hoje em dia, uma partição 
de SWAP fica pouco viável.

* A partição montada em `/home` normalmente é utilizada por questões de segurança 
de dados. É mais fácil configurar ferramentas de backup se você tiver essa separação.
Diferente da raíz do sistema (`/`), o diretório casa (`/home`) guarda apenas arquivos
relacionados aos usuários do sistema.

