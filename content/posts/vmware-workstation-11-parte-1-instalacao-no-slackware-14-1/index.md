---
title: "VMware Workstation 11 - Parte 1 (Instalação no Slackware 14.1)"
slug: "vmware-workstation-11-parte-1-instalacao-no-slackware-14-1"
date: 2015-06-02
category: 
  - "linux"
  - "virtualizacao"
tag: 
  - "linux"
  - "slackware"
  - "vmware"
  - "vmware-workstation"
---

[![vmw-bnr-workstation11-product](images/vmw-bnr-workstation11-product1.jpg)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/vmw-bnr-workstation11-product1.jpg)Salve Salve Pessoal!

Resolvi fazer uma serie de posts para mostrar as funcionalidades do VMware Workstation, o mesmo é muito pouco explorado, principalmente quando se trata de realizar alguns laboratórios com a ferramenta, sem contar diversos outros recursos que não são utilizados.

Neste primeiro post vou mostrar como instalar ele no Linux, no meu caso no Slackware, a instalação segue o mesmo padrão em outras distribuições, como também no windows.

Então vamos lá:

Primeiro baixe o VMware Workstation do site da vmware:

[https://my.vmware.com/web/vmware/info/slug/desktop\_end\_user\_computing/vmware\_workstation/11\_0](https://my.vmware.com/web/vmware/info/slug/desktop_end_user_computing/vmware_workstation/11_0)

Dê permissão de execução ao arquivo:

```
#chmod +x VMware-Workstation-Full-11.1.0-2496824.x86_64.bundle
```

<!--more-->E execute o mesmo:

```
#./VMware-Workstation-Full-11.1.0-2496824.x86_64.bundle -I
```

**Obs:** Foi utilizado o parâmetro "-I" no final do comando para ignorar erros, para verificar todas as opções possíveis basta coloca o parâmetro "--help".

Apôs executar o comando a janela de instalaçao do VMware Workstation se abre:

1 - Aceite a licença de uso da ferramenta:

[![imagem2](images/imagem2-300x232.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/imagem2.png)

 

 

 

 

 

 

2 - Aceite a licença de uso de componente OVF Tool para Linux.

[![imagem3](images/imagem3-300x232.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/imagem3.png)

 

 

 

 

 

 

3 - Marque "yes" para verificação de atualização quando iniciar a ferramenta:

[![imagem4](images/imagem4-300x233.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/imagem4.png)

 

 

 

 

 

 

4 - Se deseja ajudar com o desenvolvimento da ferramenta, marque "yes" para enviar estatísticas sobre a ferramenta:

[![imagem5](images/imagem5-300x229.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/imagem5.png)

 

 

 

 

 

 

5 - Deixe como padrão "root":

[![imagem6](images/imagem6-300x232.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/imagem6.png)

 

 

 

 

 

 

6 - Deixe o compartilhamento de VMs como padrão da instalação:

[![imagem7](images/imagem7-300x232.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/imagem7.png)

 

 

 

 

 

 

7 - Deixe a porta padrão de acesso "443":

[![imagem8](images/imagem8-300x232.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/imagem8.png)

 

 

 

 

 

 

8 - Adicione a cheve de licença de uso, caso não tenha pressione "next", você poderá usar a ferramenta durante 30 dias:

[![imagem9](images/imagem9-300x232.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/imagem9.png)

 

 

 

 

 

 

9 - Clique em "install" para instalar a ferramenta:

[![imagem10](images/imagem10-300x233.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/imagem10.png)

 

 

 

 

 

 

10 - Pronto, VMware Workstation instalado:

[![imagem11](images/imagem11-300x232.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/imagem11.png)

 

 

 

 

 

 

No Slackware você precisar iniciar o serviço do VMware Workstation manualmente, execute o seguinte comando:

#/etc/rc.d/init.d/vmware start

[![imagem12](images/imagem12-300x91.png)](http://rodrigolira.eti.br/wp-content/uploads/2015/06/imagem12.png)

 

 

 

Para automatizar esse processo na inicialização do sistema, adicione no as seguintes linhas no /etc/rc.d/rc.local:

```
if [ -x etc/rc.d/init.d/vmware ] 
then 
/etc/rc.d/init.d/vmware start 
fi
```

Pronto, VMware Workstation 11 instalado!

Até a próxima :D
