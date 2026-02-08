---
title: "Script para backup do OpenWrt"
slug: "script-para-backup-do-openwrt"
date: 2015-12-23
category: 
  - "linux"
  - "scripts"
tag: 
  - "backup"
  - "linux"
  - "openwrt"
  - "script"
---

Salve Salve Pessoal!

Vou adicionar aqui, um simples script que criei para realizar backup das configurações do OpenWrt.

Segue o Script abaixo:

```
#!/bin/sh
# Rodrigo Lira
# E-mail - eurodrigolira@gmail.com
# Script para backup do OpenWrt

# VARIAVEIS
DATA=`date +%d_%m_%Y`
NOME=backup-openwrt-$DATA.tar.gz

# CRIANDO O BACKUP DENTRO DO /tmp
sysupgrade --create-backup /tmp/$NOME

# ENVIA O ARQUIVO VIA SCP PARA SERVIDOR DE BACKUP
scp /tmp/$NOME root@IP_DE_DESTINO:/PASTA_DE_DESTINO

# APAGA O ARQUIVO DE BACKUP
rm /tmp/$NOME
```

Este script faz o backup utilizando autenticação sem senha, instale o pacote openssh-client-utils para poder gerar as chaves para autenticação sem senha:

```
opkg install openssh-client-utils
```

O resto é o padrão, não esqueça de adicionar no cron.

Até a próxima :D

Referência:

[https://wiki.openwrt.org/doc/howto/generic.backup](https://wiki.openwrt.org/doc/howto/generic.backup)
