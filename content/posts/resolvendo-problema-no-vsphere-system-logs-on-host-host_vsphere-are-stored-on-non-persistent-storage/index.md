---
title: "Resolvendo problema no vSphere - System logs on host \"HOST_VSPHERE\" are stored on non-persistent storage"
date: 2015-06-29
categories: 
  - "virtualizacao"
tags: 
  - "kb-2032823"
  - "vmware"
  - "vsphere-5-0"
  - "vsphere-5-1"
  - "vsphere-5-5"
  - "vsphere-6"
---

[![vmware-kb](images/vmware-kb.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/vmware-kb.png)Salve Salve Pessoal!

Estava configurando o meu laboratório para VCP6-DCV quando me deparei com a seguintes mensagem "System logs on host vsphere-03.lab.local are stored on non-persistent storage", achei estranho e fui pesquisar para saber melhor sobre o problema, que é basicamente o seguinte, os logs não estão sendo gravados em disco, dessa forma você tem que adicionar o caminho manualmente para que os mesmos possam ser gravados em disco.

Este problema já foi diagnosticado pela VMware "**KB 2032823**".

Segue abaixo um passo-a-passo de como resolver o problema:

1 - Abra p vSphere Client e selecione o host, no meu caso o vsphere-03.lab.local:<!--more-->

[![print1](images/print11-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/print11.png)

2 - Clique em **Configuration** > **Advanced Settings**:

[![print2](images/print2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/print2.png)

3 - Na aba lateral esquerda clique em **Syslog** > **global**, observe na opção **Syslog.global.logDir** ele não está apontando para nenhum storage (disco):

[![print3](images/print3-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/print3.png)

4 - Substitua o seu conteúdo por **\[SEU\_STORAGE\]/systemlog**, observe que no meu caso o nome do meu storage local é DAS\_03, caso você não tenha renomeado o seu storage local, ou seja, o disco onde você instalou o vSphere ele deve estar como datastore, feito isso basta clicar em OK.

[![print4](images/print41-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/print41.png)

5 - Pronto, problema resolvido.

[![print5](images/print51-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/print51.png)

Espero ter ajudado, até a próxima :D

Referência:

[http://kb.vmware.com/selfservice/microsites/search.do?language=en\_US&cmd=displayKC&externalId=2032823](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=2032823)
