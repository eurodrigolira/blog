---
title: "Update ESXi Embedded Host Client v1.9.1"
date: 2016-09-20
categories: 
  - "labs"
  - "virtualizacao"
---

Salve Salve Pessoal!

Saiu uma nova versão do **ESXi Embedded Host Client** a **versão 1.9.1**, o que achei muito legal é que o próprio **ESXi Embedded Host Client v1.8.1** foi quem me alertou sobre essa atualização, desta vez vamos fazer está atualização usando a interface web.

Após logar no seu host com a versão **ESXi Embedded Host Client v1.8.1** ele vai abrir a tela **Client update available**, informando da atualização, para atualizar basta clicar em **Update**:

[![captura-de-tela-2016-09-19-as-22-40-44](images/Captura-de-Tela-2016-09-19-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/09/Captura-de-Tela-2016-09-19-a?s-22.40.44.png)

Vai abri a tela **Install Update** com a url para atualização do **.vib,** basta clicar em **Update** novamente:

[![captura-de-tela-2016-09-19-as-22-41-01](images/Captura-de-Tela-2016-09-19-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/09/Captura-de-Tela-2016-09-19-a?s-22.41.01.png)

Vai aparecer uma tela de Warning, em nosso caso vamos ignorar e clicar em **Continue**:

[![captura-de-tela-2016-09-19-as-22-41-11](images/Captura-de-Tela-2016-09-19-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/09/Captura-de-Tela-2016-09-19-a?s-22.41.11.png)

Verifique a aba **Recent Task**, veja que o pacote está sendo atualizado:

[![captura-de-tela-2016-09-19-as-23-12-35](images/Captura-de-Tela-2016-09-19-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/09/Captura-de-Tela-2016-09-19-a?s-23.12.35.png)

Depois disso basta atualizar a página e verificar a versão:

Via navegador:

```
Host > Manage > Packages:
```

[![captura-de-tela-2016-09-19-as-23-13-24](images/Captura-de-Tela-2016-09-19-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/09/Captura-de-Tela-2016-09-19-a?s-23.13.24.png)

Via console:

```
# esxcli software vib list | grep esx-ui
```

[![captura-de-tela-2016-09-19-as-23-00-58](images/Captura-de-Tela-2016-09-19-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/09/Captura-de-Tela-2016-09-19-a?s-23.00.58.png)

**ESXi Embedded Host Client** atualizado para a versão **1.9.1**.

Até a próxima :D
