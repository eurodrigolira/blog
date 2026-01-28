---
title: "iproute2 - Parte 3"
date: 2018-01-26
categories: 
  - "linux"
tags: 
  - "dummy"
  - "iproute2"
  - "linux"
  - "macvlan"
  - "qinq"
  - "vlan"
---

Salve Salve Pessoa!

Seguindo com nossa serie de posts sobre **iproute2**, vamos ver nesse post como criar interfaces especiais.

Se você não leu os posts anteriores, sugiro que leia nos links abaixo:

[iproute2 - Parte 01](http://rodrigolira.eti.br/iproute2-parte-01/)

[iproute2 - Parte 02](http://rodrigolira.eti.br/iproute2-parte-02/)

Algumas das interfaces citadas nesse post, podem ser novas para alguns de vocês, vou colocar um link como referência para as interfaces que são menos comuns no dia-a-dia, não vou explicar sobre cada uma delas para o post não ficar muito extenso.

Vamos ao que interessa :D

**Criar uma interface VLAN**

```
# ip link add name eth0.110 link eth0 type vlan id 110
```

Obs: O nome **eth0.100** é uma forma tradicional de nomeclatura da interface, mas não é obrigatório, podemos nomear como quisermos, preste atenção a interface que está lincada e ao id da vlan.

**Criar uma interface QinQ (VLAN Stacking)**

```
# ip link add name eth0.100 link eth0 type vlan proto 802.1ad id 100 (Cria a interface VLAN)
# ip link add name eth0.100.200 link eth0.100 type vlan proto 802.1q id 200 (Cria um cliente da interface VLAN)
```

Para maiores informações sobre o QinQ e seu uso, acesse o link abaixo:

[https://www.cisco.com/en/US/docs/ios/lanswitch/configuration/guide/lsw\_ieee\_802.1q.html#wp1050990](https://www.cisco.com/en/US/docs/ios/lanswitch/configuration/guide/lsw_ieee_802.1q.html#wp1050990)

**Criar uma interface Macvlan**

```
# ip link add name mvlan0 link eth0 type macvlan
```

Normalmente veremos o uso de macvlan em ambiente com virtualização ou com docker, para maiores informações sobre esse tipo de interface, acesse o link abaixo:

[https://docs.docker.com/engine/userguide/networking/get-started-macvlan/](https://docs.docker.com/engine/userguide/networking/get-started-macvlan/)

**Criar interfaces dummy**

```
# ip link add name dummy0 type dummy
```

Interfaces dummy, são interfaces de loopback, normalmente utilizadas para comunicação interna de programas dentro do mesmo sistema, para maiores informações, acesse o link abaixo:

[http://www.tldp.org/LDP/nag/node72.html](http://www.tldp.org/LDP/nag/node72.html)
