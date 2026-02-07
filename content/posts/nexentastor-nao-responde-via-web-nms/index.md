---
title: "NexentaStor não responde via Web (NMS)"
slug: "nexentastor-não-responde-via-web-(nms)"
date: 2016-09-15
categories: 
  - "labs"
  - "storage"
tags: 
  - "nexenta"
  - "nexentastor"
  - "storage"
---

Salve Salve Pessoal!

Hoje comecei a montar o meu storage para o meu novo homelab.

Quem acompanha o blog já sabe que costumo usar o NexentaStor Community Edition como solução de storage.

[https://nexenta.com/products/downloads/download-community-edition](https://nexenta.com/products/downloads/download-community-edition)

Pois bem, fiz a instalação do sistema tudo certinho, a maquina reiniciou normalmente, porém quando fui tentar acessar o sistema via web o mesmo não estava respondendo.

Dessa forma fui pesquisar sobre o possível motivo da mesma não respondendo, achei a solução no blog [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com/).

A solução é bem simple, através do console, entre no modo avançado, falei disso em outro post aqui no blog [CLIQUE AQUI](http://rodrigolira.eti.br/nexenta-expert-mode-shell/), depois basta executar os seguintes comando:

```
svcadm disable -st nms\:default

svcadm enable -rs nms\:default
```

Pronto, depois disso a interface web volta a responder normalmente.

Para maiores detalhes sobre os comandos você pode acessar o link abaixo:

[https://nexenta.com/sites/default/files/NexentaStor-FAQ.pdf](https://nexenta.com/sites/default/files/NexentaStor-FAQ.pdf)

Até a próxima :D
