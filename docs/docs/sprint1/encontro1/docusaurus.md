---
title: Docusaurus
sidebar_position: 7
---

# Introdução ao Docusaurus

Ficou curioso sobre como eu fiz essa página? Seus problemas acabaram! Nessa seção, 
será apresentado o framework open source para documentação desenvolvido pela 
Meta e amplamente utilizado, o Docusaurus.

## 1. Instalando o docusaurus 

Para instalar o docusaurus, precisamos ter `node >= 12`.

A melhor forma de inicializar uma documentação com docusaurus é criando um projeto
novo em seu repositório:

```bash
npx create-docusaurus@latest docs classic
```

## 2. Criando apenas documentação 
:::info
Em construção Por enquanto, acesse [documentação oficial](https://docusaurus.io/docs/docs-introduction#docs-only-mode)
:::

## 3. Configurando o deploy automático pelo Github

Para criar o deploy automático pelo github, vamos precisar utilizar o Github Actions.
Antes de mais nada, acesse o seu repositório e vá para a seção `settings`:

![](/img/repo-settings.png)

A seguir, clique em `pages`:

![](/img/repo-pages.png)

A seguir, escolha como source da sua página o `Github Actions` no menu drop-down:

![](/img/repo-actions.png)

Pronto! Seu repositório já está configurado para aceitar deploy de páginas a 
partir de `Actions`. Resta agora criar a pasta `.github/workflows` na pasta raíz 
do seu repositório e adicionar um arquivo `yml` com o seguinte conteúdo:

```yml showLineNumber title=".github/workflows/docusaurus-deploy.yml"
name: Deploy Docusaurus

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
# Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Allow one concurrent deployment
concurrency:
  group: "pages"
  cancel-in-progress: true

env:
  # Hosted GitHub runners have 7 GB of memory available, let's use 6 GB
  NODE_OPTIONS: --max-old-space-size=6144

jobs:
  build:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: latest

    - name: Install and Build
      run: |
        cd docs
        npm install
        npm run build
        mv build ../build
        
    - name: Setup Pages
      uses: actions/configure-pages@v3
        
    - name: Upload artifact
      uses: actions/upload-pages-artifact@v2
      with:
        path: ./build

    - name: Deploy to GitHub Pages
      id: deployment
      uses: actions/deploy-pages@v2
```

Pronto! Agora seu repositório vai entrar na pasta `docs`, instalar e construir 
a versão de deploy do docusaurus e fazer o deploy final para o seu github pages.
