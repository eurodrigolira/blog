---
title: "Checando a qualidade de senha no Oracle Linux 7 com o pwscore"
slug: "checando-a-qualidade-de-senha-no-oracle-linux-7-com-o-pwscore"
date: 2017-06-21
categories: 
  - "linux"
tags: 
  - "oracle"
  - "oracle-linux"
  - "oracle-linux-7"
  - "pwmake"
  - "senhas"
---

[![](images/oraclelinux1.png)](http://rodrigolira.eti.br/wp-content/uploads/2017/06/oraclelinux1.png)

Salve Salve Pessoal!

**Pwscore** é uma ferramenta para verificar a qualidade de senha.

A ferramenta usa a biblioteca libpwquality para executar verificações de comprimento mínimo, verificação de dicionário entre outras verificações.

O pwscore mostra um índice de qualidade que pode variar entre 0 e 100.

O índice de qualidade da senha é relativo, mas em geral, os valores abaixo de 50 podem ser tratados como qualidade moderada e acima da qualidade bastante forte.

Seu uso é bastante simples, execute o comando **\# pwscore** e depois informe a senha que deseja testar.

```
[root@ol7 ~]# pwscore (comando)
Mudar123 (senha testada)
12 (resultado)
```

Use o comando **pwmake** para gerar novas senha aleatórias e realizar alguns testes. Para maiores informações sobre o pwmake acesse o link abaixo.

http://rodrigolira.eti.br/gerando-senhas-aleatorias-no-oracle-linux-7-com-pwmake/

O **pwscore** também está presente no **CentOS 7** e no **Red Hat 7**.

Até a próxima :D
