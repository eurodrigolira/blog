---
title: "Recuperando o Lilo no Slackware"
slug: "recuperando-o-lilo-no-slackware"
date: 2013-11-21
category: 
  - "linux"
tag: 
  - "dicas"
  - "lilo"
  - "linux"
  - "slackware"
coverImage: "lilo.png"
---

[![lilo](images/lilo.png)](http://rodrigolira.eti.br/wp-content/uploads/2013/11/lilo.png)Salve Salve Pessoal!

Nessa ultima semana tive que reinstalar o Windows do meu notebook  (travando muito, hehehe) e tive que recuperar o lilo para poder utilizar o meu Slackware novamente, segue abaixo um passo a passo do que fiz:

1º Inicie o computador com um CD ou DVD do Slackware(pode ser outro SO, desde que seja linux):

2º Logue como root:

3º Monte a partição onde esta o Slackware com o comando abaixo:

```
#mount /dev/sdaX /mnt (o X é o numero da sua partição, observe que tem um espaço entre o X e o /mnt)
```

4º Entre dentro do /etc:

```
#cd /etc
```

5º Crie um link simbólico do lilo.conf do  /etc que foi montado no /mnt com o comando abaxio:

```
#ln -s /mnt/etc/lilo.conf
```

6º Reinstale o lilo com o comando abaixo:

```
#lilo
```

Pronto o LILO foi reinstalado com todos os parâmetros anteriores.

Até a próxima!
