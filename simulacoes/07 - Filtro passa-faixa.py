import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

# --- Teoria --- #
# Questão 7: Projetar um filtro passa-faixa para selecionar uma frequência específica em um sinal composto; verificar o resultado no domínio da frequência.
#
# Teoria:
# Um filtro passa-faixa (bandpass filter) é projetado para permitir a passagem de componentes de frequência dentro de uma faixa específica e atenuar (ou bloquear) as frequências fora dessa faixa. Isso é particularmente útil quando se deseja isolar uma componente de sinal específica de um sinal composto que contém múltiplas frequências.
#
# O projeto de um filtro passa-faixa Butterworth envolve a definição de duas frequências de corte: uma inferior (fc_low) e uma superior (fc_high). A função `butter` da `scipy.signal` pode ser utilizada para projetar este tipo de filtro, especificando `btype="bandpass"`. A ordem do filtro determina a inclinação da transição entre as bandas passante e de rejeição.
#
# Para verificar o resultado no domínio da frequência, é comum utilizar a Transformada Rápida de Fourier (FFT) para analisar o espectro de frequência do sinal original e do sinal filtrado. Espera-se que, após a filtragem, a componente de frequência desejada seja proeminente, enquanto as outras frequências sejam significativamente atenuadas.

# --- Parâmetros do Sinal --- #
fs = 1000  # Frequência de amostragem (Hz)
T = 1      # Duração do sinal (segundos)
n = int(T * fs) # Número de amostras
t = np.linspace(0, T, n, endpoint=False) # Vetor de tempo

# Sinal composto com três senoides
f1 = 20    # Frequência baixa (Hz)
f2 = 70    # Frequência de interesse (Hz)
f3 = 150   # Frequência alta (Hz)
A1 = 0.8   # Amplitude da primeira senoide
A2 = 1.0   # Amplitude da segunda senoide
A3 = 0.6   # Amplitude da terceira senoide

sinal_composto = A1 * np.sin(2 * np.pi * f1 * t) + \
                 A2 * np.sin(2 * np.pi * f2 * t) + \
                 A3 * np.sin(2 * np.pi * f3 * t)

# --- Projeto do Filtro Passa-Faixa --- #
fc_low = 50   # Frequência de corte inferior (Hz)
fc_high = 90  # Frequência de corte superior (Hz)
ordem = 5     # Ordem do filtro

# Normaliza as frequências de corte para o intervalo [0, 1]
nyquist = 0.5 * fs
normal_cutoff_low = fc_low / nyquist
normal_cutoff_high = fc_high / nyquist

b, a = butter(ordem, [normal_cutoff_low, normal_cutoff_high], btype="bandpass", analog=False)

# --- Aplicação do Filtro --- #
sinal_filtrado = lfilter(b, a, sinal_composto)

# --- Análise no Domínio da Frequência (FFT) --- #
# Sinal Composto
fft_sinal_composto = np.fft.fft(sinal_composto)
freq_sinal = np.fft.fftfreq(n, d=1/fs)

# Sinal Filtrado
fft_sinal_filtrado = np.fft.fft(sinal_filtrado)

# --- Plotagem dos Resultados --- #
plt.figure(figsize=(14, 12))

# Sinal Composto Original no Tempo
plt.subplot(4, 1, 1)
plt.plot(t, sinal_composto)
plt.title("Sinal Composto Original (f1={}Hz, f2={}Hz, f3={}Hz)"
          .format(f1, f2, f3))
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Sinal Filtrado no Tempo
plt.subplot(4, 1, 2)
plt.plot(t, sinal_filtrado)
plt.title("Sinal Filtrado Passa-Faixa (Fc_low={}Hz, Fc_high={}Hz)"
          .format(fc_low, fc_high))
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Espectro de Frequência do Sinal Composto
plt.subplot(4, 1, 3)
plt.plot(freq_sinal[:n//2], np.abs(fft_sinal_composto[:n//2]))
plt.title("Espectro de Frequência do Sinal Composto Original")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, fs/2)
plt.grid(True)

# Espectro de Frequência do Sinal Filtrado
plt.subplot(4, 1, 4)
plt.plot(freq_sinal[:n//2], np.abs(fft_sinal_filtrado[:n//2]))
plt.axvspan(fc_low, fc_high, color="green", alpha=0.2, label="Banda Passante")
plt.title("Espectro de Frequência do Sinal Filtrado")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, fs/2)
plt.grid(True)
plt.legend()