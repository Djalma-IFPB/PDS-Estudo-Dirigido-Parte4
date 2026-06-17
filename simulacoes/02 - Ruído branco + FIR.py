import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, freqz

# --- Teoria --- #
# Questão 2: Gerar um sinal com ruído branco aditivo; projetar um filtro FIR passa-baixa e avaliar a redução do ruído.
#
# Teoria:
# Ruído branco aditivo é um tipo de ruído aleatório que contém todas as frequências com igual intensidade, adicionado a um sinal original. Para remover esse ruído, um filtro passa-baixa é uma escolha comum, pois o ruído geralmente se manifesta em frequências mais altas do que o sinal de interesse.
# Um filtro FIR (Finite Impulse Response) passa-baixa pode ser projetado usando o método da janela, por exemplo, com a função `firwin` da `scipy.signal`. Este método permite especificar a ordem do filtro e a frequência de corte. Filtros FIR são intrinsecamente estáveis e podem ser projetados com fase linear, o que é vantajoso para evitar distorções de fase no sinal filtrado.
# A avaliação da redução de ruído pode ser feita visualmente, comparando o sinal original com ruído e o sinal filtrado. Idealmente, o sinal filtrado deve apresentar uma versão mais suave do sinal original, com a componente de ruído de alta frequência atenuada.

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

# --- Projeto do Filtro FIR Passa-Baixa --- #
fc = 80    # Frequência de corte do filtro (Hz)
ordem = 101 # Ordem do filtro (deve ser ímpar para fase linear)

# Normaliza a frequência de corte para o intervalo [0, 1], onde 1 é a frequência de Nyquist (fs/2)
nyquist = 0.5 * fs
normal_cutoff = fc / nyquist

# Projeta o filtro FIR usando o método da janela (Hanning)
b = firwin(ordem, normal_cutoff, window="hann", pass_zero="lowpass")
a = 1.0 # Para filtros FIR, o coeficiente 'a' é 1

# --- Aplicação do Filtro --- #
sinal_filtrado = lfilter(b, a, sinal_com_ruido)

# --- Análise da Resposta em Frequência do Filtro --- #
w, h = freqz(b, a, worN=8000)
freq_resp = 0.5 * fs * w / np.pi

# --- Plotagem dos Resultados --- #
plt.figure(figsize=(14, 12))

# Sinal Original e com Ruído
plt.subplot(4, 1, 1)
plt.plot(t, sinal_original, label='Sinal Original')
plt.title('Sinal Original ({}Hz)'.format(f_sinal))
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(t, sinal_com_ruido, label='Sinal com Ruído')
plt.title('Sinal Original com Ruído Branco Aditivo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Sinal Filtrado
plt.subplot(4, 1, 3)
plt.plot(t, sinal_filtrado, label='Sinal Filtrado', color='green')
plt.title('Sinal Após Filtragem FIR Passa-Baixa (Fc={}Hz, Ordem={})'.format(fc, ordem))
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Resposta em Frequência do Filtro
plt.subplot(4, 1, 4)
plt.plot(freq_resp, 20 * np.log10(abs(h)))
plt.axvline(fc, color='red', linestyle='--', label='Frequência de Corte ({}Hz)'.format(fc))
plt.title('Resposta em Frequência do Filtro FIR Passa-Baixa')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Ganho (dB)')
plt.xlim(0, fs/2)
plt.ylim(-60, 6)
plt.grid(True)
plt.legend()