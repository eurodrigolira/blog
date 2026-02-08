---
title: "ISOs Customizadas do ESXi 7"
slug: "isos-customizadas-do-esxi-7"
date: 2020-08-26
category: 
  - "virtualizacao"
tag: 
  - "esxi"
  - "esxi-7-0"
  - "isos"
  - "linux"
  - "vmklinux"
---

[![](images/vsphere7_logo.png)](images/vsphere7_logo.png)

Salve Salve Pessoal!

Muitas pessoas estão vindo me perguntar quando irei disponibilizar uma ISO do **ESXi 7 Customizada** com os drivers de rede com chipsets da realtek.

Então resolvi fazer esse post para esclarecer um pouco porque ainda não criei as ISOs e porque não será possível criar.

**Isso mesmo que você leu, não será possível criar uma ISO do ESXi 7 Customizada com os drivers de rede com chipsets da realtek, infelizmente.**

O que acontece é o seguinte:

As versões mais antigas do **ESXi** utilizam modulos de drivers derivados do **Linux** para terem uma maior compatibilidade com diversos tipos de drivers, porém para fazer isso é necessário uma camada adicional de emulação de drivers, o que eles chamam de **VMKlinux**.

Desde a versão do **ESXI 5.5** eles introduziram uma camada de de drivers nativos e anunciaram que planejavam sair do VMKlinux.

A versão do **ESXi 6.7** foi a última vindo com o **VMKlinux**, dessa forma não será possível adicionar os os drivers de rede com chipsets da realtek na versão do **ESXi 7.0**, pelo menos até o momento desse post a comunidade ainda não desenvolveu nenhuma solução e imagino que não haverá.

A solução para muitos será utilizar o **passthrough** ou até mesmo **dispositivos de rede USB**.

Espero que o post tenha esclarecido as dúvidas e o porque eu não criei as imagens.

Para maiores informações leiam as referências.

Até o próximo post!

:D

Referências:

[https://blogs.vmware.com/vsphere/2017/08/vmware-plans-deprecate-vmklinux-apis-associated-driver-ecosystem.html](https://blogs.vmware.com/vsphere/2017/08/vmware-plans-deprecate-vmklinux-apis-associated-driver-ecosystem.html)

[https://blogs.vmware.com/vsphere/2019/04/what-is-the-impact-of-the-vmklinux-driver-stack-deprecation.html](https://blogs.vmware.com/vsphere/2019/04/what-is-the-impact-of-the-vmklinux-driver-stack-deprecation.html)
