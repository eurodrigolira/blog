---
title: "Hardening Red Hat/CentOS 7 – Parte 02 (Controlando o acesso por SSH)"
slug: "hardening-red-hat-centos-7-parte-02-controlando-o-acesso-por-ssh"
date: 2018-02-05
categories: 
  - "linux"
  - "seguranca"
tags: 
  - "centos-7"
  - "hardening"
  - "linux"
  - "oracle-linux-7"
  - "red-hat-7"
  - "seguranca"
  - "ssh"
---

Salve Salve Pessoal!

Vamos para mais um post da serie de Hardening em **Red Hat/CentOS 7**.

No post anterior vimos como controlar o acesso de root em diversas formas de login. até mesmo por SSH, se não viu o primeiro post, sugiro que acesse e leia, segue o link:

[Hardening Red Hat/CentOS 7 – Parte 01 (Controlando o acesso de root)](https://rodrigolira.eti.br/hardening-red-hat-centos-7-parte-01-controlando-o-acesso-de-root/)

No post de hoje, vamos mostrar como controlar o acesso via **SSH** para todos os usuários do sistema, se não entende bem o que é o **SSH** sugiro que leia um pouco sobre o projeto **OpenSSH** no link abaixo:

[https://www.openssh.com/manual.html](https://www.openssh.com/manual.html)

As formas de acesso via **SSH** podem ser através de chave pública ou através de login e senha.

O arquivo de configuração padrão do **OpenSSH** é o **/etc/ssh/sshd\_config**, nele podemos definir vários parâmetros de autenticação, esse arquivo só pode ser alterado por um usuário administrador do sistema.

Outro ponto interessante de falar, é que a partir da versão **7.6/7.6p1** o **OpenSSH** só suporta o protocolo com a versão 2, o protocolo com a versão 1 foi removido, o que já devia ter acontecido a muito tempo(minha opnião).

**OpenSSH Release Notes** **OpenSSH 7.6/7.6p1** (2017-10-03) - [https://www.openssh.com/releasenotes.html](https://www.openssh.com/releasenotes.html)

Vamos ao que interessa :D

A primeira coisa de devemos mudar no arquivo de configuração do SSH é a porta, por padrão o SSH roda na porta **22/tcp**, é uma porta bastante explorada por ataques de brute force principalmente, dessa forma devemos usar uma porta alta aleatória, como por exemplo **54768**, por padrão no **Red Hat/CentOS 7** a linha que faz referência a porta vem comentada, é necessário remover o comentário e mudar o número.

**#Port 22** (padrão do arquivo de configuração)

**Port 54768** (remover o comentário e mudar a porta)

Alguns detalhes importantes quanto a porta, por padrão o firewall libera a porta 22, como estamos mudando a porta, temos que liberar a nova porta no firewall também, execute os seguintes comandos:

```
# firewall-cmd --permanent --add-port=54768/tcp

# firewall-cmd --reload
```

Se vocês estiver com o SELinux como enforcing, precisamos informa-lo sobre está mudança, execute o comando abaixo:

```
# semanage port -a -t ssh_port_t -p tcp 54768
```

Agora basta reiniciar o serviço.

```
# systemctl restart sshd.service (reiniciar o serviço)
```

Podemos especificar a família do protocolo, por padrão é aceito conexões tanto IPv4 quanto IPv6.

```
AddressFamily any (qualquer um)

AddressFamily inet (somente IPv4)

AddressFamily inet6 (somente IPv6)
```

Também podemos especificar um host ou rede que pode se conectar.

```
ListenAddress 0.0.0.0 (aceita qualquer conexão IPv4)

ListenAddress 192.168.0.1 (aceita qualquer conexão do host)

ListenAddress 192.168.0.0/24 (aceita qualquer conexão da rede)
```

**Obs:** O mesmo se aplica a IPv6

Podemos permite ou não o login de root.

```
PermitRootLogin yes (sem comentário com yes no final, permitimos o login de root)

PermitRootLogin no (sem comentário com no no final, proibimos o login de root)

PermitRootLogin prohibit-password ou without-password (permite o login de root apenas com chave)
```

Podemos permite ou não o login de usuários.

```
DenyUsers joao lucia (bloqueamos o acesso dos usuários João e Lúcia)

AllowUsers maria jose (permitimos o acesso dos usuários maria e jose)
```

Também podermos permite ou bloquear um determinado grupo de usuários.

```
DenyGroups estagiarios (bloqueia o acesso do grupo estagiarios)

AllowGroups administradores  (permitimos o acesso do grupo administradores)
```

**Obs:** Existe uma ordem de processamento quando usamos usuários e grupos, a ordem é a seguintes:

**DenyUsers > AllowUsers > DenyGroups > AllowGroups**

Podemos fazer com que a conexão seja interrompida após período de inatividade, esse período é dado em segundos.

**ClientAliveCountMax 0** (numero de mensagens checkalive enviada pelo servidor para o cliente)

**ClientAliveInterval 300** (tempo máximo em segundos)

Existem diversas outras possibilidades de configuração do SSH, leia o manual para saber tudo o que podemos fazer com ele.

Até a próxima :D
