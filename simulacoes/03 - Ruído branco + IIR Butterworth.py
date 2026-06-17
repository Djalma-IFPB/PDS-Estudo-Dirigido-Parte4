import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz, firwin

# --- Teoria --- #
# Questão 3: Repetir o experimento anterior (Questão 2) com um filtro IIR Butterworth e comparar com o FIR.
#
# Teoria:
# A Questão 2 envolveu a filtragem de um sinal com ruído branco aditivo usando um filtro FIR passa-baixa. A Questão 3 propõe repetir este experimento utilizando um filtro IIR (Infinite Impulse Response) do tipo Butterworth.
# Filtros Butterworth são conhecidos por sua resposta de frequência máxima plana na banda passante e uma atenuação monotônica na banda de rejeição. Eles são projetados usando a função `butter` da `scipy.signal`.
# A principal diferença em relação ao FIR é que os filtros IIR geralmente alcançam uma atenuação semelhante com uma ordem muito menor, mas introduzem distorção de fase (fase não-linear) e podem ser instáveis se os polos não estiverem dentro do círculo unitário. A comparação entre os dois tipos de filtro deve focar na eficácia da redução de ruído, na distorção do sinal de interesse e nas características de fase.

# --- Parâmetros do Sinal --- #
fs = 1000  # Frequência de amostragem (Hz)
T = 1      # Duração do sinal (segundos)
n = int(T * fs) # Número de amostras
t = np.linspace(0, T, n, endpoint=False) # Vetor de tempo

# Sinal original (uma senoide)
f_sinal = 50 # Frequência do sinal de interesse (Hz)
sinal_original = np.sin(2 * np.pi * f_sinal * t)

# Ruído branco aditivo
ruido = 0.5 * np.random.randn(n) # Ruído gaussiano com amplitude 0.5

sinal_com_ruido = sinal_original + ruido

# --- Projeto do Filtro IIR Butterworth Passa-Baixa --- #
fc_iir = 80    # Frequência de corte do filtro IIR (Hz)
ordem_iir = 4  # Ordem do filtro IIR (geralmente menor que FIR para desempenho similar)

# Normaliza a frequência de corte para o intervalo [0, 1]
nyquist = 0.5 * fs
normal_cutoff_iir = fc_iir / nyquist

b_iir, a_iir = butter(ordem_iir, normal_cutoff_iir, btype='low', analog=False)

# --- Aplicação do Filtro IIR --- #
sinal_filtrado_iir = lfilter(b_iir, a_iir, sinal_com_ruido)

# --- Projeto do Filtro FIR (para comparação) --- #
fc_fir = 80    # Frequência de corte do filtro FIR (Hz)
ordem_fir = 101 # Ordem do filtro FIR
normal_cutoff_fir = fc_fir / nyquist
b_fir = firwin(ordem_fir, normal_cutoff_fir, window='hann', pass_zero='lowpass')
a_fir = 1.0
sinal_filtrado_fir = lfilter(b_fir, a_fir, sinal_com_ruido)

# --- Análise da Resposta em Frequência dos Filtros --- #
w_iir, h_iir = freqz(b_iir, a_iir, worN=8000)
freq_resp_iir = 0.5 * fs * w_iir / np.pi

w_fir, h_fir = freqz(b_fir, a_fir, worN=8000)
freq_resp_fir = 0.5 * fs * w_fir / np.pi

# --- Plotagem dos Resultados --- #
plt.figure(figsize=(14, 15))

# Sinal Original e com Ruído
plt.subplot(5, 1, 1)
plt.plot(t, sinal_original)
plt.title('Sinal Original ({}Hz)'.format(f_sinal))
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(5, 1, 2)
plt.plot(t, sinal_com_ruido)
plt.title('Sinal Original com Ruído Branco Aditivo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Sinal Filtrado IIR
plt.subplot(5, 1, 3)
plt.plot(t, sinal_filtrado_iir, color='orange')
plt.title('Sinal Filtrado IIR Butterworth (Fc={}Hz, Ordem={})'.format(fc_iir, ordem_iir))
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Sinal Filtrado FIR
plt.subplot(5, 1, 4)
plt.plot(t, sinal_filtrado_fir, color='green')
plt.title('Sinal Filtrado FIR (Fc={}Hz, Ordem={})'.format(fc_fir, ordem_fir))
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Resposta em Frequência dos Filtros
plt.subplot(5, 1, 5)
plt.plot(freq_resp_iir, 20 * np.log10(abs(h_iir)), label='IIR Butterworth (Ordem={})'.format(ordem_iir), color='orange')
plt.plot(freq_resp_fir, 20 * np.log10(abs(h_fir)), label='FIR (Ordem={})'.format(ordem_fir), color='green', linestyle='--')
plt.axvline(fc_iir, color='red', linestyle='--', label='Frequência de Corte ({}Hz)'.format(fc_iir))
plt.title('Resposta em Frequência dos Filtros IIR e FIR')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Ganho (dB)')
plt.xlim(0, fs/2)
plt.ylim(-60, 6)
plt.grid(True)
plt.legend()