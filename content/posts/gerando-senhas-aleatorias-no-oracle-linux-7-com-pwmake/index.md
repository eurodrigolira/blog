---
title: "Gerando senhas aleatórias no Oracle Linux 7 com pwmake"
slug: "gerando-senhas-aleatorias-no-oracle-linux-7-com-pwmake"
date: 2017-06-19
category: 
  - "linux"
tag: 
  - "linux"
  - "oracle"
  - "oracle-linux"
  - "oracle-linux-7"
  - "pwmake"
---

[![](images/oraclelinux1.png)](http://rodrigolira.eti.br/wp-content/uploads/2017/06/oraclelinux1.png)

Salve Salve Pessoal!

O **pwmake** é uma ferramenta simples e configurável para gerar senhas aleatórias. A ferramenta permite que você especifique o número de bits que são usados para gerar a senha.

A entropia é retirada de /dev/urandom.

O número mínimo de bits é 56, normalmente os bits utilizados são os seguintes, 56, 64, 80, 128 ou 256.

[![](images/Oracle-Linux-7-VMware-Workstation-2017-06-19-10.45.39.png)](http://rodrigolira.eti.br/wp-content/uploads/2017/06/Oracle-Linux-7-VMware-Workstation-2017-06-19-10.45.39.png)

Como podemos ver na imagem acima, o tamanho da senha vai depender de sua paranoia.

A complexidade e outras opções de configuração do pwmake podem ser configuradas no arquivo  /etc/security/pwquality.conf.

O **pwmake** também está presente no **CentOS 7** e no **Red Hat 7**.

Até a próxima :D
