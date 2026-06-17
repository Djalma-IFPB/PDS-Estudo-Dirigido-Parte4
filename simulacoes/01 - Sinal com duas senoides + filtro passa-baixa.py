import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

# --- Teoria --- #
# Questão 1: Gerar um sinal composto por duas senoides de frequências diferentes. Projetar um filtro passa-baixa e verificar quais componentes permanecem após a filtragem.
#
# Teoria:
# Um sinal composto pode ser criado pela soma de múltiplas senoides com diferentes frequências e amplitudes. A filtragem passa-baixa é um processo que permite a passagem de componentes de baixa frequência e atenua (ou bloqueia) componentes de alta frequência.
# O projeto de um filtro digital passa-baixa envolve a definição de sua ordem e da frequência de corte. A função `butter` da biblioteca `scipy.signal` é utilizada para projetar filtros Butterworth, que são conhecidos por terem uma resposta de frequência máxima plana na banda passante e uma atenuação monotônica na banda de rejeição.
# A função `lfilter` aplica o filtro digital a um sinal. Após a filtragem, espera-se que as componentes senoidais com frequência abaixo da frequência de corte do filtro permaneçam, enquanto as componentes com frequência acima da frequência de corte sejam atenuadas.

# --- Parâmetros do Sinal --- #
fs = 1000  # Frequência de amostragem (Hz)
T = 1      # Duração do sinal (segundos)
n = int(T * fs) # Número de amostras
t = np.linspace(0, T, n, endpoint=False) # Vetor de tempo

# Duas senoides com frequências diferentes
f1 = 50    # Frequência da primeira senoide (Hz)
f2 = 200   # Frequência da segunda senoide (Hz)
A1 = 1.0   # Amplitude da primeira senoide
A2 = 0.5   # Amplitude da segunda senoide

sinal_composto = A1 * np.sin(2 * np.pi * f1 * t) + A2 * np.sin(2 * np.pi * f2 * t)

# --- Projeto do Filtro Passa-Baixa --- #
fc = 100   # Frequência de corte do filtro (Hz)
ordem = 4  # Ordem do filtro

# Normaliza a frequência de corte para o intervalo [0, 1], onde 1 é a frequência de Nyquist (fs/2)
nyquist = 0.5 * fs
normal_cutoff = fc / nyquist

# Projeta o filtro Butterworth
b, a = butter(ordem, normal_cutoff, btype='low', analog=False)

# --- Aplicação do Filtro --- #
sinal_filtrado = lfilter(b, a, sinal_composto)

# --- Análise da Resposta em Frequência do Filtro --- #
w, h = freqz(b, a, worN=8000)
freq_resp = 0.5 * fs * w / np.pi

# --- Plotagem dos Resultados --- #
plt.figure(figsize=(14, 10))

# Sinal Composto Original
plt.subplot(3, 1, 1)
plt.plot(t, sinal_composto)
plt.title('Sinal Composto Original (f1={}Hz, f2={}Hz)'.format(f1, f2))
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Sinal Filtrado
plt.subplot(3, 1, 2)
plt.plot(t, sinal_filtrado)
plt.title('Sinal Após Filtragem Passa-Baixa (Fc={}Hz)'.format(fc))
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Resposta em Frequência do Filtro
plt.subplot(3, 1, 3)
plt.plot(freq_resp, 20 * np.log10(abs(h)))
plt.axvline(fc, color='red', linestyle='--', label='Frequência de Corte ({}Hz)'.format(fc))
plt.title('Resposta em Frequência do Filtro Passa-Baixa')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Ganho (dB)')
plt.xlim(0, fs/2)
plt.ylim(-60, 6)
plt.grid(True)
plt.legend()