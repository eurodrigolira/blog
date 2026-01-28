---
title: "Oracle Linux Virtualization Manager – Parte 02"
date: 2019-08-06
categories: 
  - "linux"
  - "virtualizacao"
tags: 
  - "linux"
  - "oracle"
  - "oracle-linux"
  - "oracle-linux-virtualization-manager"
  - "virtualizacao"
---

[![](images/olvm-300x172.png)](images/olvm.png)

Salve Salve Pessoal!

Vamos ao nosso segundo post da nossa serie de posts sobre o **Oracle Linux Virtualization Manager**.

Se você não viu o primeiro post ainda acesse o link abaixo e leia o mesmo para entender um pouco mais sobre o **Oracle Linux Virtualization Manager** e nosso cenário:

https://rodrigolira.eti.br/oracle-linux-virtualization-manager-parte-01/

Nessa segunda parte vamos ver os requisitos para instalação do **Manager** e vamos instalar o **Oracle Linux** e deixar ele no ponto de instalação do **Manager**.

**Requisitos mínimos:**

Oracle Linux 7 update 6 com Unbreakable Enterprise Kernel Release 5 update 1 ou posterior.

Processador 64-bit com dois núcleos.

4 GB de memoria RAM.

1 placa de rede gigabit.

25 GB de disco local.

**Requisitos recomendados:**

Oracle Linux 7 update 6 com Unbreakable Enterprise Kernel Release 5 update 1 ou posterior.

Processador 64-bit com quatro núcleos ou mais.

16 GB de memoria RAM ou mais.

2 placas de rede Gigabit ou mais.

50 GB de disco local ou mais.

Devemos sempre observar o tamanho do nosso ambiente, você pode acabar precisando de mais recursos de hardware dependendo do tamanho dele.

O download do Oracle Linux 7.6 pode ser feito na Oracle Software Delivery Cloud, acesse o link abaixo para fazer o download, ele é gratuito.

[http://edelivery.oracle.com/](http://edelivery.oracle.com/)

Agora que já sabemos os requisitos vamos a instalação do Oracle Linux 7.6.

**01** - Dê boot e selecione **Install Oracle Linux 7.6** e aperte **ENTER**.

[![](images/01.png)](images/01.png)

**02** - Selecione o idioma de instalação, por padrão sempre deixo em **English** e depois clique em **Continue**.

[![](images/02.png)](images/02.png)

**03** - Configure a hora e região.

[![](images/03.png)](images/03.png)

**04** - Selecione sua região, no meu caso como não tem João Pessoa/PB uso Recife, se desejar pode configurar os servidores NTP e clique em **Done**.

[![](images/04.png)](images/04.png)

**05** - Configure seu teclado.

[![](images/05.png)](images/05.png)

**06** - Selecione o teclado desejado e clique em **Done**.

[![](images/06.png)](images/06.png)

**07** - Sempre deixo a linguagem de suporte em **English** mesmo, mas se desejar pode mudar.

[![](images/07.png)](images/07.png)

**08** - Pode deixar a fonte de instalação padrão.

[![](images/08.png)](images/08.png)

**09** - É recomendado fazer a **Minimal Install**.

[![](images/09.png)](images/09.png)

**10** - Vamos selecionar o destino da instalação.

[![](images/10.png)](images/10.png)

**11** - Clique em configurar o particionamento você mesmo e depois em **Done**.

[![](images/11.png)](images/11.png)

**12** - Clique em **Click here to create them automatically** para criar o particionamento automaticamente.

[![](images/12.png)](images/12.png)**OBS:** O requerimento minimo de tamanho das partições para o Manager é o seguinte:

**/ (root) - 6 GB** **/home - 1 GB** **/tmp - 1 GB** **/boot - 1 GB** **/var - 15 GB** **/var/log - 8 GB** **/var/log/audit - 2 GB** **swap - 1 GB**

Como podem perceber os **50 GB** são suficiente, se desejarem podem colocar em partições separadas, mas como estamos fazendo em laboratório deixei tudo no **/**.

**13** - Por padrão o Oracle Linux irá criar três partições para esse tamanho de disco, clique em **Done**.

[![](images/13.png)](images/13.png)

**14** - Aceite as mudanças.

[![](images/14.png)](images/14.png)

**15** - Clique em **KDUMP** para desabilitarmos o kdump.

[![](images/15.png)](images/15.png)

**16** - Desmarque a caixa e clique em **Done**.

[![](images/16.png)](images/16.png)

**17** - Não vamos configurar a rede nem o nome agora.

[![](images/17.png)](images/17.png)

**18** - Em **SECURITY POLICY** pode deixar no padrão também.

[![](images/18.png)](images/18.png)

**19** - Clique em **Begin Installation**.

[![](images/19.png)](images/19.png)

**20** - Clique em **ROOT PASSWORD** para configurar a senha do usuário root.

[![](images/20.png)](images/20.png)

**21** - Defina a senha do usuário root e clique em **Done**.

[![](images/21.png)](images/21.png)**OBS:** Não precisamos configurar nenhum outro usuário.

**22** - Ao terminar a instalação reinicie o sistema clicando em **Reboot**.

[![](images/22.png)](images/22.png)

**23** - Depois que o sistema reiniciar, vamos configurar a rede, verifique o **nome das suas interfaces**.

[![](images/23.png)](images/23.png)

**24** - Agora que já sabemos os nomes das interfaces, que no meu caso aqui é **ens32** e **ens33** vamos configurar a interface do tipo team com loadbalance, execute o seguintes comandos:

**OBS**: Altere as interfaces e o endereçamento IP de acordo com o seu ambiente.

```
# nmcli con add type team con-name team0 ifname team0 config '{"runner": {"name": "loadbalance"}}' 
# nmcli con add type team-slave con-name team0-slave1 ifname ens32 master team0 
# nmcli con add type team-slave con-name team0-slave2 ifname ens33 master team0 
# nmcli con mod team0 ipv4.address 10.20.30.20/24 ipv4.gateway 10.20.30.1 ipv4.dns 10.20.30.1 ipv4.method manual connection.autoconnect yes

```

**25** - Agora configure o hostname com o comando abaixo:

```
# hostnamectl set-hostname ovl-manager.rodrigolira.lab
```

**OBS**: Altere o **hostname** de acordo com seu ambiente.

**26** - Agora que estamos com rede vamos atualizar o sistema e depois reiniciar.

```
# yum update -y

# systemctl reboot
```

Pronto, o sistema já está instalado e pronto para instalação do **Oracle Linux Virtualization Manager**.

Para esse post não se estender muito vamos deixar para o próximo post todo o processo de instalação.

Até o próximo post!

:D
