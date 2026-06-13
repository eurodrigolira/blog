---
title: "Linux Performance Tuning (Recursos de Hardware)"
date: 2026-05-31
draft: true
category: 
  - "linux"
tag: 
  - "performance"
  - "tuning"
  - "ajustes"
  - "hardware"

---

Salve Salve Pessoal!

Continuando nossa série de posts sobre Performance Tuning no Linux, hoje vamos ver algumas ferramentas básicas que podemos identificar e visualizar qual o hardware que nós estamos trabalhando.

## Introdução

Antes de sair ajustando parâmetros de kernel, tunando aplicações ou analisando gargalos de performance, é fundamental entender o ambiente onde tudo está rodando. Conhecer o hardware, seja físico ou virtual, é o primeiro passo para qualquer análise de desempenho eficiente.

Muitas vezes, problemas de performance não estão diretamente ligados à aplicação, mas sim a limitações ou características do próprio hardware, como número de CPUs, topologia NUMA, tipo de armazenamento, sistemas de arquivos, ou até mesmo configurações aplicadas pelo hypervisor ou pela versão do seu sistema operacional.

Felizmente, o Linux disponibiliza uma série de ferramentas que nos permitem inspecionar detalhadamente esses recursos. Nesse post vamos explorar algumas dessas ferramentas.

## Ferramentas

### dmesg

O dmesg exibe as mensagens do buffer do kernel, sendo uma das primeiras ferramentas que devemos consultar ao investigar o hardware.

Com ele, conseguimos visualizar o processo de detecção de dispositivos durante o boot, incluindo CPUs, memória, discos e drivers carregados. Também é extremamente útil para identificar erros ou falhas de hardware.

Em sua saída padrão ele exibe todo o buffer, mas podemos fazer filtros simples com o **grep** e filtrar por determinados tipos de recursos.

```bash
dmesg | grep -i disk --color
```

![](/images/dmesg1.png)

Por padrão ele não exibe a hora em formato legivel, então podemos usar o **-T** para ele converter.

```bash
dmesg -T
```

![](/images/dmesg2.png)

### dmidecode

O dmidecode acessa informações da BIOS Gerenciamento de sistema
(SMBIOS, System Management BIOS) e Interface gerenciamento de área de trabalho (DMI,
Desktop Management Interface).

Com ele, conseguimos obter detalhes como fabricante do servidor, modelo, versão da BIOS, quantidade de memória instalada, slots disponíveis, informações sobre CPUs, etc. É uma ferramenta essencial para inventário de hardware físico.

Os dados exibidos na saída do comando podem ser encontrados no diretório **/sys/class/dmi/id** e são obtidos pelo sistema de arquivos **sysfs**.

![](/images/dmidecode.png)

### lscpu

O lscpu apresenta informações detalhadas sobre a arquitetura da CPU.

Entre os dados disponíveis, temos número de sockets, cores, threads, frequência, flags de CPU e informações sobre NUMA. É uma ferramenta indispensável para entender como o processamento está organizado no sistema.

A opção -e exibe:

![](/images/lscpu-e.png)

A opção -p exibe:

![](/images/lscpu-p.png)

### lsusb

O lsusb lista todos os dispositivos conectados às portas USB.

Apesar de simples, pode ser útil para identificar dispositivos externos que podem impactar performance, como adaptadores de rede, storage externo ou dispositivos específicos utilizados pela aplicação.

### lstopo

Parte do pacote hwloc, o lstopo fornece uma visualização da topologia do hardware.

Ele mostra de forma hierárquica como CPUs, caches, memória e dispositivos estão organizados, sendo extremamente útil para entender ambientes com NUMA e otimizar o uso de CPU e memória.

### lshw

O lshw é uma ferramenta bastante completa para listar informações detalhadas de hardware.

Ele apresenta uma visão abrangente de CPU, memória, discos, interfaces de rede e outros dispositivos, incluindo capacidades, configurações e estado atual.

### virsh dumpxml

Para ambientes virtualizados com KVM/libvirt, o virsh dumpxml permite visualizar a configuração completa de uma máquina virtual.

Através dele, conseguimos entender quantas CPUs estão alocadas, quantidade de memória, tipo de disco, interfaces de rede e diversas outras configurações que impactam diretamente na performance da VM.

### kvm_stat

O kvm_stat fornece estatísticas em tempo real sobre o funcionamento do KVM.

Ele mostra métricas relacionadas a exits de virtualização, que ajudam a entender como o hypervisor está interagindo com a VM — informação valiosa para troubleshooting de performance em ambientes virtualizados.

### perf-kvm

O perf-kvm é uma extensão do perf voltada para análise de performance em ambientes KVM.

Com ele, é possível analisar eventos tanto no host quanto nas VMs, permitindo identificar gargalos mais profundos relacionados à virtualização, como latência de CPU e comportamento de instruções.

### getconf

O getconf -a retorna parâmetros de configuração do sistema, incluindo limites e capacidades definidas pelo POSIX e pelo kernel.

Embora não seja uma ferramenta exclusivamente de hardware, ela fornece informações importantes como número de processadores disponíveis (_NPROCESSORS_ONLN) e outras configurações que impactam diretamente na performance.


## Conclusão

Como vimos, antes de qualquer ajuste de performance, é essencial conhecer bem o terreno onde estamos pisando. Essas ferramentas nos dão uma visão clara e detalhada do hardware — seja físico ou virtual — permitindo tomar decisões mais assertivas durante o processo de tuning.

Nos próximos posts, vamos sair um pouco dessa visão mais estática do ambiente e começar a explorar ferramentas que nos mostram o comportamento do sistema em tempo real, analisando consumo de CPU, memória, disco e rede.

Até o próximo post!

🖖🖖🖖

## Referências

* man dmesg
* man getconf
* man dmidecode
* man lscpu
* man lsusb
* man lshw
* man virsh
* man perf