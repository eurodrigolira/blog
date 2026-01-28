---
title: "Lab Oracle VM Server - Parte 1"
date: 2016-05-28
categories: 
  - "labs"
  - "linux"
  - "virtualizacao"
tags: 
  - "nexenta"
  - "oracle-linux"
  - "oracle-vm-server"
  - "virtualizacao"
---

Salve Salve Pessoal!

Bem, depois de um bom tempo sem realizar nenhum post sobre laboratórios, venho iniciar uma nova serie, desta vez vamos montar um lab sobre o Oracle VM Server.

O Oracle VM Server é a solução de virtualização da Oracle, é uma plataforma totalmente gratuita, ou seja, custo zero, e desenvolvida e mantida por uma das maiores empresas de TI do mundo, a gigante **Oracle**.<!--more-->

Não vou me aprofundar em falar sobre a solução, abaixo alguns links para conhecer um pouco mais sobre a plataforma:

Visão Geral :

[http://www.oracle.com/us/technologies/virtualization/oraclevm/overview/index.html](http://www.oracle.com/us/technologies/virtualization/oraclevm/overview/index.html)

Recursos:

[http://www.oracle.com/us/technologies/virtualization/oraclevm/resources/index.html](http://www.oracle.com/us/technologies/virtualization/oraclevm/resources/index.html)

Especificações e Requerimentos:

[http://www.oracle.com/us/technologies/virtualization/oraclevm/specifications/index.html](http://www.oracle.com/us/technologies/virtualization/oraclevm/specifications/index.html)

Documentação completa:

[http://www.oracle.com/technetwork/server-storage/vm/documentation/index.html](http://www.oracle.com/technetwork/server-storage/vm/documentation/index.html)

A Oracle também disponibiliza um lab pronto para você testar a solução, são arquivos OVA que você pode fazer o deploy no VirtualBox, você pode baixar no link abaixo:

[http://www.oracle.com/technetwork/server-storage/vm/downloads/hol-oraclevm-2368799.html](http://www.oracle.com/technetwork/server-storage/vm/downloads/hol-oraclevm-2368799.html)

Para o nosso lab nós vamos fazer a instalação do zero, criar toda a parte de rede, pool, storage, repositórios e etc.

No meu caso vou utilizar o vSphere como virtualizador para o lab, mas você pode usar o próprio VirtualBox da Oracle ou o VMware Workstation.

Abaixo um pequeno esborço da arquitetura do lab:

[![Lab Oracle](images/Lab-Oracle-1024x467.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/05/Lab-Oracle.png)

Imagino que nesse momento você já tinha dado uma olhada nos requerimentos para a instalação da solução, no caso do meu lab vou utilizar a seguinte configuração de hardware para cada VM.

Oracle VM Server - OVS-01 / OVS-02

```
4GB de RAM

2  Processadores

1 Disco de 40GB

4 Placas de Rede
```

Oracle VM Manager - OVM

```
4GB de RAM

2  Processadores

1 Disco de 40GB

1 Placa de Rede
```

Storage (Nexenta)

```
1GB de RAM

1  Processador

1 Disco de 5GB para o Sistema Operacional

1 Disco de 50GB para NFS

1 Disco de 100GB para iSCSI

1 Placa de Rede
```

Para maiores detalhes sobre a instalação e configuração do Nexenta, acesse os links abaixo:

http://rodrigolira.eti.br/meu-lab-vmware-parte-02-storage-com-nexenta/

http://rodrigolira.eti.br/lab-vcp6-dcv-parte-3/

Antes de mais nada, precisamos baixar todas as ISOs para fazer a instalação do lab, abaixo segue um passo-a-passo do procedimento para download:

1 - Acesso o link abaixo:

[https://edelivery.oracle.com/osdc/faces/SearchSoftware](https://edelivery.oracle.com/osdc/faces/SearchSoftware)

[![oracle-01](images/oracle-01-1024x515.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/05/oracle-01.png)

2 - Entre com seu usuário e senha, caso não tenha, faço o registro:

[![oracle-02](images/oracle-02-1024x512.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/05/oracle-02.png)

3 - Pesquise e selecione **Oracle VM Server**:

[![oracle-03](images/oracle-03-1024x510.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/05/oracle-03.png)

4 - Selecione a arquitetura **x86 64 bit** e clique em **Select**:

[![oracle-06](images/oracle-06-1024x511.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/05/oracle-06.png)

 

5 - Clique em **Continue**:

[![oracle-07](images/oracle-07-1024x514.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/05/oracle-07.png)

6 - Desmarque a opção **Oracle VM Agent for SPARC** e clique em **Continue**:

[![oracle-08](images/oracle-08-1024x514.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/05/oracle-08.png)

7 - Aceite os termos:

[![oracle-09](images/oracle-09-1024x512.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/05/oracle-09.png)

8 - Será solicitado a instalação do **Download Manager da Oracle**, instale e clique em **Download**:

[![oracle-10](images/oracle-10-1024x512.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/05/oracle-10.png)

9 - O download é iniciado:

[![oracle-11](images/oracle-11-1024x514.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/05/oracle-11.png)

Pronto, depois do download nós teremos disponível a ISO do Oracle VM Server e Manager, além do driver paravirtualizado para windows.

Bem, por enquanto é só, espero que tenham gostado desse post, façam o download e até o próximo post :D
