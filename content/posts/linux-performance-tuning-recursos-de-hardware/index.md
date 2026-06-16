---
title: "Linux Performance Tuning (Recursos de Hardware)"
date: 2026-06-16
draft: false
category: 
  - "linux"
tag: 
  - "performance"
  - "tuning"
  - "ajustes"
  - "dmesg"
  - "dmidecode"
  - "lscpu"
  - "lsusb"
  - "lspci"
  - "lstopo"
  - "lshw"

---

Salve Salve Pessoal!

Continuando nossa série de posts sobre Performance Tuning no Linux, hoje vamos ver algumas ferramentas básicas que podemos identificar e visualizar qual o hardware que nós estamos trabalhando.

## Introdução

Antes de sair ajustando parâmetros de kernel, tunando aplicações ou analisando gargalos de performance, é fundamental entender o ambiente onde tudo está rodando. Conhecer o hardware, seja físico ou virtual, é o primeiro passo para qualquer análise de desempenho eficiente.

Muitas vezes, problemas de performance não estão diretamente ligados à aplicação, mas sim a limitações ou características do próprio hardware, como número de CPUs, topologia NUMA, tipo de armazenamento, sistemas de arquivos, ou até mesmo configurações aplicadas pelo hypervisor ou pela versão do seu sistema operacional.

Felizmente, o Linux disponibiliza uma série de ferramentas que nos permitem inspecionar detalhadamente esses recursos. Nesse post vamos explorar algumas dessas ferramentas.

## Ferramentas

### dmesg

O **dmesg** exibe as mensagens do buffer do kernel, sendo uma das primeiras ferramentas que devemos consultar ao investigar o hardware.

Com ele, conseguimos visualizar o processo de detecção de dispositivos durante o boot, incluindo CPUs, memória, discos e drivers carregados. Também é extremamente útil para identificar erros ou falhas de hardware.

Em sua saída padrão ele exibe todo o buffer, mas podemos fazer filtros simples com o **grep** e filtrar por determinados tipos de recursos.

```bash
dmesg | grep -i disk --color
```

![](/images/dmesg1.png)

Por padrão ele não exibe a hora em formato legível, então podemos usar o **-T** para ele converter.

```bash
dmesg -T
```

![](/images/dmesg2.png)

### dmidecode

O **dmidecode** acessa informações da BIOS Gerenciamento de sistema
(SMBIOS, System Management BIOS) e Interface gerenciamento de área de trabalho (DMI,
Desktop Management Interface).

Com ele, conseguimos obter detalhes como fabricante do servidor, modelo, versão da BIOS, quantidade de memória instalada, slots disponíveis, informações sobre CPUs, etc. É uma ferramenta essencial para inventário de hardware físico.

Os dados exibidos na saída do comando podem ser encontrados no diretório **/sys/class/dmi/id** e são obtidos pelo sistema de arquivos **sysfs**.

![](/images/dmidecode.png)

### lscpu

O **lscpu** apresenta informações detalhadas sobre a arquitetura da CPU.

```bash
lscpu
```

![](/images/lscpu.png)

Entre os dados disponíveis, temos número de sockets, cores, threads, frequência, flags de CPU e informações sobre NUMA. É uma ferramenta indispensável para entender como o processamento está organizado no sistema.

Com a opção **-e** exibe informações detalhadas da distribuição de cache por CPU.

```bash
lscpu -e
```

![](/images/lscpu-e.png)

### lsusb

O **lsusb** lista todos os dispositivos conectados às portas USB.

Apesar de simples, pode ser útil para identificar dispositivos externos que podem impactar performance, como adaptadores de rede, storage externo ou dispositivos específicos utilizados pela aplicação.

```bash
lsusb
```

![](/images/lsusb.png)

### lspci

O **lspci** lista todos os dispositivos conectados ao barramento PCI/PCIe do sistema.

Através dele, podemos identificar controladoras de armazenamento, placas de rede, GPUs, controladoras RAID, adaptadores Fibre Channel e diversos outros componentes fundamentais para a análise de desempenho.

```bash
lspci
```

![](/images/lsusb.png)

Uma das grandes vantagens do **lspci** é a possibilidade de visualizar informações detalhadas sobre cada dispositivo, incluindo o driver em uso e os módulos do kernel associados, utilizando opções como:

```bash
lspci -v
lspci -vv
lspci -k
```

### lstopo

Parte do pacote **hwloc**, o lstopo fornece uma visualização da topologia do hardware.

Ele mostra de forma hierárquica como CPUs, caches, memória e dispositivos estão organizados, sendo extremamente útil para entender ambientes com NUMA e otimizar o uso de CPU e memória.

Nós temos a opção com interface gráfica, que visualmente é mais fácil o entendimento.

```bash
lstopo
```

![](/images/lstopo.png)

Também temos a opção sem interface gráfica, mostrando a saída direto no console.

```bash
lstopo-no-graphics
```

![](/images/lstopo-no-graphics.png)

### lshw

O **lshw** é uma ferramenta bastante completa para listar informações detalhadas de hardware.

Ele apresenta uma visão abrangente de CPU, memória, discos, interfaces de rede e outros dispositivos, incluindo capacidades, configurações e estado atual.

```bash
lshw
```

![](/images/lshw.png)

### getconf

O **getconf** retorna parâmetros de configuração do sistema, incluindo limites e capacidades definidas pelo POSIX e pelo kernel.

Embora não seja uma ferramenta exclusivamente de hardware, ela fornece informações importantes como número de processadores disponíveis e outras configurações que impactam diretamente na performance.

```bash
getconf -a
```

![](/images/getconf.png)

### virsh dumpxml

Para ambientes virtualizados com **KVM/libvirt**, o **virsh dumpxml** permite visualizar a configuração completa de uma máquina virtual.

Através dele, conseguimos entender quantas CPUs estão alocadas, quantidade de memória, tipo de disco, interfaces de rede e diversas outras configurações que impactam diretamente na performance da VM.

### kvm_stat

O **kvm_stat** fornece estatísticas em tempo real sobre o funcionamento do KVM.

Ele mostra métricas relacionadas a exits de virtualização, que ajudam a entender como o hypervisor está interagindo com a VM, informação valiosa para troubleshooting de performance em ambientes virtualizados.

### perf-kvm

O **perf-kvm** é uma extensão do **perf** voltada para análise de performance em ambientes KVM.

Com ele, é possível analisar eventos tanto no host quanto nas VMs, permitindo identificar gargalos mais profundos relacionados à virtualização, como latência de CPU e comportamento de instruções.

## Conclusão

Vale lembrar que este post teve como objetivo apresentar as principais ferramentas e seus casos de uso de forma introdutória. Cada uma delas possui diversas opções, parâmetros e funcionalidades avançadas que não foram abordadas aqui. Por isso, sempre que precisar aprofundar seus conhecimentos ou realizar uma análise mais detalhada, consulte a documentação oficial através das páginas de manual (**man pages**), que continuam sendo uma das melhores fontes de informação disponíveis no Linux.

Além disso, recomendo fortemente o hábito de explorar as opções de cada comando utilizando **--help** e a própria documentação do projeto responsável pela ferramenta. Muitas vezes, recursos extremamente úteis passam despercebidos simplesmente por não consultarmos a documentação.

Até o próximo post!

🖖🖖🖖
