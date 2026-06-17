import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, lfilter

# --- Teoria --- #
# Questão 10: Pesquisar e implementar uma aplicação prática de filtragem digital, como remoção de ruído em áudio, suavização de sinais de sensores ou filtragem de vibrações mecânicas; apresentar resultados e interpretação física.
#
# Teoria:
# A remoção de ruído em áudio é uma aplicação prática muito comum de filtragem digital. Sinais de áudio frequentemente contêm ruídos indesejados (como chiado, zumbido, ou ruído de fundo) que podem degradar a qualidade da escuta. Filtros digitais podem ser empregados para atenuar essas componentes de ruído, preservando o sinal de áudio de interesse.
#
# Para esta implementação, utilizaremos um filtro passa-baixa Butterworth. A premissa é que o ruído indesejado no áudio geralmente ocupa faixas de frequência mais altas do que as componentes principais da fala ou música. Ao aplicar um filtro passa-baixa, as frequências acima de um determinado limiar (frequência de corte) são atenuadas, resultando em um áudio com menos ruído.
#
# - **Filtro Butterworth**: Escolhido por sua resposta de frequência plana na banda passante e transição suave, minimizando distorções no sinal de áudio desejado.
# - **Frequência de Corte (fc)**: Deve ser selecionada cuidadosamente. Uma fc muito baixa pode remover partes importantes do áudio (deixando-o "abafado"), enquanto uma fc muito alta pode não remover ruído suficiente.
# - **Ordem do Filtro**: Afeta a inclinação da atenuação na banda de transição. Ordens mais altas resultam em transições mais abruptas, mas podem introduzir mais atraso e complexidade computacional.
#
# A interpretação física dos resultados envolve observar a redução do ruído no espectro de frequência e, idealmente, ouvir a melhoria na qualidade do áudio (embora a reprodução de áudio não seja diretamente simulada aqui, o impacto no espectro é um bom indicativo).

# --- Geração de um Sinal de Áudio Simulado com Ruído --- #
fs = 44100  # Frequência de amostragem (Hz) - padrão para áudio
T = 3       # Duração do sinal (segundos)
n = int(T * fs) # Número de amostras
t = np.linspace(0, T, n, endpoint=False) # Vetor de tempo

# Sinal de áudio simulado (tom puro + harmônicos)
f_audio = 440 # Frequência fundamental (Hz)
sinal_audio = 0.6 * np.sin(2 * np.pi * f_audio * t) + \
              0.3 * np.sin(2 * np.pi * 2 * f_audio * t) + \
              0.1 * np.sin(2 * np.pi * 3 * f_audio * t)

# Ruído branco aditivo (simulando chiado de fundo)
ruido = 0.2 * np.random.randn(n)

sinal_com_ruido = sinal_audio + ruido

# --- Projeto do Filtro Passa-Baixa Butterworth --- #
fc = 4000  # Frequência de corte do filtro (Hz) - remover ruído acima de 4kHz
ordem = 5  # Ordem do filtro

# Normaliza a frequência de corte para o intervalo [0, 1]
nyquist = 0.5 * fs
normal_cutoff = fc / nyquist

b, a = butter(ordem, normal_cutoff, btype="low", analog=False)

# --- Aplicação do Filtro --- #
sinal_filtrado = lfilter(b, a, sinal_com_ruido)

# --- Análise no Domínio da Frequência (FFT) --- #
# Sinal com Ruído
fft_sinal_com_ruido = np.fft.fft(sinal_com_ruido)
freq_sinal = np.fft.fftfreq(n, d=1/fs)

# Sinal Filtrado
fft_sinal_filtrado = np.fft.fft(sinal_filtrado)

# --- Plotagem dos Resultados --- #
plt.figure(figsize=(14, 10))

# Sinal com Ruído no Tempo
plt.subplot(3, 1, 1)
plt.plot(t, sinal_com_ruido)
plt.title("Sinal de Áudio Simulado com Ruído")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Sinal Filtrado no Tempo
plt.subplot(3, 1, 2)
plt.plot(t, sinal_filtrado)
plt.title("Sinal de Áudio Após Filtragem Passa-Baixa (Fc={}Hz)".format(fc))
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Espectro de Frequência
plt.subplot(3, 1, 3)
plt.plot(freq_sinal[:n//2], 20 * np.log10(np.abs(fft_sinal_com_ruido[:n//2])), label="Com Ruído")
plt.plot(freq_sinal[:n//2], 20 * np.log10(np.abs(fft_sinal_filtrado[:n//2])), label="Filtrado", linestyle="--")
plt.axvline(fc, color="red", linestyle=":", label="Frequência de Corte ({}Hz)".format(fc))
plt.title("Espectro de Frequência do Sinal de Áudio")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB)")
plt.xlim(0, fs/2)
plt.ylim(-80, 0)
plt.grid(True)
plt.legend()
