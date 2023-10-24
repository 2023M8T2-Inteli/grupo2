---
title: Trabalhando com branches
sidebar_position: 6
---

# Boas Práticas ao Trabalhar com Branches: Pull e Rebase

Trabalhar com branches é uma abordagem comum e fundamental quando se utiliza sistemas de controle de versão como o Git. Porém, quando múltiplas pessoas estão colaborando em um mesmo projeto, é comum encontrar situações em que dois ou mais contribuidores modificam a mesma parte de um arquivo, levando a conflitos de merge durante um pull request. Este documento aborda boas práticas para se trabalhar com branches, focando especialmente em `pull` e `rebase` para evitar esses conflitos.

## 1. Crie Branches com Propósitos Claros

- **Nomeie claramente**: Os nomes dos branches devem ser descritivos e refletir o propósito ou a funcionalidade que está sendo trabalhada.
- **Uma tarefa, um branch**: Cada branch deve representar uma única tarefa ou funcionalidade para evitar grandes divergências do branch principal.

## 2. Mantenha o Branch Atualizado

É uma boa prática manter seu branch local sincronizado com as mudanças mais recentes do branch principal (geralmente, `main` ou `master`). Isso reduz a chance de conflitos.

- **Faça o Pull com frequência**: Puxe as mudanças mais recentes do branch principal regularmente.

```bash
git checkout main
git pull
```

- **Rebase com frequência**: Depois de garantir que o branch principal está atualizado, mude para o seu branch de trabalho e faça o rebase:

```bash
git checkout seu-branch
git rebase main
```

## 3. Use `rebase` Antes de Abrir um Pull Request

Ao terminar as alterações em seu branch e antes de abrir um pull request, é útil fazer um último rebase. Isso garante que seu branch esteja atualizado com as mudanças mais recentes do branch principal e que qualquer conflito potencial seja resolvido em sua máquina, não durante o pull request.

```bash
git checkout seu-branch
git rebase main
```

## 4. Resolva Conflitos Localmente

Se encontrar conflitos durante o rebase, o Git vai pausar e pedir para você resolvê-los. Após resolver cada conflito:

```bash
git add arquivo-com-conflito
git rebase --continue
```

Ao resolver todos os conflitos, seu branch estará pronto para ser mesclado com o principal sem problemas.

## Exemplo

Imagine que Alice e Bob estão trabalhando em um mesmo projeto. Ambos criaram branches separados para suas tarefas.

1. Alice completa sua tarefa e faz o merge no `main`.
2. Bob, ainda trabalhando em seu branch, decide que está pronto para fazer o merge. Antes disso, ele segue as boas práticas:
   
   a. Atualiza o `main`:
   
   ```bash
   git checkout main
   git pull
   ```

   b. Rebase seu branch:
   
   ```bash
   git checkout branch-do-bob
   git rebase main
   ```

3. Durante o rebase, Bob percebe um conflito em `arquivo.txt`. Ele o resolve manualmente, salva o arquivo, e então:

   ```bash
   git add arquivo.txt
   git rebase --continue
   ```

4. Com os conflitos resolvidos, Bob agora pode abrir seu pull request com confiança de que não haverá conflitos de merge.

**Conclusão**: Mantendo as práticas de pull e rebase em mente, é possível minimizar e resolver eficientemente conflitos, garantindo um fluxo de trabalho mais suave e colaborativo no Git.
