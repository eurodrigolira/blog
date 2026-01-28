---
title: "Transformando o CentOS em Oracle Linux"
date: 2017-05-24
categories: 
  - "linux"
  - "scripts"
tags: 
  - "centos"
  - "centos2ol-sh"
  - "linux"
  - "oracle-linux"
  - "scientific-linux"
---

[![](images/oraclelinux.png)](http://rodrigolira.eti.br/wp-content/uploads/2017/04/oraclelinux.png)

Salve Salve Pessoal!

Já imaginou poder transformar seu servidor **CentOS** em um **Oracle Linux** rodando apenas um script, sem precisar reinstalar todo o sistema novamente.

Isso é possível graças a um script desenvolvido pelo pessoal da Oracle, eles desenvolveram um script chamado **centos2ol.sh**.

**centos2ol.sh** pode converter seus sistemas **CentOS 5, 6** e **7** para o **Oracle Linux**. Ele também suporta o **Scientific Linux 5, 6** e **7**.

**O que o script faz?**

O script tem duas funções principais:

Ele troca os repositórios do yum para usar o servidor yum.oracle.com da Oracle e instala alguns pacotes necessários.

É isso aí! Você nem precisará reiniciar após a execução do script.

Execute os comandos abaixo como root, para transformar o **CentOS** ou  **Scientific Linux** em um **Oracle Linux**:

```
# curl -O https://linux.oracle.com/switch/centos2ol.sh

# sh centos2ol.sh
```

Ao final da execução do script execute:

```
# yum distro-sync
```

Pronto, seu sistema agora é um Oracle Linux :D

Até a próxima!

Maiores detalhes: https://linux.oracle.com/switch/centos/
