---
title: "Configurando o Postfix para o usar o Gmail ou Outlook como Relay no CentOS 7/Red Hat 7/Oracle Linux 7"
date: 2018-08-10
categories: 
  - "linux"
  - "scripts"
tags: 
  - "centos-7"
  - "gmail"
  - "oracle-linux-7"
  - "outlook"
  - "postfix"
  - "red-hat-7"
  - "relay"
  - "scripts"
  - "smtp"
---

[![](images/postfix.png)](images/postfix.png)

Salve Salve Pessoal!

É comum quando criamos scripts de backup ou outros, querermos receber alertas se eles foram bem executados ou não, normalmente agendamos scripts de backup para serem executados a noite ou de madrugada, apesar de podermos enviar um e-mail diretamente do nosso servidor, esbarramos no problema desse e-mail normalmente ser colocado na caixa de spam, assim as vezes acabamos nem vendo que o e-mail chegou.

Para solucionar esse problema, podemos configurar o Postifix para utilizar o Gmail, Outlook e etc como Relay, dessa forma quando enviarmos um e-mail ele não cai na caixa de Spam.

Antes de mais nada precisamos de uma conta em um desses provedores, no **Gmail** ou **Outlook**.

Depois que criar a conta em um dos provedores vamos as configurações do **Sistema Operacional** e **Postfix**.

**1** - Instale as dependências necessárias.

```
# yum install postfix mailx cyrus-sasl cyrus-sasl-plain -y
```

**2** - Crie o arquivo **sasl\_passwd** contendo os dados do provedor de e-mail, usuário e senha.

```
# echo "[smtp.gmail.com]:587 EMAIL:SENHA" > /etc/postfix/sasl_passwd (gmail)

# echo "[smtp-mail.outlook.com]:587 EMAIL:SENHA" > /etc/postfix/sasl_passwd (outlook)
```

**OBS**: troque o EMAIL pelo e-mail criado e SENHA pela senha criada para o e-mail.

**3** - Configure as permissões do arquivo **sasl\_passwd**.

```
# chmod 600 /etc/postfix/sasl_passwd
```

**4** - Agora precisamos configurar o arquivo de configuração do postfix, o **main.cf**.

Com seu editor preferido abra o arquivo **/etc/postfix/main.cf** e insira as seguintes informações:

```
"relayhost = [PROVEDOR]:587"
"smtp_use_tls = yes"
"smtp_sasl_auth_enable = yes"
"smtp_sasl_security_options ="
"smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd"
"smtp_tls_CAfile = /etc/ssl/certs/ca-bundle.crt"
```

**OBS**: Substitua o nome PROVEDOR POR smtp.gmail.com para o Gmail e smtp-mail.outlook.com para o Outlook.

**5** - Vamos compilar o hash da senha configurada no arquivo **sasl\_passwd**.

```
# postmap /etc/postfix/sasl_passwd
```

**6** - Habilite o serviço do postfix.

```
# systemctl enable postfix
```

**7** - Inicie/reiniciar o serviço do postfix.

```
# systemctl restart postfix
```

**8** - Podemos verificar as configurações atuais do postfix executando o comando abaixo.

```
# postconf -n
```

**9** - Agora execute um teste via linha de comando mesmo.

```
# mail -s "Teste de email" e-mail@seudominio.com [TECLE ENTER]

Digite o conteúdo do Teste [TECLE ENTER]

. [DIGITE PONTO E TECLE ENTER PARA ENVIAR O E-MAIL]
```

Pronto, verifique sua caixa de entrada para verificar se o e-mail chegou.

Para facilitar a sua vida, criei um script que faz todo esse processo, quando você executar o script ele vai perguntar a você o endereço de e-mail e a senha, e faz todo o processo por você. :D

Segue abaixo o link de acesso aos scripts.

[https://gitlab.com/eurodrigolira/centos/tree/master/e-mail](https://gitlab.com/eurodrigolira/centos/tree/master/e-mail "https://gitlab.com/eurodrigolira/centos/tree/master/e-mail")

Espero que tenha gostado e até a próxima!
