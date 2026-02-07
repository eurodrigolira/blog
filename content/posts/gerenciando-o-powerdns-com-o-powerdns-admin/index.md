---
title: "Gerenciando o PowerDNS com o PowerDNS-Admin"
slug: "gerenciando-o-powerdns-com-o-powerdns-admin"
date: 2020-04-21
categories: 
  - "linux"
  - "redes"
tags: 
  - "dns"
  - "linux"
  - "powerdns"
  - "powerdns-admin"
---

[![](images/030.png)](images/030.png)

Salve Salve Pessoal!

No post anterior falei mostrei como podemos instalar e configurar o **PowerDNS 4.3 Authoritative no CentOS 8 / Oracle Linux 8 / RHEL 8**, veja o post no link abaixo:

https://rodrigolira.eti.br/instalando-o-powerdns-4-3-authoritative-no-centos-8-oracle-linux-8-rhel-8/

Porém o gerenciamento dele é um pouco complexo se tivermos que fazer tudo via o console do banco de dados.

Para resolver esse problema vamos utilizar uma interface web, assim podemos gerenciar o PowerDNS de uma maneira bem mais fácil.

Existe diversas interfaces de gerenciamento, elas podem fazer o gerenciamento acessando diretamente o banco de dados ou através da API do PowerDNS.

Já utilizei duas dessas interfaces:

**PowerDNS-Admin:** desenvolvida em Python e JS, o acesso é través da API.

[https://github.com/ngoduykhanh/PowerDNS-Admin](https://github.com/ngoduykhanh/PowerDNS-Admin)

**Poweradmin:** desenvolvida em PHP, o acesso é através do banco de dados.

[https://github.com/poweradmin/poweradmin](https://github.com/poweradmin/poweradmin)

Para ver todas as interfaces acessem o link abaixo:

[https://github.com/PowerDNS/pdns/wiki/WebFrontends](https://github.com/PowerDNS/pdns/wiki/WebFrontends)

Hoje em dia sempre uso **PowerDNS-Admin** pois ela tem bem mais features de gerenciamento do que as outras interfaces e podemos fazer o deploy dela diretamente em um container, que será o nosso caso de hoje.

Então vamos ao que interessa! :D

Vamos fazer a instalação do **Docker** no mesmo servidor que está executando o PowerDNS.

1 - Instale o pacote **yum-utils.**

```
# yum install -y yum-utils
```

2 - Adicione o repositório do docker.

```
# yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

3 - Vamos instalar o **docker**, também estou instalando o **git** pois vamos precisar dele para fazer um clone do projeto PowerDNS-Admin e do **jq** para os testes da API.

```
# yum install docker-ce docker-ce-cli containerd.io git jq --nobest
```

4 - Agora vamos iniciar e habilitar a inicialização do docker junto com o sistema operacinal.

```
# systemctl enable docker
```

```
# systemctl start docker
```

Pronto, agora já temos nosso docker rodando.

[![](images/001.png)](images/001.png)

Agora precisamos instalar o docker compose.

5 - Faça o download do docker compose.

```
# curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

6 - Varmos dar permissão de execução.

```
# chmod +x /usr/local/bin/docker-compose
```

7 - Vamos criar o link simbólico.

```
# ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

Agora nos vamos as configurações do PowerDNS-Admin.

8 - Vamos fazer um clone do projeto.

```
# git clone https://github.com/ngoduykhanh/PowerDNS-Admin.git
```

9 - Após fazer o clone do projeto entre na pasta PowerDNS-Admin.

```
# cd PowerDNS-Admin
```

Dentro da pasta teremos vários arquivos, nós só precisamo de um arquivo, o arquivo **docker-compose.yml**. Porém eu particularmente deixo tudo para estudar o projeto.

[![](images/002.png)](images/002.png)

10 - Vamos editar esse arquivo, use seu editor favorito, como já falei em diversos posts eu sempre uso o vim.

```
# vim docker-compose.yml
```

[![](images/003.png)](images/003.png)

Nós só precisamos editar um campo, que é o **SQLALCHEMY\_DATABASE\_URI** com as informações de conexão da **API**, as informações são as seguintes:

**SQLALCHEMY\_DATABASE\_URI = 'mysql://' + USUARIO\_DO\_BANCO + ':' + SENHA\_DO\_USUARIO\_DO\_BANCO + '@' + HOST\_DO\_BANCO + '/' + NOME\_DO\_BANCO**

Usando as informações do nosso post anterior, nosso caso fica assim:

**\- SQLALCHEMY\_DATABASE\_URI=mysql://pdnsuser:Mudar123@10.20.30.220/powerdns**

O campo **\- "9191:80"** fica a seu critério, se você não entende de docker esse campo vai redirecionar as requisições na porta **9191** para a porta **80** no container do PowerDNS-Admin, como normalmente não executamos nenhum outro serviço web no servidor, podemos modificar para a porta 80 mesmo, ficando assim:

**\- "80:80"**

Nosso arquivo editado ficará assim:

[![](images/004.png)](images/004.png)

11 - Agora vamos acessar nosso banco de dados e configurar uma nova conexão com o mesmo.

```
# grant all privileges on powerdns.* to pdnsuser@'%' identified by 'Mudar123';
```

No comando acima substitui o **@localhost** por **@'%'** permitindo a conexão de qualquer host.

12 - Agora você precisa liberar a rede do docker no firewall com destino a porta ao mysql (3306), execute o comando abaixo:

```
# firewall-cmd --add-rich-rule='rule family=ipv4 source address=172.18.0.0/16 service name=mysql accept' --permanent
```

```
# firewall-cmd --reload
```

**OBS:** Ajuste as configurações de acesso de acordo com a sua rede e garantindo a melhor segurança possível, apesar de termos liberado o acesso ao banco de dados do PowerDNS de qualquer host o firewall está permitindo conexões que venham apenas da rede do docker, podemos limitar isso ao endereço IP do container também.

11 - Agora vamos iniciar o container.

```
# docker-compose up -d
```

[![](images/005.png)](images/005.png)

12 - Agora basta acessar via navegador o endereço IP do servidor, nesse primeiro acesso clique em **Create an account** para criar uma conta.

[![](images/006.png)](images/006.png)

13 - Preencha os dados solicitados e clique em **Register**.

[![](images/007.png)](images/007.png)

14 - Após concluir o registro faça login, depois que você logar será direcionado para a página de configuração da API.

[![](images/008.png)](images/008.png)

15 - Agora vamos configurar o PowerDNS para executar o webserver da API, acesse o arquivo de configuração **/etc/pdns/pdns.conf** e insira os seguintes dados.

```
api=yes
api-key=ODop9YtUf7ah
webserver=yes
webserver-address=10.20.30.220
webserver-allow-from=10.20.30.0/24,172.18.0.0/16

```

**OBS:** a chave da api "**ODop9YtUf7ah**" deve ser gerada por você mesmo, normalmente uso o comando **pwmake** para gerar minhas chaves, altere o endereço IP pelo endereço IP do seu servidor e permita a conexão da sua rede e da rede do docker.

```
# pwmake 12
```

[![](images/009.png)](images/009.png)

Nosso arquivo deve ficar assim:

[![](images/010-3.png)](images/010-3.png)

16 - Reinicie o PowerDNS

```
# systemctl restart pdns
```

17 - Por padrão a API do PowerDNS usa a porta **8081**, precisamos liberar nossa rede e a rede do docker no firewall para ter acesso a essa porta também.

```
# firewall-cmd --add-rich-rule='rule family=ipv4 source address=172.18.0.0/16 port port=8081 protocol=tcp accept' --permanent
```

```
# firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.20.30.0/24 port port=8081 protocol=tcp accept' --permanent
```

```
# firewall-cmd --reload
```

18 - Agora vamos fazer uma consulta simples via console para ver se  a API do PowerDNS está respondendo, troque a chave da API pela sua e o endereço IP também.

```
# curl -H 'X-API-Key: ODop9YtUf7ah' http://10.20.30.220:8081/api/v1/servers/localhost/zones | jq .
```

[![](images/012.png)](images/012.png)

Como podemos ver na imagem ele retornou os dados com o domínio **rodrigolira.lab** criado no post anterior, a API está funcionando corretamente.

19 - Volte ao PowerDNS-Admin e insira a **URL** a **chave da API** e depois clique em **Update**.

[![](images/020.png)](images/020.png)

Pronto, se tudo foi configurado corretamente quando você clicar em Dashboard o domínio que foi criado deve aparecer.

[![](images/021.png)](images/021.png)

Agora é so explorar e ver suas funcionalidades e facilidades.

No próximo post sobre PowerDNS irei mostrar como configurar para ele trabalhar como **master** e outro serviodr como **slave**.

Até a próxima!

:D
