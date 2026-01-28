---
title: "Instalação do Docker no Oracle Linux 7"
date: 2017-04-26
categories: 
  - "devops"
  - "linux"
tags: 
  - "docker"
  - "linux"
  - "oracle"
  - "oracle-linux"
---

[![](images/dockericon-300x102.png)](http://rodrigolira.eti.br/wp-content/uploads/2017/04/dockericon.png)

Salve Salve Pessoal!

Depois de um tempo sem postar nada devido alguns compromissos, venho mostrar como instalar o Docker no Oracle linux 7.

O processo é muito simples, porém precisamos habilitar o  repositório ol7\_addons do Oracle Linux 7.

Edite o arquivo **/etc/yum.repos.d/public.repo** e habilite o **ol7\_addons**, para habilitar basta colocar o número **1** no lugar do **0** em **enabled**.

```
[ol7_addons]
name=Oracle Linux $releasever Add ons ($basearch)
baseurl=http://yum.oracle.com/repo/OracleLinux/OL7/addons/$basearch/
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-oracle
gpgcheck=1
enabled=1
```

Atualize os repositórios.

```
# yum update
```

Instale o pacote do Docker.

```
# yum install docker-engine
```

Habilite o docker na inicialização do sistema.

```
# systemctl enable docker
```

Inicie o serviço do Docker.

```
# systemctl start docker
```

Verifique o status do Docker.

```
#systemctl status docker
```

Pronto, é isso ai, até a próxima :D
