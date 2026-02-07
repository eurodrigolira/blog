---
title: "Instalação do Apache no Oracle Linux 7"
slug: "instalação-do-apache-no-oracle-linux-7"
date: 2017-06-13
categories: 
  - "linux"
tags: 
  - "apache"
  - "linux"
  - "oracle"
  - "oracle-linux"
---

[![](images/oraclelinux1.png)](http://rodrigolira.eti.br/wp-content/uploads/2017/06/oraclelinux1.png)Salve Salve Pessoal!

Uma vez ou outra tenho a necessidade de instalar um servidor web em uma vm, seja para importar uma imagem do tipo .iso para dentro do Oracle VM, as vezes para que os meus alunos possam pegar o materia do curso sem a necessidade de estar passando por pendrive.

Nesse post vou mostrar como instalar e configurar o Apache no Oracle Linux 7,  de forma que possa vim a facilitar um pouco sua vida.

Siga os passos abaixo, execute os comando como usuário root.

1 - Faça a instalação do Apache:

```
# yum install httpd -y
```

2 - Inicie o serviço.

```
# systemctl start httpd
```

3 - Caso deseje habilitar o serviço para iniciar junto com o sistema.

```
# systemctl enable httpd
```

4 - Cheque se existe algum erro de configuração.

```
# apachectl configtest
```

5 - Libere o serviço no firewall.

```
# firewall-cmd --zone=zona --add-service=http

# firewall-cmd --permanent --zone=zona --add-service=http
```

**Obs:** Substitua a o nome **zona** dos comando acima pela zona atual que seu firewalld está utilizando, caso não saiba execute o comando abaixo para descobrir.

```
# firewall-cmd --get-default-zone
```

Pronto, depois disso seu servidor já estará pronto para uso.

Até a próxima :D
