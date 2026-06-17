PDS-Estudo-Dirigido-Parte4

Estudo Dirigido - Processamento Digital de Sinais (PDS) - Parte 4

Disciplina: Processamento Digital de Sinais  
Instituição: Instituto Federal da Paraíba — IFPB  
Curso: Telemática

Descrição:

Estudo Dirigido - Parte 4 da disciplina de Processamento Digital de Sinais (PDS), ministrada no Instituto Federal da Paraíba (IFPB) para os cursos de Engenharia da Computação e Telemática. O objetivo principal deste estudo é aprofundar a compreensão sobre os fundamentos de projeto e análise de filtros digitais, com foco em suas aplicações práticas e características teóricas.

O trabalho aborda conceitos essenciais como filtros FIR (Finite Impulse Response) e IIR (Infinite Impulse Response), suas respostas em frequência e fase, estabilidade, polos e zeros, e o impacto do atraso de grupo em sistemas de comunicação. Através de simulações computacionais em Python, são exploradas as diferenças e aplicações desses filtros, fornecendo uma base sólida para a análise e projeto de sistemas de processamento de sinais.

> Estrutura do Repositório


* README.md                       ( Este arquivo )

> teoria:

* resumo teorico.pdf              ( Resumo teórico fundamentado )

> simulacoes:

01 - Sinal com duas senoides + filtro passa-baixa.py
02 - Ruído branco + FIR.py
03 - Ruído branco + IIR Butterworth.py
04 - Resposta em frequência FIR x IIR.py
05 - Polos e zeros.py
06 - Resposta ao impulso.py
07 - Filtro passa-faixa.py
08 - Comparação de fase.py
09 - Atraso de grupo.py
10 - Aplicação prática sensor agrícola.py

> resultados:

01 - Sinal com duas senoides + filtro passa-baixa.png
02 - Ruído branco + FIR.png
03 - Ruído branco + IIR Butterworth.png
04 - Resposta em frequência FIR x IIR.png
05 - Polos e zeros.png
06 - Resposta ao impulso.png
07 - Filtro passa-faixa.png
08 - Comparação de fase.png
09 - Atraso de grupo.png
10 - Aplicação prática sensor agrícola.png
 
Conteúdos Abordados


> Resumo Teórico:

1. Classificação dos Filtros Digitais
2. Resposta em frequência
3. Resposta em fase
4. Atraso de grupo
5. Estabilidade de filtros digitais (polos e zeros)
6. Aplicações dos Filtros Digitais


> Simulações Computacionais:


## Questões e Simulações:

As questões propostas no estudo dirigido foram resolvidas com base em simulações computacionais utilizando Colab (Python). Cada questão é acompanhada de sua teoria, o script de simulação e os gráficos gerados.

### 1 - Sinal com duas senoides + filtro passa-baixa

**Teoria**: Geração de um sinal composto por múltiplas senoides e aplicação de um filtro passa-baixa para isolar componentes de baixa frequência. A teoria dos filtros passa-baixa e sua aplicação para separar sinais é fundamental para entender como componentes de frequência são seletivamente processados.
**Simulação**: (simulacoes/1 - Sinal com duas senoides + filtro passa-baixa.py)
**Resultado**: (resultados/1 - Sinal com duas senoides + filtro passa-baixa.png)

### 2 - Ruído branco + FIR

**Teoria**: Demonstração da eficácia de um filtro FIR passa-baixa na remoção de ruído branco aditivo de um sinal. A estabilidade inerente e a fase linear dos filtros FIR são destacadas neste contexto.
**Simulação**: (simulacoes/2 - Ruído branco + FIR.py)
**Resultado**: (resultados/2 - Ruído branco + FIR.png)

### 3 - Ruído branco + IIR Butterworth

**Teoria**: Comparação do desempenho de um filtro IIR Butterworth com um filtro FIR na redução de ruído. Esta questão explora as vantagens e desvantagens de cada tipo de filtro em termos de ordem, complexidade e distorção de fase.
**Simulação**: (simulacoes/3 - Ruído branco + IIR Butterworth.py)
**Resultado**: (resultados/3 - Ruído branco + IIR Butterworth.png)

### 4 - Resposta em frequência FIR x IIR

**Teoria**: Análise comparativa das respostas de magnitude e fase de filtros FIR e IIR com frequências de corte semelhantes. O foco é na fase linear dos FIR e na fase não-linear dos IIR.
**Simulação**: (simulacoes/4 - Resposta em frequência FIR x IIR.py)
**Resultado**: (resultados/4 - Resposta em frequência FIR x IIR.png)

### 5 - Polos e zeros

**Teoria**: Representação dos polos e zeros de um filtro IIR no plano Z e discussão da relação entre a localização dos polos e a estabilidade do filtro (critério BIBO).
**Simulação**: (simulacoes/5 - Polos e zeros.py)
**Resultado**: (resultados/5 - Polos e zeros.png)

### 6 - Resposta ao impulso

**Teoria**: Comparação da resposta ao impulso de filtros FIR (finita) e IIR (infinita), explicando as razões fundamentais para essa diferença com base em suas estruturas recursivas e não-recursivas.
**Simulação**: (simulacoes/6 - Resposta ao impulso.py)
**Resultado**: (resultados/6 - Resposta ao impulso.png)

### 7 - Filtro passa-faixa

**Teoria**: Projeto de um filtro passa-faixa para isolar uma frequência específica de um sinal composto, com verificação no domínio da frequência via FFT. Demonstra a capacidade de filtros para segmentar o espectro de um sinal.
**Simulação**: (simulacoes/7 - Filtro passa-faixa.py)
**Resultado**: (resultados/7 - Filtro passa-faixa.png)

### 8 - Comparação de fase

**Teoria**: Análise detalhada da resposta de fase de filtros FIR e IIR, com ênfase no conceito de fase linear e suas implicações na distorção de forma de onda. Reforça a importância da fase em aplicações sensíveis.
**Simulação**: (simulacoes/8 - Comparação de fase.py)
**Resultado**: (resultados/8 - Comparação de fase.png)

### 9 - Atraso de grupo

**Teoria**: Cálculo e comparação do atraso de grupo para filtros FIR e IIR, explicando sua importância crítica em sistemas de comunicação para evitar distorção de fase e ISI.
**Simulação**: (simulacoes/9 - Atraso de grupo.py)
**Resultado**: (resultados/9 - Atraso de grupo.png)

### 10 - Aplicação prática sensor agrícola

**Teoria**: Implementação de uma aplicação prática de filtragem digital para remoção de ruído em um sinal de áudio simulado, utilizando um filtro passa-baixa Butterworth. A interpretação física dos resultados é discutida em termos de melhoria da qualidade do áudio.
**Simulação**: (simulacoes/10 - Aplicação prática sensor agrícola.py)
**Resultado**: (resultados/10 - Aplicação prática sensor agrícola.png)

## Problema Norteador (PBL)
O problema norteador proposto no estudo dirigido envolve o projeto e validação de filtros digitais para reduzir ruídos em sinais provenientes de sensores em um sistema de monitoramento agrícola, sem comprometer as informações relevantes para a tomada de decisão.

As simulações e análises realizadas neste estudo fornecem as ferramentas e o conhecimento necessários para abordar este problema. A escolha entre filtros FIR e IIR, a definição da ordem e das frequências de corte, e a análise das respostas em frequência e fase são passos cruciais para projetar um sistema de filtragem eficaz que atenda aos requisitos de um cenário real como o da agricultura de precisão.

> Como Executar (Esses códigos foram testados no https://colab.research.google.com/)

> Execução:

Abrir ou copiar os códigos dos arquivos para https://colab.research.google.com/ ou algum programas Phyton de sua preferência.

* Referências Bibliográficas

1. OPPENHEIM, A. V.; SCHAFER, R. W. Discrete-Time Signal Processing. 3. ed.
Upper Saddle River: Prentice Hall, 2010.
2. PROAKIS, J. G.; MANOLAKIS, D. G. Digital Signal Processing: Principles,
Algorithms and Applications. 4. ed. New Jersey: Pearson Education, 2007.
3. HAYKIN, S.; VAN VEEN, B. Signals and Systems. 2. ed. New York: Wiley, 2003.
