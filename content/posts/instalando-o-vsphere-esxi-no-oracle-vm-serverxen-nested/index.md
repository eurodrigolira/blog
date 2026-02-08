---
title: "Instalando o vSphere ESXi no Oracle VM Server/Xen (Nested)"
slug: "instalando-o-vsphere-esxi-no-oracle-vm-serverxen-nested"
date: 2016-10-06
category: 
  - "labs"
  - "linux"
  - "virtualizacao"
tag: 
  - "labs"
  - "oracle-vm-manager"
  - "oracle-vm-server"
  - "vmware"
  - "vmware-vsphere"
---

Salve Salve Pessoal!

Depois de um bom tempo pesquisando, várias tentativas e erros, consegui fazer o VMware vSphere ESXi funcionar como guest dentro do Oracle VM Server. O procedimento é um pouco chato, porque nós vamos ter que editar o arquivo de configuração da VM manualmente, e um detalhe muito importante, se formos fazer qualquer alteração da VM com o Oracle VM Manager, as configurações manuais que colocamos são excluídas, por isso temos que ficar atentos a qualquer modificação realizada na VM.

Primeiro de tudo vamos criar nossa VM, nas imagens abaixo criei a VM com as configurações minimas recomendadas pela VMware para a instalação do vSphere.

Expliquei todos os passos a seguir em outro post, clique [AQUI](http://rodrigolira.eti.br/lab-oracle-vm-server-parte-5/) para acessar e ver o passo-a-passo.

[![captura-de-tela-2016-10-06-as-13-53-50](images/Captura-de-Tela-2016-10-06-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/10/Captura-de-Tela-2016-10-06-a?s-13.53.50.png)

[![captura-de-tela-2016-10-06-as-13-53-29](images/Captura-de-Tela-2016-10-06-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/10/Captura-de-Tela-2016-10-06-a?s-13.53.29.png)

[![captura-de-tela-2016-10-06-as-13-55-42](images/Captura-de-Tela-2016-10-06-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/10/Captura-de-Tela-2016-10-06-a?s-13.55.42.png)

[![captura-de-tela-2016-10-06-as-13-56-40](images/Captura-de-Tela-2016-10-06-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/10/Captura-de-Tela-2016-10-06-a?s-13.56.40.png)

[![captura-de-tela-2016-10-06-as-13-56-55](images/Captura-de-Tela-2016-10-06-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/10/Captura-de-Tela-2016-10-06-a?s-13.56.55.png)

Feito todo o processo nossa VM está criada, basta iniciar a mesma e abrir o console para vermos a inicialização do sistema, quando o sistema iniciar ele vai detectar que não temos nenhum driver de rede disponível. Isso acontece porque o driver de rede padrão do Oracle VM Server/Xen é o Realtek RTL8139 e o mesmo não é suportado pelo vSphere.

[![captura-de-tela-2016-10-06-as-14-02-17](images/Captura-de-Tela-2016-10-06-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/10/Captura-de-Tela-2016-10-06-a?s-14.02.17.png)

Para resolvermos esse problema, temos que editar o arquivo de configuração manualmente e colocar qual o driver que queremos usar. Acesse o Oracle VM Server(hospedeiro) via SSH e navegue até a pasta de configurações da VM.

```
# cd /OVS/Repositories/0004fb0000030000598e525857751f9a/VirtualMachines/0004fb0000060000cfe2da48f9e2120e/
```

Esse **0004fb0000030000598e525857751f9a** é o **ID** do seu repositório onde a VM se encontra, se você tiver mais de um, você pode identificar qual o correto da seguinte forma:

Acesse a aba **Repositories**, selecione o repositório e em **Pespective** selecione **Info**, dessa forma ele vai mostrar o ID do repositório:

[![captura-de-tela-2016-10-06-as-14-28-54](images/Captura-de-Tela-2016-10-06-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/10/Captura-de-Tela-2016-10-06-a?s-14.28.54.png)

Esse **0004fb0000060000cfe2da48f9e2120e** é o **ID** da VM, se você tiver mais de uma, você pode identificar qual a VM correta da seguinte forma:

Acesse a aba **Servers and VMs**, selecione o **HOST** e depois a **VM**, clique no ícone com a seta para baixo para expandir os detalhes da VM, dessa forma vai mostrar o ID:

[![captura-de-tela-2016-10-06-as-14-32-31](images/Captura-de-Tela-2016-10-06-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/10/Captura-de-Tela-2016-10-06-a?s-14.32.31.png)

Agora que já sabemos o diretório correto, abra o arquivo **vm.cfg**, no meu caso o meu arquivo ficou com as seguintes configurações:

```
vif = ['mac=00:21:f6:5b:b5:f7,bridge=10238073c2']
OVM_simple_name = 'ESXi-01'
vnclisten = '127.0.0.1'
serial = 'pty'
disk = ['file:/OVS/Repositories/0004fb00000300001e4ee7d261313647/VirtualDisks/0004fb00001200009d2574fd9b824a84.img,xvda,w', 'file:/OVS/Repositories/0004fb0000030000598e525857751f9a/ISOs/0004fb00001500009f6ce2a34d84d851.iso,xvdb:cdrom,r']
vncunused = 1
uuid = '0004fb00-0006-0000-cfe2-da48f9e2120e'
on_reboot = 'restart'
boot = 'dc'
cpu_weight = 27500
memory = 4096
cpu_cap = 0
maxvcpus = 2
OVM_high_availability = False
vnc = 1
OVM_description = ''
on_poweroff = 'destroy'
on_crash = 'restart'
guest_os_type = 'linux'
name = '0004fb0000060000cfe2da48f9e2120e'
builder = 'hvm'
vcpus = 2
keymap = 'pt-br'
OVM_os_type = 'Other Linux'
OVM_cpu_compat_group = ''
OVM_domain_type = 'xen_hvm'
```

Vamos modificar a linha que faz referência a placa de rede virtual, vamos colocar explicitamente qual o tipo de driver de rede que queremos usar, que no nosso caso vai ser a **Intel E1000**, então vai ficar da seguinte forma:

```
vif = ['type=ioemu,mac=00:21:f6:5b:b5:f7,bridge=10238073c2,model=e1000']
```

Pronto, driver de rede foi resolvido :D

Mas precisamos habilitar o modo Nested para está VM! Para maiores detalhes sobre Nested clique [AQUI](http://solutions4crowds.com.br/configurando-o-esxi-nested-no-vmware-vsphere-6/) e veja o post no blog do amigo [@ricardoconzatti](https://twitter.com/ricardoconzatti).

Para isso vamos adicionar as seguintes linhas ao nosso arquivo de configuração:

```
hap=1
nestedhvm=1
```

Pronto, agora o arquivo de configuração está pronto e podemos reiniciar a nossa VM, segue abaixo como ficou o meu arquivo de configuração:

```
hap=1
nestedhvm=1
vif = ['type=ioemu,mac=00:21:f6:5b:b5:f7,bridge=10238073c2,model=e1000']
OVM_simple_name = 'ESXi-01'
vnclisten = '127.0.0.1'
serial = 'pty'
disk = ['file:/OVS/Repositories/0004fb00000300001e4ee7d261313647/VirtualDisks/0004fb00001200009d2574fd9b824a84.img,xvda,w', 'file:/OVS/Repositories/0004fb0000030000598e525857751f9a/ISOs/0004fb00001500009f6ce2a34d84d851.iso,xvdb:cdrom,r']
vncunused = 1
uuid = '0004fb00-0006-0000-cfe2-da48f9e2120e'
on_reboot = 'restart'
boot = 'dc'
cpu_weight = 27500
memory = 4096
cpu_cap = 0
maxvcpus = 2
OVM_high_availability = False
vnc = 1
OVM_description = ''
on_poweroff = 'destroy'
on_crash = 'restart'
guest_os_type = 'linux'
name = '0004fb0000060000cfe2da48f9e2120e'
builder = 'hvm'
vcpus = 2
keymap = 'pt-br'
OVM_os_type = 'Other Linux'
OVM_cpu_compat_group = ''
OVM_domain_type = 'xen_hvm'
```

Os passos da instalação seguem normalmente, durante a instalação ele vai apresentar uma mensagem de erros, informando que a dispositivos não suportados:

[![captura-de-tela-2016-10-06-as-15-17-07](images/Captura-de-Tela-2016-10-06-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/10/Captura-de-Tela-2016-10-06-a?s-15.17.07.png)

Dando uma pesquisada podemos ver que é devido ao driver de rede da Intel.

[https://kb.vmware.com/selfservice/microsites/search.do?language=en\_US&cmd=displayKC&externalId=2056935](https://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=2056935)

[![captura-de-tela-2016-10-06-as-15-21-07](images/Captura-de-Tela-2016-10-06-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/10/Captura-de-Tela-2016-10-06-a?s-15.21.07.png)

Mas podemos seguir com a instação normalmente que funciona perfeitamente.

Após a instalação for concluída, desligue a VM e mude a ordem de boot, lembre-se do que eu disse no inicio do post, se alterar qualquer coisa usando o Oracle VM Manager ele vai sobrescrever a configuração, dessa forma depois que alterar as configurações com o Manager, volte para a linha de comando e refaça as alterações manuais.

Pronto terminamos a configuração do guest, ligue a VM e o ESXi vai estar funcionando perfeitamente :D

[![captura-de-tela-2016-10-06-as-16-01-01](images/Captura-de-Tela-2016-10-06-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/10/Captura-de-Tela-2016-10-06-a?s-16.01.01.png)

Agora acesso o ESXi e crie uma VM, quando você for tentar ligar ela aparecerá o seguinte erro para você:

[![captura-de-tela-2016-10-06-as-16-09-44](images/Captura-de-Tela-2016-10-06-a)](http://rodrigolira.eti.br/wp-content/uploads/2016/10/Captura-de-Tela-2016-10-06-a?s-16.09.44.png)

Está mensagem de erro é porque o ESXi detecta que está rodando em outro Hypervisor, para resolver o problema temos que adicionar a seguinte linha no arquivo **/etc/vmware/config**:

```
vmx.allowNested = TRUE
```

Pronto, agora podemos iniciar a VM dentro do ESXi normalmente!

Espero que tenham gostado e até a próxima :D

Referências:

[https://wiki.xenproject.org/wiki/Nested\_Virtualization\_in\_Xen](https://wiki.xenproject.org/wiki/Nested_Virtualization_in_Xen)

[http://xenbits.xen.org/docs/unstable/misc/xl-network-configuration.html](http://xenbits.xen.org/docs/unstable/misc/xl-network-configuration.html)

[https://docs.oracle.com/cd/E15458\_01/doc.22/e15444/templates.htm](https://docs.oracle.com/cd/E15458_01/doc.22/e15444/templates.htm)

[https://communities.vmware.com/docs/DOC-8970](https://communities.vmware.com/docs/DOC-8970)
