import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, firwin, freqz

# --- Teoria --- #
# Questão 9: Calcular e comparar o atraso de grupo de diferentes filtros digitais. Explicar a importância desse parâmetro em sistemas de comunicação.
#
# Teoria:
# O **atraso de grupo** (group delay) é uma medida de como as diferentes componentes de frequência de um sinal são atrasadas ao passar por um sistema, como um filtro. Ele é definido como o negativo da derivada da fase em relação à frequência angular: $\tau_g(\omega) = -\frac{d\phi(\omega)}{d\omega}$.
#
# - **Importância em Sistemas de Comunicação**: Em sistemas de comunicação, a preservação da forma de onda do sinal é crucial para evitar a distorção da informação transmitida. Se o atraso de grupo não for constante em todas as frequências da banda de interesse, as diferentes componentes de frequência do sinal chegarão em momentos diferentes, causando distorção. Isso é conhecido como **distorção de fase** ou **distorção de atraso de grupo**.
#   - Para sinais de banda estreita (como as portadoras moduladas), a distorção de atraso de grupo pode levar à dispersão do pulso e à Interferência Intersímbolo (ISI), degradando a qualidade da comunicação.
#   - Para sinais de banda larga (como áudio ou vídeo), a distorção de atraso de grupo pode causar uma reprodução "borrada" ou "desfocada" do sinal.
#
# - **Filtros FIR vs IIR**: Filtros FIR com fase linear possuem um atraso de grupo constante, o que os torna ideais para aplicações onde a preservação da forma de onda é primordial. Já os filtros IIR, devido à sua fase não-linear, geralmente apresentam um atraso de grupo variável, o que pode ser problemático em certas aplicações de comunicação.

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

# --- Análise do Atraso de Grupo dos Filtros --- #
w_fir, h_fir = freqz(b_fir, a_fir, worN=8000)
freq_resp_fir = 0.5 * fs * w_fir / np.pi

w_iir, h_iir = freqz(b_iir, a_iir, worN=8000)
freq_resp_iir = 0.5 * fs * w_iir / np.pi

# Cálculo do atraso de grupo (em amostras)
# Para filtros FIR de fase linear, o atraso de grupo é constante e igual a (ordem_fir / 2)
# Para filtros IIR, o atraso de grupo é calculado a partir da derivada da fase

# Função para calcular o atraso de grupo (em amostras)
def group_delay(b, a, w):
    _, H = freqz(b, a, worN=w.size)
    phase = np.unwrap(np.angle(H))
    # Aproximação da derivada da fase em relação à frequência angular
    # Atraso de grupo = -d(phase)/d(omega)
    # d(omega) = w[1] - w[0]
    # d(phase) = phase[1:] - phase[:-1]
    # Para evitar problemas de borda, usamos diferenças centrais ou simplesmente a derivada discreta
    gd = -np.diff(phase) / np.diff(w)
    # Preenche o primeiro ponto para ter o mesmo tamanho do w original
    gd = np.insert(gd, 0, gd[0])
    return gd

gd_fir = group_delay(b_fir, a_fir, w_fir)
gd_iir = group_delay(b_iir, a_iir, w_iir)

# --- Plotagem dos Resultados --- #
plt.figure(figsize=(12, 6))

plt.plot(freq_resp_fir, gd_fir / (2 * np.pi) * fs, label="FIR (Ordem={})".format(ordem_fir), color="blue") # Convertendo para amostras
plt.plot(freq_resp_iir, gd_iir / (2 * np.pi) * fs, label="IIR Butterworth (Ordem={})".format(ordem_iir), color="red", linestyle="--") # Convertendo para amostras
plt.axvline(fc, color="gray", linestyle=":", label="Frequência de Corte ({}Hz)".format(fc))
plt.title("Comparação do Atraso de Grupo FIR vs IIR")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Atraso de Grupo (amostras)")
plt.xlim(0, fs/2)
plt.grid(True)
plt.legend()