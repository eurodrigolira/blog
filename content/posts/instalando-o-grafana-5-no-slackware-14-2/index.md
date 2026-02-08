---
title: "Instalando o Grafana 5 no Slackware 14.2"
slug: "instalando-o-grafana-5-no-slackware-14-2"
date: 2018-05-28
category: 
  - "linux"
  - "monitoramento"
  - "scripts"
tag: 
  - "grafana"
  - "linux"
  - "slackware"
  - "slackware-14-2"
---

[![](images/grafana-1024x503.png)](images/grafana.png)

Salve Salve Pessoal!

Hoje vou mostrar como fazer a instalação do **Grafana no Slackware 14.2**.

Para quem não conhece o Grafana, é uma ferramenta para exibir e criar gráficos muito flexível, uma das grandes diferenças sobre essa ferramenta é que ela open source, ela trabalha integrada com diversas ferramentas, inclusive com o Zabbix.

Para maiores detalhes sobre ela, acessem o link abaixo:

[https://grafana.com/](https://grafana.com/)

Vamos ao que interessa :D

**1** - Baixe o Grafana:

```
# wget https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana-5.1.3.linux-x64.tar.gz
```

**OBS:** Se por algum motivo o link estiver off, acessem a URL abaixo e faça o download do pacote Standalone:

[https://grafana.com/grafana/download](https://grafana.com/grafana/download)

**2** - Crie a pasta **/etc/grafana** e descompactar o arquivo baixado dentro dela:

```
# mkdir -p /etc/grafana && tar -xvf grafana-5.1.3.linux-x64.tar.gz -C /etc/grafana --strip-components=1
```

**3** - Vamos criar links simbólicos dos comandos **grafana-server** e **grafana-cli** para dentro do **/usr/sbin**, assim poderemos executar eles de qualquer diretório que estivermos:

```
# ln -s /etc/grafana/bin/grafana-server /usr/sbin

# ln -s /etc/grafana/bin/grafana-cli /usr/sbin/
```

Nesse ponto, basta executarmos o comando **grafana-server** passando como parâmetro o **homepath** do diretório do **grafana**, que no nosso caso é o **/etc/grafana** que o grafana já iniciaria normalmente.

```
# grafana-server --homepath /etc/grafana
```

Porém, para deixar as coisas mais automatizadas, criei um script de inicialização.

**4** - Crie a pasta de logs:

```
# mkdir -p /var/log/grafana
```

**5** - Faça o download do script:

```
# wget -O /etc/rc.d/rc.grafana-server https://github.com/eurodrigolira/slackware/blob/master/grafana/rc.grafana-server
```

**6** - Vamos dar permissão de execução:

```
# chmod +x /etc/rc.d/rc.grafana-server
```

**7** - Agora só inicializar o Grafana:

```
# /etc/rc.d/rc.grafana-server start
```

Outras possibilidades:

```
# /etc/rc.d/rc.grafana-server stop (para o serviço)

# /etc/rc.d/rc.grafana-server restart (reinicia o serviço)

# /etc/rc.d/rc.grafana-server status (verifica status o serviço)
```

**8** - Configure para o grafana inicializar junto com o sistema operacional, adicione as linhas abaixo no arquivo **/etc/rc.local**:

```
if [ -x /etc/rc.d/rc.grafana-server ]; then
  /etc/rc.d/rc.grafana-server start
fi
```

Pronto, até a próxima :D
