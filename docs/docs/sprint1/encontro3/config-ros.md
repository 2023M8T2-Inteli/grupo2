---
title: Config ROS
sidebar_position: 1
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Configurações do ROS

![](/img/ros2_overlay.webp)

[Fonte](https://roboticseabass.com/2023/07/09/updated-guide-docker-and-ros2/)

O ROS 2 depende da noção de combinar espaços de trabalho (*workspaces*) usando o
ambiente do shell. O espaço de trabalho principal do ROS 2 é chamado de
"underlay", e os subsequentes são chamados de "overlays". Combinar espaços de 
trabalho facilita o desenvolvimento com diferentes versões do ROS 2 ou contra 
diferentes conjuntos de pacotes. Isso é realizado ao fontar arquivos de 
configuração toda vez que você abre um novo shell.

## 1. Instalação do ROS 

Para instalar o ROS 2 Humble, basta utilizar o script disponível no [repositório
de scripts](https://github.com/rmnicola/Scripts.git).

<Tabs defaultValue="clonar" values={[
        {label: 'Clonando o repositorio', value: 'clonar'},
        {label: 'Setup dos scripts', value: 'setup'},
        {label: 'Instalando o ROS', value: 'instalar'},
  ]}>

<TabItem value="clonar">

```bash
git clone https://github.com/rmnicola/Scripts ~/Scripts 
```

</TabItem>

<TabItem value="setup">

```bash
cd ~/Scripts && sudo ./install.sh
```

</TabItem>

<TabItem value="instalar">

```bash
install-ros
```

</TabItem>
</Tabs>


## 2. Setup do script de inicialização do ROS 

Para que os comandos e pacotes do ROS sejam reconhecidos pelo sistema, é 
necessário executar um script de inicialização. A maneira sugerida de trabalhar 
é rodando esse script toda vez que sua sessão de shell seja iniciada. Para isso, 
deve-se adicionar um comando ao script de inicialização do shell:

<Tabs defaultValue="bash" values={[
        {label: 'Bash', value: 'bash'},
        {label: 'Zsh', value: 'zsh'},
        {label: 'Zsh com a minha config.', value: 'zsh-meu'},
  ]}>

<TabItem value="bash">

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

</TabItem>

<TabItem value="zsh">

```bash
echo "source /opt/ros/humble/setup.zsh" >> ~/.zshrc
```

</TabItem>

<TabItem value="zsh-meu">

```bash
echo "source /opt/ros/humble/setup.zsh" >> '$ZODTDIR'/.zshrc
```

</TabItem>
</Tabs>

## 3. Verificação das variáveis de ambiente

Para que o ROS funcione adequadamente, são necessárias algumas variáveis de 
ambiente para definir aspectos relacionados ao `underlay`.
O script configurado acima já deve ter feito toda a configuração necessária, 
mas não custa nada conferir. Vamos rodar o comando:

```bash
printenv | grep -i ROS 
```

Vamos aproveitar a ocasião para aumentar o entendimento de vocês sobre os 
programas básicos UNIX? Vamos.

O comando `printenv` exibe todas as variáveis de ambiente do sistema. Como são 
muitas variáveis, acaba ficando um pouco difícil de encontrar as variáveis 
relacionadas ao ROS. Como resolver esse problema? Utilizando um segundo programa, 
o `grep`. O `grep` é uma ferramenta de linha de comando usada para pesquisar 
padrões específicos dentro de arquivos ou entrada de texto, baseando-se em 
expressões regulares. No caso, estamos buscando o padrão `ROS`.

Beleza, mas como o `grep` sabe o que tem na saída do `printenv`? Caso vocês 
ainda não conheçam, faço a apresentação formal: pipe (`|`), queridos alunos. 
Queridos alunos, pipe. O pipe serve para redirecionar a saída de ferramentas 
de linha de comando, mexendo direto no fluxo do `stdin`, `stdout` e `stderr`.
O pipe é o que faz funcionar a filosofia Unix de criar um programa que faça 
uma coisa, mas uma coisa bem feita. Com ele, podemos encadear diversas ferramentas 
simples para criar uma funcionalidade mais complexa. Aprendam a encadear 
"tubulações" e vocês nunca mais vão querer voltar pro deserto do `powershell`. 
[Referência sobre pipes](https://dev.to/leandronsp/entendendo-unix-pipes-3k56)

Depois desse redirecionamento, vamos às variáveis de ambiente que devem ter sido 
setadas no seu sistema pelo ROS:

```bash
ROS_DISTRO=humble
ROS_LOCALHOST_ONLY=0
ROS_PYTHON_VERSION=3
ROS_VERSION=2
```
