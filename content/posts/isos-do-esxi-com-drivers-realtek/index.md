---
title: "ISOs do ESXi com drivers Realtek"
slug: "isos-do-esxi-com-drivers-realtek"
date: 2017-06-09
category: 
  - "virtualizacao"
tag: 
  - "esxi"
  - "homelab"
  - "isos"
  - "vmware"
  - "vmware-vsphere"
coverImage: "esxi.png"
---

Para imagens atualizadas visite a página abaixo:

https://rodrigolira.eti.br/isos-esxi-customizadas/

Salve Salve Pessoal!

Diversas pessoas chegam até mim pedindo a imagem personalizada do ESXi porque não estão conseguindo utilizar o script **ESXi-Customizer-PS**.

Para saber mais sobre o script acesse o link abaixo:

http://rodrigolira.eti.br/iso-personalizada-do-esxi-homelab/

Dessa forma resolvi criar as ISOs das versões 6 e 6.5 com os drivers de rede da Realtek não suportados por padrão, e drivers de controladora sata ahci.

Lista de drivers da ISO **ESXi-6.0\_u3.iso**:

Pacote net55-r8168: **Realtek 8168/8111/8411/8118**

Pacote net51-r8169: **Realtek R8169** Pacote net-r8101: **Realtek RTL8101E/RTL8102E** Pacote net-r8139too: **Realtek RTL-8100/8101L/8139** Pacote sata-xahci: **Controladoras SATA AHCI**

Lista de Drivers da ISO **ESXi-6.5.iso**

Pacote net55-r8168: **Realtek 8168/8111/8411/8118** Pacote net51-r8169: **Realtek R8169** Pacote net-r8101: **Realtek RTL8101E/RTL8102E** Pacote net-r8139too: **Realtek RTL-8100/8101L/8139**

**Obs**: Na versão 6.5 não é necessário o driver sata ahci :D

Segue abaixo o link das ISOs para download:

**ESXi 6.0** - [CLIQUE AQUI PARA O DOWNLOAD](https://www.dropbox.com/s/6xgxcmjw2pw2i9n/ESXi-6.0u3_Drivers_Realtk.iso?dl=0)

**ESXi 6.5** - [CLIQUE AQUI PARA O DOWNLOAD](https://www.dropbox.com/s/21z6mvy0pmfxv9y/ESXi-6.5_Drivers_Realtek.iso?dl=0)

Para maiores informações sobre os drivers e como usar o script acesse o link abaixo:

[https://www.v-front.de/](https://www.v-front.de/)
