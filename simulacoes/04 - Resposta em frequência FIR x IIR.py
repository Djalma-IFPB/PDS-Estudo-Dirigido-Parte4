import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz, firwin

# --- Teoria --- #
# Questão 4: Projetar filtros passa-baixa FIR e IIR com frequências de corte semelhantes; comparar as respostas em frequência e discutir as diferenças observadas.
#
# Teoria:
# Esta questão foca na comparação direta das características de resposta em frequência de filtros FIR e IIR com a mesma frequência de corte. A resposta em frequência de um filtro é composta por sua resposta de magnitude (ganho) e sua resposta de fase.
#
# Filtros FIR (Finite Impulse Response) são conhecidos por sua capacidade de ter uma resposta de fase linear, o que significa que todas as componentes de frequência do sinal são atrasadas pelo mesmo tempo, evitando distorção de fase. No entanto, para obter uma transição abrupta na banda de transição, eles geralmente requerem uma ordem muito alta, o que implica em maior atraso de grupo e maior custo computacional.
#
# Filtros IIR (Infinite Impulse Response), como o Butterworth, podem alcançar uma transição abrupta com uma ordem significativamente menor, resultando em menor atraso e menor custo computacional. Contudo, a principal desvantagem dos filtros IIR é a sua resposta de fase não-linear, que pode introduzir distorção de fase no sinal filtrado, especialmente próximo à frequência de corte. Além disso, filtros IIR podem ser instáveis se seus polos não estiverem dentro do círculo unitário.
#
# A comparação visual das respostas de magnitude e fase permitirá observar essas diferenças teóricas na prática.

# --- Parâmetros do Sinal e Filtros --- #
fs = 1000  # Frequência de amostragem (Hz)
fc = 100   # Frequência de corte comum para ambos os filtros (Hz)
nyquist = 0.5 * fs
normal_cutoff = fc / nyquist

# --- Projeto do Filtro FIR Passa-Baixa --- #
ordem_fir = 101 # Ordem do filtro FIR (ímpar para fase linear)
b_fir = firwin(ordem_fir, normal_cutoff, window='hann', pass_zero='lowpass')
a_fir = 1.0

# --- Projeto do Filtro IIR Butterworth Passa-Baixa --- #
ordem_iir = 4  # Ordem do filtro IIR (menor que FIR para desempenho similar)
b_iir, a_iir = butter(ordem_iir, normal_cutoff, btype='low', analog=False)

# --- Análise da Resposta em Frequência dos Filtros --- #
w_fir, h_fir = freqz(b_fir, a_fir, worN=8000)
freq_resp_fir = 0.5 * fs * w_fir / np.pi

w_iir, h_iir = freqz(b_iir, a_iir, worN=8000)
freq_resp_iir = 0.5 * fs * w_iir / np.pi

# --- Plotagem dos Resultados --- #
plt.figure(figsize=(14, 10))

# Resposta de Magnitude
plt.subplot(2, 1, 1)
plt.plot(freq_resp_fir, 20 * np.log10(abs(h_fir)), label='FIR (Ordem={})'.format(ordem_fir), color='blue')
plt.plot(freq_resp_iir, 20 * np.log10(abs(h_iir)), label='IIR Butterworth (Ordem={})'.format(ordem_iir), color='red', linestyle='--')
plt.axvline(fc, color='gray', linestyle=':', label='Frequência de Corte ({}Hz)'.format(fc))
plt.title('Comparação da Resposta de Magnitude (Ganho) FIR vs IIR')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Ganho (dB)')
plt.xlim(0, fs/2)
plt.ylim(-60, 6)
plt.grid(True)
plt.legend()

# Resposta de Fase
plt.subplot(2, 1, 2)
# Convertendo a fase de radianos para graus
plt.plot(freq_resp_fir, np.unwrap(np.angle(h_fir)) * 180 / np.pi, label='FIR (Ordem={})'.format(ordem_fir), color='blue')
plt.plot(freq_resp_iir, np.unwrap(np.angle(h_iir)) * 180 / np.pi, label='IIR Butterworth (Ordem={})'.format(ordem_iir), color='red', linestyle='--')
plt.axvline(fc, color='gray', linestyle=':', label='Frequência de Corte ({}Hz)'.format(fc))
plt.title('Comparação da Resposta de Fase FIR vs IIR')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (graus)')
plt.xlim(0, fs/2)
plt.grid(True)
plt.legend()
