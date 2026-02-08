---
title: "Interface Bond no Oracle VM Server"
slug: "interface-bond-no-oracle-vm-server"
date: 2016-11-06
category: 
  - "labs"
  - "linux"
  - "virtualizacao"
tag: 
  - "labs"
  - "linux"
  - "oracle"
  - "oracle-linux"
  - "oracle-vm-manager"
  - "oracle-vm-server"
---

Salve Salve Pessoal!

Nesse post vou mostrar as opções de configuração da interface bond no Oracle VM Server.

[![network_bonding_mode4](images/network_bonding_mode4.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/network_bonding_mode4.png)

O bond é o responsável por fazer a agregação de interfaces no Oracle VM, na versão atual (3.4.2) é possível configurar o bond com as seguintes opções:

**Active Backup:** Usa apenas uma interface do bond, caso a interface ativa falhe, outra interface assume o lugar da interface que falhou.

**Link Aggregation:** Faz uma agregação das interfaces, que resulta em um maior throughput.

**Load Balanced:** Faz um balanceamento de carga, dividindo o pacotes trafegados entre as interfaces.

Vamos ao que interessa :D

Acesse o **Oracle VM Manager** e verifique as interfaces disponíveis no host, clique em cima do host e depois selecione **Ethernet Ports** em **Perspective**, como podemos verificar, o host **ovs-03.lab.local** possui **4 interfaces** de rede, sendo que a interface **eth0** já faz parte do **bond0**, outro detalhe é que apenas a **eth0** está com o status **Port UP**.

[![oracle-vm-server-01](images/Oracle-VM-Server-01-1-1024x420.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Oracle-VM-Server-01-1.png)

Agora em **Perspective** selecione **Bond Ports**, podemos verificar agora qual o tipo de configuração que o nosso bond está utilizando, nessa caso é o **Active Backup** e o endereço **IP** que está configurado na interface.

**Active Backup é a configuração padrão do bond do Oracle VM Server** ;)

[![oracle-vm-server-02](images/Oracle-VM-Server-02-1024x414.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Oracle-VM-Server-02.png)

Selecione a interface bond e clique em **editar,** ou clique com o botão direito do mouse sobre a interface bond e clique em **editar**.

[![oracle-vm-server-03](images/Oracle-VM-Server-03-1024x433.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Oracle-VM-Server-03.png)

Na aba que se abriu, temos várias informações, o **host** que estamos configurando, o **bond** que nesse caso é o **bond0**, endereço **IP** e etc, o que temos que modificar nesse caso é apenas o tipo de **Bonding** e quais interfaces vão fazer parte dele.

No nosso caso já estamos com a interface **eth0** fazendo parte do **bond0** e o tipo de bond, configurado como **Active Backup**.

[![oracle-vm-server-04](images/Oracle-VM-Server-04-1024x413.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Oracle-VM-Server-04.png)

Vamos configurar o nosso **bond0** como **Link Aggreation** e Inserir a interface **eth1** ao nosso **bond0**, em **Bonding** selecione **Link Aggregation**, depois selecione a interface **eth1** e clique no ícone com **seta para a direita**, feito isso clique em **OK**.

[![oracle-vm-server-05](images/Oracle-VM-Server-05-1024x415.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Oracle-VM-Server-05.png)

Agora podemos verificar que o **Bond Mode** está como **Link Aggregation** e em **Ethernet Ports** temos **eth0** e **eth1**.

[![oracle-vm-server-06](images/Oracle-VM-Server-06-1024x414.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Oracle-VM-Server-06.png)

Agora vamos criar um novo bond e configurar como **Load Balance** usando as interfaces **eth2** e **eth3**. Clique em cima do ícone com o sinal de adição.

[![oracle-vm-server-07](images/Oracle-VM-Server-07-1024x412.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Oracle-VM-Server-07.png)

Na aba que se abri configure de seguinte forma:

**Interface Name:** bond1

**Addresing:** Static

**IP:** 192.168.1.37 (Pode ser diferente acordo com seu lab)

**Netmask:** 255.255.255.0 (Pode ser diferente acordo com seu lab)

**Bonding:** Load Balanced

**Selected Ports:** eth2 e eth3

Depois de tudo configurado clique em **OK**.

[![oracle-vm-server-09](images/Oracle-VM-Server-09-1024x416.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Oracle-VM-Server-09.png)

Pronto, um novo bond foi criado, como podemos ver na imagem abaixo.

[![oracle-vm-server-10](images/Oracle-VM-Server-10-1024x414.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Oracle-VM-Server-10.png)

Espero que tenham gostado do post!

Até a próxima :D
