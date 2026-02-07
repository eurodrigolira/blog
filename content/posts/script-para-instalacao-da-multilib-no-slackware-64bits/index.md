---
title: "Script para instalação do multilib no Slackware 64Bits"
slug: "script-para-instalação-do-multilib-no-slackware-64bits"
date: 2014-06-05
categories: 
  - "linux"
tags: 
  - "linux"
  - "multilib"
  - "scripts"
  - "slackware"
  - "software-livre"
---

[![slackware.linux_multilib](images/slackware.linux_multilib.png)](http://rodrigolira.eti.br/wp-content/uploads/2014/06/slackware.linux_multilib.png)Salve Salve Pessoal!

Hoje precisei instalar o multilib para compatibilidade de alguns softwares 32bits no meu Slackware 64bits.  Para que não sabe o Slackware 64bits é um SO puro, ou seja, não contém pacotes 32bits. Para maiores detalhes click [AQUI](http://www.slackware.com/~alien/multilib/).

Dessa forma resolvi elaborar um script para automatizar essa tarefa, mas resolvi pesquisar antes para saber se alguém já tinha elaborado algum, e descobri um, porém não serviria para minha versão atual, dessa forma fiz algumas modificações para a minha realidade, e imagino que para de vocês também, esse script serve para qualquer versão do slackware desde que não seja para a versão current.<!--more-->

Abaixo segue o script:

```
#!/bin/bash
# 
# Rodrigo Lira - eu@rodrigolira.eti.br
# Script de instalação do multilib em qualquer versão do Slackware 64Bits
# OBS: Este script não instala a versão current 
#
# Script Original
# Noilson Caio Teixeira de Araújo - caiogore[at]gmail[dot]com
# Script de instalação do multilib no slackware 13.37.0
# URL - http://ncaio.wordpress.com/2011/08/22/slackware-13-37-com-multlib/#more-378
#
# Definição das Variáveis
binwget=$(which wget)
binlftp=$(which lftp)
binawk=$(which awk)
binupgradepkg=$(which upgradepkg)
version=`cut -d " " -f 2 /etc/slackware-version`
wgetopt="-q --delete-after -T 5 -t 1"
url="http://slackware.com/~alien/multilib/"
#
# Teste para saber se a URL está online
echo Testando a URL
sleep 2
$binwget $wgetopt $url
retorno="$?"
if [ "$retorno" != 0 ]
then
 echo "$url - [URL não encontrada]"
 exit 1
fi
echo "Teste realizado com sucesso!"
sleep 2
#
# Realizando download dos arquivos
echo "Realizando download"
$binlftp -c "open $url ; mirror $version" > /dev/null
retornolftp="$?"
if [ "$retornolftp" != 0 ]
 then
 echo "[ Download falhou ]"
 exit 1
fi
echo "Download realizado com sucesso!"
#
# Instalação dos pacotes baixados
echo "Instalar os pacotes agora? (y / n)"
read retornoinst
if [ "$retornoinst" = "y" ]
 then
 $binupgradepkg --reinstall --install-new $version/*.t?z
 $binupgradepkg --install-new $version/slackware64-compat32/*-compat32/*.t?z
fi
echo "Pacotes instalados com sucesso!"
```

Irei melhorar este script sempre que possível, aceito a ajuda de todos para um melhor desenvolvimento do mesmo!

Link para script original:

[http://ncaio.wordpress.com/2011/08/22/slackware-13-37-com-multlib/](http://ncaio.wordpress.com/2011/08/22/slackware-13-37-com-multlib/)

Link para maiores detalhes da multilib:

[http://alien.slackbook.org/dokuwiki/doku.php?id=slackware:multilib](http://alien.slackbook.org/dokuwiki/doku.php?id=slackware:multilib)

Até a próxima :)

<

p style="text-align: justify;">
