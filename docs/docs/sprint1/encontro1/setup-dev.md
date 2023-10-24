---
title: Setup ambiente dev
sidebar_position: 4
---

# Setup de ferramentas de desenvolvimento

Nesta seção estão algumas das ferramentas de desenvolvimento para tornar a 
vida de vocês um pouco mais fácil (e a vida no terminal ficar mais confortável)

## 1. Zsh

A primeira dessas ferramentas na verdade é uma versão mais moderna do antigo 
bourne shell (shell) e o bourne again shell (bash). O principal motivo da 
recomendação do uso dessa ferramenta se dá pelo seu poderoso autocomplete. Se 
configurado corretamente, o zsh fornece um sistema de autocomplete muito robusto 
e altamente customizável.

A maioria das pessoas começa a utilizar o Zsh com um "gerenciador de pacotes"
de plugin para shell chamando `Oh My Zsh`. Francamente, acho ele uma porcaria.
É um projeto que carrega os plugins utilizando um repositório que agrega todos 
os plugins de usuários do Zsh, o que faz com que seja muito fácil deixar o 
startup do prompt demorando alguns segundos (pode não parecer muito, mas a 
usabilidade do terminal depende fortemente de tempos de resposta quase 
instantâneos).

Em vez de usar o `Oh My Zsh`, eu sugiro o uso de uma configuração customizada,
feita a mão e adicionando plugins de forma sensata. Não precisa necessariamente
ser a minha configuração, mas utilizando o meu repositório de `Dotfiles` em 
conjunto com o de `Scripts` fica muito fácil configurar o zsh. Para começar,
vamos instalar o zsh com:

### 1.1. Instalando o zsh

```bash
sudo apt install zsh
```

A seguir, vamos garantir que o zsh é o shell padrão do sistema usando:

```bash
chsh -s $(which zsh)
```

Notem que, para que essa mudança seja computada, é necessário deslogar e logar
novamente.

### 1.2. Reproduzindo a minha configuração

Para reproduzir a minha configuração, vamos começar clonando o meu repositório
de scripts:

```bash
git clone https://github.com/rmnicola/Scripts.git 
```

A seguir, rode o script de instalação dos binários:

```bash
cd Scripts
sudo ./install.sh
```

Agora, retorne para o seu home e clone o repositório de arquivos de configuração:

```bash
git clone https://github.com/rmnicola/Dotfiles.git
```

Entre na pasta e rode o meu script de configuração dos dotfiles. Esse script vai
criar um link simbólico dos diretórios/arquivos de configuração para a pasta 
`~/.config`:

```
cd Dotfiles
link-configs
```

Como o `zsh` é bagunceiro e usa como padrão a pasta home do usuário para guardar 
seu arquivo de configuração, precisamos contar para ele que vamos utilizar outra 
pasta. Para isso, usaremos a variável de ambiente `ZDOTDIR`. Onde colocar a 
inicialização dessa variável? De acordo com a 
[ordem de execução do zsh](https://wiki.archlinux.org/title/zsh#Startup/Shutdown_files),
podemos ver que o arquivo `/etc/zsh/zshenv` é ideal para este tipo de setup.
Vamos adicionar essa definição utilizando o comando abaixo:

```bash
echo "ZDOTDIR=$HOME/.config/zsh" >> /etc/zsh/zshenv
```


## 2. Nvim

> I use neovim, btw
>
> — Einstein, probably

A Canonical acha adequado deixar uma versão extremamente desatualizada do neovim
no apt para forçar a gente a usar o snap. Eu não acho. Se você também não acha,
use esse meu script para instalar/atualizar o neovim usando o AppImage oficial 
mais recente:

```bash
install-neovim
```

Para conseguir rodar essa versão, garante que o `fuse` está instalado:

```bash
sudo apt install fuse
```

Se você usou meus `Dotfiles` no passo anterior, assim que você abrir o neovim
o Packer vai trabalhar e baixar todas as extensões necessárias. Após isso, 
reinicie o neovim e desenvolva o seu código confortavelmente =)

## 3. Vscode

Em construção. Ainda não configurei meu vscode.

## 4. Git
:::note
Ainda não arrumei um probleminha na assinatura de commit do git. Tudo vai 
funcionar, mas vai aparecer `Unverified` no github. Em breve arrumo
:::

O git é uma das ferramentas mais importantes no arsenal do desenvolvedor. 
Há várias ferramentas com interface gráfica para usar o Git, mas qual a graça 
nisso? Vamos de terminal! Para isso, você vai precisar criar uma chave SSH e 
algumas configurações básicas do git. Não achei razoável adicionar as 
configurações de nome e email dentro de um script, então seguem
as instruções:

```bash
git config --global user.name "Seu Nome Aqui"
git config --global user.email "seu.email@aqui"
```

Antes de configurar a chave ssh, vamos resolver um probleminha: nano? nãono.

```bash
git config --global core.editor "nvim"
```

Por fim, vamos configurar a chave ssh com:
```bash
set-ssh-key git 
```

Se tudo deu certo, você configurou sua chave ssh e ela automaticamente foi 
copiada pro seu clipboard. Entre [nesse link](https://github.com/settings/keys),
 clique em `Adicionar uma chave SSH` e é só apertar `Ctrl-V`.

## 5. Node

Snap de novo, Canonical? Não, vamos instalar usando o `fnm`, um gerenciador de 
versões do Node feito inteiramente em Rust (apoiando os infinitos projetos que 
reescrevem absolutamente **tudo** em rust sem nenhum motivo racional =D). 
Basta rodar:

```bash
install-node
```
