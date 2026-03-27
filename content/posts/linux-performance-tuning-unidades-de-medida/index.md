---
title: ""
date: 2026-03-27
draft: false
category: 
  - "linux"
tag: 
  - "performance"
  - "tuning"
  - "ajustes"
  - "numfmt"
  - "units"
  - "bc"
  - "dc"
  - "si"
  - "iec"
---

Salve Salve Pessoal!

Dando continuidade à série sobre **Performance Tuning no Linux**, este post aborda um conceito fundamental para análise de métricas, as **Unidades de Medida Computacionais**. Embora seja um tema conceitual, o seu entendimento é essencial para evitar interpretações incorretas durante análises de desempenho e troubleshooting.

## Introdução

Durante atividades de ajustes de desempenho, é comum trabalhar com métricas como:

- Utilização de Memória
- Taxa de transferência de Disco (I/O)
- Throughput de Rede
- Uso do Sistema de Arquivos

Um ponto crítico, porém frequentemente negligenciado, é que essas métricas podem ser apresentadas em diferentes padrões de unidade, dependendo da ferramenta, sistema operacional ou fabricante de hardware.

Essa variação pode introduzir inconsistências na análise, especialmente quando não há clareza entre o uso de:

- Unidades Decimais (**base 10**)
- Unidades Binárias (**base 2**)

## Unidades Decimais (SI)

As unidades decimais seguem o padrão do **Sistema Internacional de Unidades (SI)**, sendo baseadas em potências de **10**. Esse padrão é amplamente adotado por fabricantes de hardware e é o sistema de medida mais comum do mundo.

Os prefixos adotados pelo Sistema Internacional de Unidades (SI) são:

| Nome  | Símbolo | Potência                                 |
|-------|---------|------------------------------------------|
| kilo  | k       | 10³ = 1.000                              |
| mega  | M       | 10⁶ = 1.000.000                          |
| giga  | G       | 10⁹ = 1.000.000.000                      |
| tera  | T       | 10¹² = 1.000.000.000.000                 |
| peta  | P       | 10¹⁵ = 1.000.000.000.000.000             |
| exa   | E       | 10¹⁸ = 1.000.000.000.000.000.000         |

## Unidades Binárias (IEC)

As unidades binárias são definidas pela **Comissão Eletrotécnica Internacional (IEC, International Electrotechnical Commission)** e baseiam-se em potências de **2**, sendo mais adequadas para representação interna em sistemas computacionais.

Os prefixos da Comissão Eletrotécnica Internacional (IEC) são:

| Nome | Símbolo | Potência                                |
|------|---------|-----------------------------------------|
| kibi | Ki      | 2¹⁰ = 1.024                             |
| mebi | Mi      | 2²⁰ = 1.048.576                         |
| gibi | Gi      | 2³⁰ = 1.073.741.824                     |
| tebi | Ti      | 2⁴⁰ = 1.099.511.627.776                 |
| pebi | Pi      | 2⁵⁰ = 1.125.899.906.842.624             |
| exbi | Ei      | 2⁶⁰ = 1.152.921.504.606.846.976         |

## Conversão das Unidades

Embora ambos os padrões sejam amplamente utilizados, é fundamental compreender que **SI** (decimal) e **IEC** (binário) não são equivalentes.

Essa distinção se torna especialmente importante no contexto de sistemas Linux, onde ferramentas e o próprio sistema operacional frequentemente utilizam unidades binárias, enquanto fabricantes de hardware adotam o padrão decimal.

Ter clareza sobre qual unidade está sendo utilizada é fundamental para interpretar corretamente métricas, evitar inconsistências na análise e tomar decisões mais precisas durante o processo de ajustes.

A tabela a seguir apresenta a equivalência entre os múltiplos decimais (SI) e binários (IEC), evidenciando que a diferença relativa entre eles cresce progressivamente.

Esse aumento torna cada vez mais relevante o uso correto das unidades, já que a interpretação incorreta pode gerar erros acumulados significativos, especialmente em ambientes de grande escala.

| SI                                                 | IEC                                               | Diferença |
|----------------------------------------------------|---------------------------------------------------|-----------|
| kilo  (k) 10³ = 1.000                              | kibi (Ki) 2¹⁰ = 1.024                             | 2,4%      |
| mega  (M) 10⁶ = 1.000.000                          | mebi (Mi) 2²⁰ = 1.048.576                         | 4,9%      |
| giga  (G) 10⁹ = 1.000.000.000                      | gibi (Gi) 2³⁰ = 1.073.741.824                     | 7,4%      |
| tera  (T) 10¹² = 1.000.000.000.000                 | tebi (Ti) 2⁴⁰ = 1.099.511.627.776                 | 10,0%     |
| peta  (P) 10¹⁵ = 1.000.000.000.000.000             | pebi (Pi) 2⁵⁰ = 1.125.899.906.842.624             | 12,6%     |
| exa   (E) 10¹⁸ = 1.000.000.000.000.000.000         | exbi (Ei) 2⁶⁰ = 1.152.921.504.606.846.976         | 15,3%     |

Em cenários mais antigos, quando os recursos computacionais eram limitados, essa diferença tinha impacto reduzido. No entanto, com a evolução do hardware e o crescimento exponencial das capacidades, essa discrepância passa a ser cada vez mais relevante.

Em escalas maiores, como em unidades de exabytes, a diferença já ultrapassa 15%, o que pode impactar diretamente análises de capacidade, planejamento e troubleshooting.

## Ferramentas

Agora que já sabemos um pouco mais sobre as unidades de medida, vamos falar sobre quais ferramentas temos disponíveis no Linux que podem nos ajudar.

### numfmt

O **numfmt** faz parte do pacote **GNU coreutils** e é utilizado para converter números de/para formatos legíveis por humanos. Ele é especialmente útil para padronizar saídas de comandos, suportando tanto o padrão **SI** (decimal) quanto **IEC** (binário).

Observe a saída do comando *cat* no arquivo */proc/meminfo*. Ele retorna diversas informações sobre memória, mas vamos focar apenas na primeira linha, que representa o total de memória do sistema:

```
rodrigo@homelab:~$ cat /proc/meminfo | head -n 1
MemTotal:       65527128 kB
```

Interpretar esse valor diretamente não é trivial. Sabemos que ele está em **kB**, então podemos convertê-lo para bytes e, em seguida, para uma unidade mais legível.

Primeiro, convertendo de kB para bytes:

```
rodrigo@homelab:~$ echo 65527128k | numfmt --from=iec
67099779072
```

Agora, convertendo de bytes para uma unidade legível (IEC):

```
rodrigo@homelab:~$ echo 67099779072 | numfmt --to=iec
63G
```

Podemos fazer essa conversão em apenas um comando, para obter mais precisão (casas decimais), podemos usar a opção **--format**:

```
rodrigo@homelab:~$ numfmt --from-unit=1K --to=iec --format="%.2f" 65527128
62.50G
```
{{< alert >}}
**Atenção!** O numfmt arredonda os valores automaticamente!
{{< /alert >}}

### units

Outra ferramenta bastante útil no contexto de conversão de medidas é o **units**, um utilitário de linha de comando projetado especificamente para conversões entre diferentes unidades. Diferente do **numfmt**, que foca principalmente em formatos legíveis (SI e IEC), o units é muito mais abrangente, permitindo converter entre diversos tipos de unidades.

Exemplo:

```
rodrigo@homelab:~$ units -o "%.2f" -t "65527128 kibibytes" "gibibytes"
62.49
```

### bc e dc

Além de ferramentas como o **numfmt** e **units**, o Linux também disponibiliza calculadoras de linha de comando que permitem realizar operações matemáticas com precisão e flexibilidade: o **bc** e o **dc**.

O **bc** (Basic Calculator) é uma calculadora interativa de sintaxe mais amigável, amplamente utilizada em scripts e no dia a dia para operações com números inteiros e ponto flutuante. Já o **dc** (Desk Calculator) é uma calculadora baseada em notação polonesa reversa (RPN), sendo mais poderosa e tradicional, porém menos intuitiva.

Usando **bc** para converter de kB para Bytes e depois para GiB:

```
rodrigo@homelab:~$ echo "65527128 * 1024" | bc
67099779072
rodrigo@homelab:~$ echo "scale=2; 67099779072 / (1024^3)" | bc
62.50
```

Agora um exemplo usando **dc**:

```
rodrigo@homelab:~$ echo "2 k 65527128 1024 * 1024 1024 * * / p" | dc
62.50
```

## Cálculo Manual

Caso não queiramos utilizar ferramentas específicas para conversão, também é possível realizar os cálculos manualmente. Uma forma prática e bastante comum é utilizar o próprio Python como calculadora interativa.

Usando como base o valor da memória (65527128 kB), podemos fazer:

```
>>> (65527128 * 1024) / (1024 ** 3)
62.491539001464844
>>>
```

**Explicação do cálculo:**

1 - 65527128 * 1024 (converte o valor de kB para bytes)  
2 - 1024 ** 3 (representa o total de bytes em 1 GiB)  
3 -	Divisão final (conversão de bytes para GiB)  

## Outras Fontes

Alguns utilitários documentam explicitamente como os valores são calculados e apresentados nos formatos **SI** (decimal) e **IEC** (binário). Esse é o caso do **lsmcli**, ferramenta que faz parte do pacote **libStorageMgmt**.

Na prática, é mais eficiente saber onde consultar essas informações do que memorizar todos os cálculos e conversões. Isso garante maior precisão nas interpretações e mais confiança durante atividades de troubleshooting e performance tuning.

```
rodrigo@homelab:~$  man lsmcli
...
           KiB,                    # 2^10 Bytes
           MiB,                    # 2^20 Bytes
           GiB,                    # 2^30 Bytes
           TiB,                    # 2^40 Bytes
           PiB,                    # 2^50 Bytes
           EiB,                    # 2^60 Bytes
           KB,                     # 10^3 Bytes
           MB,                     # 10^6 Bytes
           GB,                     # 10^9 Bytes
           TB,                     # 10^12 Bytes
           PB,                     # 10^15 Bytes
           EB,                     # 10^18 Bytes
...
```

É isso, pessoal! Espero que tenha ficado claro e que ajude no dia a dia de vocês.

Até o próximo post!

🖖🖖🖖

## Referências

[https://pt.wikipedia.org/wiki/Sistema_Internacional_de_Unidades/](https://pt.wikipedia.org/wiki/Sistema_Internacional_de_Unidades)

[https://physics.nist.gov/cuu/Units/binary.html](https://physics.nist.gov/cuu/Units/binary.html)

[https://pt.wikipedia.org/wiki/Prefixo_binário](https://pt.wikipedia.org/wiki/Prefixo_binário)

[https://man7.org/linux/man-pages/man1/numfmt.1.html](https://man7.org/linux/man-pages/man1/numfmt.1.html)

[https://man7.org/linux/man-pages/man7/units.7.html](https://man7.org/linux/man-pages/man7/units.7.html)

[https://man7.org/linux/man-pages/man1/bc.1p.html](https://man7.org/linux/man-pages/man1/bc.1p.html)