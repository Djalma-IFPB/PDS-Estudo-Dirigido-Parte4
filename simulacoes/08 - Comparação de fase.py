import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, firwin, freqz

# --- Teoria --- #
# Questão 8: Analisar a resposta de fase de um filtro FIR e comparar com a de um filtro IIR; discutir fase linear.
#
# Teoria:
# A **resposta de fase** de um filtro descreve como o filtro altera a fase de cada componente de frequência de um sinal. É uma característica crucial, especialmente em aplicações onde a preservação da forma de onda é importante, como em áudio e telecomunicações.
#
# **Fase Linear**:
# Um filtro possui **fase linear** se o atraso de fase é uma função linear da frequência, ou seja, $\phi(\omega) = -\tau \omega$, onde $\tau$ é um atraso constante. Isso implica que todas as componentes de frequência do sinal são atrasadas pelo mesmo tempo (atraso de grupo constante), evitando distorções na forma de onda do sinal. Filtros FIR podem ser projetados para ter fase linear exata, o que é uma de suas maiores vantagens.
#
# **Fase Não-Linear**:
# Filtros IIR, por outro lado, geralmente apresentam **fase não-linear**. Isso significa que diferentes componentes de frequência são atrasadas por tempos diferentes, o que pode resultar em distorção da forma de onda do sinal. Essa distorção é mais perceptível em sinais que contêm uma ampla gama de frequências e onde a relação de fase entre elas é crítica.
#
# A comparação visual das respostas de fase de um filtro FIR e um IIR demonstrará claramente essa diferença, com o FIR exibindo uma linha reta (ou quase reta) e o IIR mostrando uma curva mais complexa.

# --- Parâmetros dos Filtros --- #
fs = 1000  # Frequência de amostragem (Hz)
fc = 100   # Frequência de corte comum para ambos os filtros (Hz)
nyquist = 0.5 * fs
normal_cutoff = fc / nyquist

# --- Projeto do Filtro FIR Passa-Baixa --- #
ordem_fir = 100 # Ordem do filtro FIR (par para fase linear simétrica)
b_fir = firwin(ordem_fir + 1, normal_cutoff, window="hann", pass_zero="lowpass")
a_fir = 1.0

# --- Projeto do Filtro IIR Butterworth Passa-Baixa --- #
ordem_iir = 4  # Ordem do filtro IIR
b_iir, a_iir = butter(ordem_iir, normal_cutoff, btype="low", analog=False)

# --- Análise da Resposta em Frequência (Fase) dos Filtros --- #
w_fir, h_fir = freqz(b_fir, a_fir, worN=8000)
freq_resp_fir = 0.5 * fs * w_fir / np.pi
phase_fir = np.unwrap(np.angle(h_fir)) * 180 / np.pi # Fase em graus

w_iir, h_iir = freqz(b_iir, a_iir, worN=8000)
freq_resp_iir = 0.5 * fs * w_iir / np.pi
phase_iir = np.unwrap(np.angle(h_iir)) * 180 / np.pi # Fase em graus

# --- Plotagem dos Resultados --- #
plt.figure(figsize=(12, 6))

plt.plot(freq_resp_fir, phase_fir, label="FIR (Ordem={})".format(ordem_fir), color="blue")
plt.plot(freq_resp_iir, phase_iir, label="IIR Butterworth (Ordem={})".format(ordem_iir), color="red", linestyle="--")
plt.axvline(fc, color="gray", linestyle=":", label="Frequência de Corte ({}Hz)".format(fc))
plt.title("Comparação da Resposta de Fase FIR vs IIR")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Fase (graus)")
plt.xlim(0, fs/2)
plt.grid(True)
plt.legend()
