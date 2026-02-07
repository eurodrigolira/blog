---
title: "Instalação do VMware vCenter Server Appliance 6.7"
slug: "instalacao-do-vmware-vcenter-server-appliance-6-7"
date: 2018-08-09
categories: 
  - "labs"
  - "virtualizacao"
tags: 
  - "labs"
  - "vcsa"
  - "vcsa-6-7"
  - "virtualizacao"
  - "vmware"
  - "vmware-vsphere-6-7"
  - "vsphere-6-7"
---

[![](images/migrate2vcsa-232x300.png)](images/migrate2vcsa.png)

Salve Salve Pessoal!

Depois de um tempo sem um LAB do vSphereEstou refazendo meu LAB, então já estou partindo para a versão VMware vSphere 6.7.

Para começar, vamos ter uma visão geral sobre vCenter Server Appliance 6.7.

O VCSA é uma máquina virtual baseada em Linux, é otimizada e pré-configurada para executar o vCenter Server e os serviços associados, pelo fato de ser uma máquina virtual pré-configurada acaba reduzindo o tempo de implementação e reduzindo os custos se comparado a solução baseada em Windows, pois não precisamos de licença para o Sistema Operacional.

O vCenter Server Appliance é composto por diversos softwares, entre eles podemos citar:

Sistema Operacional Photon OS 1.0

PostgreSQL

Update Manager

Entre outros...

Os pré-requisitos de hardware são variados e depende do tamanho do seu ambiente, segue abaixo uma tabela:

**CPU e Memoria**

| **Hosts / VMs** | **vCPU** | **Memoria** |
| --- | --- | --- |
| até 10 hosts ou 100 vms | 2 | 10 GB |
| até 100 hosts ou 1.000 vms | 4 | 16 GB |
| até 400 hosts ou 4.000 vms | 8 | 24 GB |
| até 1.000 hosts ou 10.000 vms | 16 | 32 GB |
| até 2.000 hosts ou 35.000 vms | 24 | 48 GB |

**Storage**

| **Hosts / VMs** | **Padrão** | **Grande** | **Extra Grande** |
| --- | --- | --- | --- |
| até 10 hosts ou 100 vms | 250 GB | 775 GB | 1650 GB |
| até 100 hosts ou 1.000 vms | 290 GB | 820 GB | 1700 GB |
| até 400 hosts ou 4.000 vms | 425 GB | 925 GB | 1805 GB |
| até 1.000 hosts ou 10.000 vms | 640 GB | 990 GB | 1870 GB |
| até 2.000 hosts ou 35.000 vms | 980 GB | 1030 GB | 1910 GB |

Agora vamos ao que interessa :D

**1** - Se estiver usando o Windows 10 como é o meu caso basta montar a ISO do VCSA. Como podemos verificar, existem três pastas com o nome vcsa e cada uma é um tipo de instalação. No nosso caso vamos fazer a instalação via interface.

[![](images/01.png)](images/01.png)

**2** - Entre na pasta **vcsa-ui-install** e depois em **win32**, se estiver usando Linux ou Mac entre nas pastas respectivas a cada sistema, execute o **installer**.

[![](images/02.png)](images/02.png)

**3** - Clique em **Install**.

[![](images/03.png)](images/03.png)

**4** - A instalação do VCSA é dividida em dois estágios, o primeira é o deploy e o segundo as configurações, clique em **NEXT**.

[![](images/04.png)](images/04.png)

**5** - Aceite os termos da licença e clique em **NEXT**.

[![](images/05.png)](images/05.png)

**6** - Selecione o tipo de instalação, em nosso caso será a **Embedded Plataform Services Controller**, selecione e clique em **NEXT**.

[![](images/06.png)](images/06.png)

**7** - Insira as informações do host onde o deploy do VCSA será realizado e clique em **NEXT**.

[![](images/07.png)](images/07.png)

**8** - Aceite o certificado, clique em **YES**.

[![](images/08.png)](images/08.png)

**9** - Especifique as configurações da VM, o nome da maquina virtual e senha de acesso e clique em **NEXT**.

[![](images/09.png)](images/09.png)

**10** - Selecione o tamanho do deploy de acordo com seu ambiente, em nosso caso como é apenas para LAB vamos deixar como **Tiny**, clique em **NEXT**.

[![](images/10.png)](images/10.png)

**11** - Selecione o **datastore** de destino, selecione **Enable Thin Disk Mode** para habilitar o **Thin Provisioning** para o disco do VCSA, clique em **NEXT**.

[![](images/11.png)](images/11.png)

**12** - Insira as informações de rede do **VCSA**, caso deseje usar um **FQDN** tenha um servidor de **DNS** bem configurado em seu ambiente, clique em **NEXT**.

[![](images/12.png)](images/12.png)

**13** - Reveja as informações inseridas e clique em **FINISH**, para começar o deploy.

[![](images/13.png)](images/13.png)

Se deu tudo certo, vamos a segunda parte :D

**14** - Clique em **CONTINUE**.

[![](images/14.png)](images/14.png)

**15** - Clique em **NEXT**.

[![](images/15.png)](images/15.png)

**16** - Selecione se o **VCSA** vai sincronizar a hora com o host ESXi, ou se vai usar um servidor **NTP**, caso opte por um servidor NTP, será necessário digitar as informações do mesmo. Selecione se o acesso via **SSH** ao **VCSA** será habilitado ou não, clique em **NEXT**.

[![](images/16.png)](images/16.png)

**17** - Configure o **SSO domain** e a senha de acesso ao ambiente do **VCSA**.

[![](images/17.png)](images/17.png)

**18** - Configure o **CEIP**, e clique em **NEXT**.

[![](images/18.png)](images/18.png)

**OBS:** Para maiores informações sobre o CEIP acesse o link abaixo:

[https://www.vmware.com/solutions/trustvmware/ceip.html](https://www.vmware.com/solutions/trustvmware/ceip.html)

19 - Reveja as configurações e clique em **FINISH**.

[![](images/19.png)](images/19.png)

**20** - Cliquem em **OK**.

[![](images/20.png)](images/20.png)

**21** - Clique no link para abrir a página do VCSA e depois em **CLOSE**.

[![](images/21.png)](images/21.png)

**22** - Pronto, VCSA instalado com sucesso!

Agora só escolher qual interface deseja utilizar :D

[![](images/22.png)](images/22.png)

Espero que tenham gostado e até a próxima! :D

**Maiores detalhes sobre a instalação do VCSA no link abaixo:**

[https://docs.vmware.com/en/VMware-vSphere/6.7/vsphere-vcenter-server-67-installation-guide.pdf](https://docs.vmware.com/en/VMware-vSphere/6.7/vsphere-vcenter-server-67-installation-guide.pdf "https://docs.vmware.com/en/VMware-vSphere/6.7/vsphere-vcenter-server-67-installation-guide.pdf")
