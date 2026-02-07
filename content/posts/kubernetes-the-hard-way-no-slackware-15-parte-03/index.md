---
title: "Kubernetes The Hard Way no Slackware 15 – Parte 03"
slug: "kubernetes-the-hard-way-no-slackware-15-parte-03"
date: 2023-10-07
categories: 
  - "kubernetes"
  - "linux"
tags: 
  - "kubernetes"
  - "kubernetes-the-hard-way"
  - "linux"
  - "slackware"
---

[![](images/k8s-slackware.png)](images/k8s-slackware.png)

Salve Salve Pessoal!

Dando continuidade a nossa serie **Kubernetes The Hard Way no Slackware 15**, neste post vamos ver as configurações das máquina virtual e um vídeo demostrando a instalação do Slackware 15.

Para quem ainda não leu os posts anteriores, só clicar nos links abaixo.

[Kubernetes The Hard Way no Slackware 15 – Parte 01](https://rodrigolira.eti.br/kubernetes-the-hard-way-no-slackware-15-parte-01/)

[Kubernetes The Hard Way no Slackware 15 – Parte 02](https://rodrigolira.eti.br/kubernetes-the-hard-way-no-slackware-15-parte-02/)

Por padrão sempre uso o VMware ESXi para meus laboratórios, mas vocês podem usar qualquer software de virtualização, VirtualBox, VMware Workstation, etc.

Abaixo uma tabela com as configurações de nome, ip e hardware que estou usando em cada máquina virtual.

| **HOSTNAME** | **IP** | **CPU** | **MEMORIA** | **DISCO** |
| --- | --- | --- | --- | --- |
| k8s-lb | 10.20.30.80 | 1 | 1 GB | 40 GB |
| k8s-cp-01 | 10.20.30.81 | 2 | 2 GB | 40 GB |
| k8s-cp-02 | 10.20.30.82 | 2 | 2 GB | 40 GB |
| k8s-cp-03 | 10.20.30.83 | 2 | 2 GB | 40 GB |
| k8s-node-01 | 10.20.30.84 | 2 | 4 GB | 40 GB |
| k8s-node-02 | 10.20.30.85 | 2 | 4 GB | 40 GB |
| k8s-node-03 | 10.20.30.86 | 2 | 4 GB | 40 GB |

O vídeo avaixo demostra a instalação do Slackware 15 no padrão que usei para o laborário.

<iframe title="YouTube video player" src="https://www.youtube.com/embed/JxbJ7I611zc?si=Tnp8mxA1JiIPykB8" width="650" height="400" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

Após terminar de instalar o sistema operacional, basta clonar a máquina e alterar as configurações de hardware, nome e endereçamento IP.

Por enquanto é isso pessoal, até o próximo post!

:D

Referência:

[https://github.com/kelseyhightower/kubernetes-the-hard-way/blob/master/docs/03-compute-resources.md](https://github.com/kelseyhightower/kubernetes-the-hard-way/blob/master/docs/03-compute-resources.md)
