---
title: "Desabilitar IPv6 no Oracle Linux 7"
slug: "desabilitar-ipv6-no-oracle-linux-7"
date: 2017-05-03
categories: 
  - "linux"
tags: 
  - "ipv6"
  - "linux"
  - "oracle"
  - "oracle-linux"
---

Salve Salve Pessoal!

Uma das coisas que faço por padrão quando faço uma nova instalação de um sistema operacional, é desabilitar o IPv6, nunca tive a necessidade de usa-lo, dessa forma quando preciso resolver algum problema referente a rede, os comando **ifconfig** ou **ip** ficam mais limpos.

Para desabilitar o IPv6 no Oracle Linux 7, basta editar o arquivo **/etc/sysctl.conf**, e inserir as seguintes linhas abaixo.

```
net.ipv6.conf.all.disable_ipv6 = 1

net.ipv6.conf.default.disable_ipv6 = 1
```

Caso deseje desabilitar em uma interface específica, como por exemplo **enp0s3** insira a linha abaixo.

```
net.ipv6.conf.enp0s3.disable_ipv6 = 1
```

Agora basta executar o comando abaixo.

```
sysctl -p
```

Pronto, o IPv6 foi desabilitado com sucesso.

Até a próxima :D
