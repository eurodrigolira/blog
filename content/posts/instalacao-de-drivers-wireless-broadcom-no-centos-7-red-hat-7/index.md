---
title: "Instalação de drivers wireless Broadcom no CentOS 7/Red Hat 7"
slug: "instalacao-de-drivers-wireless-broadcom-no-centos-7-red-hat-7"
date: 2018-07-05
category: 
  - "linux"
tag: 
  - "broadcom"
  - "centos"
  - "centos-7"
  - "linux"
  - "red-hat"
  - "red-hat-7"
  - "wireless"
---

Salve Salve Pessoal!

Por padrão o **CentOS** e **Red Hat** não vem com drivers wireless da **Broadcom** disponíveis em sua arvore de repositórios, também não é possível encontrar em repositórios de terceiros devido a questões de licenciamento.

Porém o pessoal do **ELrepo** disponibiliza os **SRPMS** para que nós usuários finais possamos construir os pacotes com os drivers.

O procedimento é para as seguintes placas:

**BCM4311, BCM4312, BCM4313, BCM4321, BCM4322, BCM4331, BCM4352, BCM4360, BCM43142, BCM43224, BCM43225, BCM43227, BCM43228**

Vamos ao que interessa :D

Execute os seguintes comandos como root:

**1** - Faça a instalação das dependências:

```
# yum group install 'Development Tools'

# yum install redhat-lsb kernel-abi-whitelists

# yum install kernel-devel-$(uname -r)
```

Agora execute os seguintes comandos com usuário comum.

**2** - Crie os diretórios necessários:

```
$ mkdir -p ~/rpmbuild/{BUILD,RPMS,SPECS,SOURCES,SRPMS}

$ echo -e "%_topdir $(echo $HOME)/rpmbuild\n%dist .el$(lsb_release -s -r|cut -d"." -f1).local" >> ~/.rpmmacros
```

**3** - Faça o download do SRPMS:

```
$ wget -P ~/rpmbuild/SRPMS/ http://elrepo.org/linux/elrepo/el7/SRPMS/wl-kmod-6_30_223_271-5.el7.elrepo.nosrc.rpm 4 - Faça o download do sources da broadcom

$ wget -P ~/rpmbuild/SOURCES/ https://docs.broadcom.com/docs-and-downloads/docs/linux_sta/hybrid-v35_64-nodebug-pcoem-6_30_223_271.tar.gz
```

**OBS:** Se o link estiver offline por algum motivo, acesse o link abaixo e faça o download manualmente, coloque o arquivo dentro do /rpmbuild/SOURCES/.

[https://www.broadcom.com/support/download-search/?pf=Wireless+LAN+Infrastructure](https://www.broadcom.com/support/download-search/?pf=Wireless+LAN+Infrastructure)

**4** - Agora vamos construir nosso pacote:

```
$ rpmbuild --rebuild --define kmod-wl-6_30_223_271-5.el7.rpm ~/rpmbuild/SRPMS/wl-kmod-6_30_223_271-5.el7.elrepo.nosrc.rpm
```

Execute os comandos como root novamente.

**5** - Remova o ndiswrapper  para não dar conflitos:

```
# yum remove \*ndiswrapper\*
```

**6** - Instale o pacote que criamos:

```
# yum install -y /home/USUARIO/rpmbuild/RPMS/x86_64/kmod-wl-6_30_223_271-5.el7.local.x86_64.rpm (troque o nome USUARIO pelo seu usuário)
```

**7** - Reinicie o computador

```
# systemctl reboot
```

Pronto, sua placa de rede sem fio já deve estar funcionando :D

**OBS:** Caso a mesma não esteja funcionando verifique se você está com o secure boot habilitado na BIOS, caso esteja basta desabilitar que funcionará, se não deseja desabilitar é preciso criar uma assinatura para o pacote, verifique o procedimentos nas referências.

Até a próxima :D

Referência:

[https://elrepo.org/tiki/wl-kmod](https://elrepo.org/tiki/wl-kmod)
