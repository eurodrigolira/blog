---
title: "Permissões no vCenter Server 6.5 – Parte 02"
slug: "permissoes-no-vcenter-server-6-5-parte-02"
date: 2016-11-26
category: 
  - "labs"
  - "virtualizacao"
tag: 
  - "labs"
  - "vcenter-server"
  - "vcenter-server-6-5"
  - "vmware"
  - "vmware-vsphere"
  - "vmware-vsphere-6-5"
---

Salve Salve Pessoal!

Nessa segunda parte da serie Permissões no vCenter Server 6.5, nós vamos ver o segundo cenário.

Nós vamos criar uma permissão personalizada chamada Power-On, criar usuário chamado estagiário02, depois criar um grupo chamado estagiarios, e adicionar o usuário estagiario02 ao grupo estagiarios e delegar a permissão Power-On ao grupo estagiarios.

Obs: Se você não leu o primeiro post sobre Permissões no vCenter Server 6.5, acesse o link abaixo e leia ;)

http://rodrigolira.eti.br/permissoes-no-vcenter-server-6-5-parte-01/

Vamos lá :D

Acesse **Administration > Access Control > Roles**:

[![screen-shot-2016-11-26-at-16-54-06-2](images/Screen-Shot-2016-11-26-at-16.54.06-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-16.54.06-2.png)

Clique no ícone para adicionar uma permissão:

[![screen-shot-2016-11-26-at-16-54-45-2](images/Screen-Shot-2016-11-26-at-16.54.45-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-16.54.45-2.png)

Digite o nome da permissão:

[![screen-shot-2016-11-26-at-16-56-48-2](images/Screen-Shot-2016-11-26-at-16.56.48-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-16.56.48-2.png)

Em Privilege nós vamos dizer o que essa permissão pode fazer, como o próprio nome da mesma já diz, essa permissão poderá apenas ligar as VMs.

Acesse **All Privileges > Virtual Machine > Interaction** e selecione **Power on**, depois clique em **OK**:

[![screen-shot-2016-11-26-at-17-01-06-2](images/Screen-Shot-2016-11-26-at-17.01.06-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.01.06-2.png)

A permissão é adicionada:

[![screen-shot-2016-11-26-at-17-03-18-2](images/Screen-Shot-2016-11-26-at-17.03.18-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.03.18-2.png)

Agora vamos criar o usuário chamado estagiario02.

Acesse **Administration > Single Sign-On > Users and Groups**:

[![screen-shot-2016-11-26-at-17-08-31-2](images/Screen-Shot-2016-11-26-at-17.08.31-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.08.31-2.png)

Clique no ícone para adicionar um novo usuário:

[![screen-shot-2016-11-26-at-17-09-17-2](images/Screen-Shot-2016-11-26-at-17.09.17-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.09.17-2.png)

Preencha os dados e clique em **OK**:

[![screen-shot-2016-11-26-at-17-10-25-2](images/Screen-Shot-2016-11-26-at-17.10.25-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.10.25-2.png)

Usuário **estagiario02** é adicionado com sucesso:

[![screen-shot-2016-11-26-at-17-11-30-2](images/Screen-Shot-2016-11-26-at-17.11.30-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.11.30-2.png)

Agora vamos criar um grupo, acesse a aba **Groups** e clique no ícone para adicionar um novo grupo:

[![screen-shot-2016-11-26-at-17-12-56-2](images/Screen-Shot-2016-11-26-at-17.12.56-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.12.56-2.png)

Digite o nome do grupo e clique em **OK**:

[![screen-shot-2016-11-26-at-17-14-00-2](images/Screen-Shot-2016-11-26-at-17.14.00-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.14.00-2.png)

O grupo estagiarios é criado com sucesso:

[![screen-shot-2016-11-26-at-17-15-13-2](images/Screen-Shot-2016-11-26-at-17.15.13-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.15.13-2.png)

Agora, vamos adicionar o usuário estagiario02 ao grupo estagiarios:

Selecione o grupo **estagiarios** e clique em no ícone adicionar membro:

[![screen-shot-2016-11-26-at-17-18-37-2](images/Screen-Shot-2016-11-26-at-17.18.37-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.18.37-2.png)

Na aba que se abre, selecione o **usuário**, clique em **Add** e depois em **OK**:

[![screen-shot-2016-11-26-at-17-19-56-2](images/Screen-Shot-2016-11-26-at-17.19.56-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.19.56-2.png)

Pronto, o usuário **estagiario02** é adicionado ao grupo **estagiarios**:

[![screen-shot-2016-11-26-at-17-22-12-2](images/Screen-Shot-2016-11-26-at-17.22.12-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.22.12-2.png)

Agora vamos configurar a permissão para o grupo.

Acesse **Administration > Access Control > Global Permissions** e clique no ícone de adicionar:

[![screen-shot-2016-11-26-at-17-24-26-2](images/Screen-Shot-2016-11-26-at-17.24.26-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.24.26-2.png)

Clique em **Add** para adicionar o grupo:

[![screen-shot-2016-11-26-at-17-25-19-2](images/Screen-Shot-2016-11-26-at-17.25.19-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.25.19-2.png)

Selecione o grupo **estagiarios**, clique em **Add** e depois em **OK**:

[![screen-shot-2016-11-26-at-17-26-30-2](images/Screen-Shot-2016-11-26-at-17.26.30-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.26.30-2.png)

Em **Assigned Role** selecione **Power-On** e depois clique em **OK**:

[![screen-shot-2016-11-26-at-17-27-51-2](images/Screen-Shot-2016-11-26-at-17.27.51-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.27.51-2.png)

Pronto, agora o grupo estagiarios tem a permissão Power-On:

[![screen-shot-2016-11-26-at-17-29-20-2](images/Screen-Shot-2016-11-26-at-17.29.20-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.29.20-2.png)

Agora vamos logar com o usuário estagiario02 e verificar as permissões:

[![screen-shot-2016-11-26-at-17-31-44-2](images/Screen-Shot-2016-11-26-at-17.31.44-2-1024x576.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/Screen-Shot-2016-11-26-at-17.31.44-2.png)

Como podemos perceber, eu posso ligar a VM mas não tenho direito de fazer nenhuma outra interação:

[![vsphere-web-client-2016-11-26-17-33-49](images/vSphere-Web-Client-2016-11-26-17-33-49-1024x568.png)](http://rodrigolira.eti.br/wp-content/uploads/2016/11/vSphere-Web-Client-2016-11-26-17-33-49.png)

Espero que tenham gostado e até o próximo post :D
