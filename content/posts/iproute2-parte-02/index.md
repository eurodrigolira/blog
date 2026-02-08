---
title: "iproute2 – Parte 02"
slug: "iproute2-parte-02"
date: 2018-01-17
category: 
  - "linux"
tag: 
  - "iproute2"
  - "linux"
---

Salve Salve Pessoal!

No post anterior dessa nova serie de posts, vimos que podemos visualizar, adicionar e remover um endereço IP utilizando o iproute2.

http://rodrigolira.eti.br/iproute2-parte-01/

Hoje vamos ver como visualizar e gerenciar tabela ARP e NDP e os links (interfaces), como por exemplo, mudar o MTU de uma interface.

Vamos logo ao que interessa :D

#### Gerenciamento da tabela ARP e NDP

Podemos verificar a tabela com o seguinte comando:

```
# ip neighbor show
```

Podemos especificar qual a versão do protocolo também:

```
# ip -4 neighbor show

# ip -6 neighbor show
```

Podemos verificar a tabela especificando uma determinada interface:

```
# ip neighbor show dev eth0
```

Também podemos limpar a tabela especificando a interface:

```
# ip neighbor flush dev eth0
```

Podemos adicionar uma entrada na tabela passando o IP e o MAC:

```
# ip neighbor add 192.168.0.1 lladdr AA:BB:CC:11:22:33 dev eth0
```

Assim como podemos adicionar, também podemos deletar:

```
# ip neighbor del 192.168.0.1 lladdr AA:BB:CC:11:22:33 dev eth0
```

#### Gerenciamento de Links(interfaces)

Existem várias possibilidades de gerenciamento de links, veremos algumas dessas possibilidades.

Podemos visualizar todos os links com o seguintes comandos:

```
# ip link show

# ip link list
```

Podemos especificar a interface que desejamos visualizar as informações:

```
# ip link show dev eth0

# ip link list dev eth0
```

Para desativar ou ativar a interface usamos os argumentos down e ip:

```
# ip link set dev eth0 down

# ip link set dev eth0 up
```

Podemos renomear uma interface para melhor compreensão:

```
# ip link set dev eth0 name lan
```

**Obs:** Para renomearmos uma interface, é necessário que a mesma não esteja em uso, precisamos desativar a interface como mostrado anteriormente. Essa alteração não será aplicada após a reinicialização do sistema.

Também podemos mudar o endereço MAC da interface:

```
# ip link set dev eth0 address 22:ce:e0:99:63:6f
```

Podemos mudar o MTU:

```
# ip link set dev eth0 mtu 9000
```

Podemos deletar link virtuais (tipos VLAN e Bridges)

```
# ip link delete dev br01
```

Podemos desabilitar ou habilitar multicast:

```
# ip link set eth0 multicast on
# ip link set eth0 multicast off
```

E por último, podemos habilitar ou desabilitar o arp:

```
# ip link set eth0 arp on
# ip link set eth0 arp off
```

Existem diversas outras possibilidades de uso, sintam-se a vontade para ler o manual do iproute2:

```
# man ip
```

Até o próximo post! :D
