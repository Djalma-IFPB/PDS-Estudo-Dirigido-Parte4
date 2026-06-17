import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, firwin

# --- Teoria --- #
# Questão 6: Analisar a resposta ao impulso de um filtro FIR e de um filtro IIR; explicar por que um tem resposta finita e o outro infinita.
#
# Teoria:
# A **resposta ao impulso** de um filtro é a sua saída quando a entrada é um impulso unitário (um único valor 1 seguido de zeros). Ela é fundamental para caracterizar o comportamento de um filtro.
#
# **Filtros FIR (Finite Impulse Response)**:
# Como o nome sugere, a resposta ao impulso de um filtro FIR é **finita**. Isso ocorre porque os filtros FIR são não-recursivos, ou seja, a saída atual depende apenas das amostras de entrada atuais e passadas, e não de amostras de saída passadas. Matematicamente, a função de transferência de um filtro FIR tem apenas zeros (o denominador é 1). Quando um impulso unitário é aplicado, a saída do filtro se torna zero após um número finito de amostras, igual à ordem do filtro mais um. Essa característica garante a estabilidade intrínseca dos filtros FIR e a possibilidade de se obter fase linear.
#
# **Filtros IIR (Infinite Impulse Response)**:
# Em contraste, a resposta ao impulso de um filtro IIR é **infinita**. Isso se deve à sua natureza recursiva, onde a saída atual do filtro depende não apenas das amostras de entrada atuais e passadas, mas também das amostras de saída passadas (feedback). Matematicamente, a função de transferência de um filtro IIR possui polos (o denominador não é 1). A presença desses polos faz com que o efeito de um impulso unitário persista indefinidamente na saída do filtro, embora geralmente decaindo exponencialmente se o filtro for estável. Essa recursividade permite que filtros IIR atinjam características de resposta em frequência mais seletivas com uma ordem muito menor em comparação com os FIR, mas introduz a complexidade da estabilidade e da fase não-linear.

# --- Parâmetros --- #
fs = 1000  # Frequência de amostragem (Hz)
num_amostras = 200 # Número de amostras para visualizar a resposta ao impulso

# Impulso unitário
impulso = np.zeros(num_amostras)
impulso[0] = 1

# --- Projeto do Filtro FIR --- #
ordem_fir = 50 # Ordem do filtro FIR
fc_fir = 100   # Frequência de corte (Hz)
nyquist = 0.5 * fs
normal_cutoff_fir = fc_fir / nyquist
b_fir = firwin(ordem_fir + 1, normal_cutoff_fir, window="hann", pass_zero="lowpass") # +1 para ordem_fir coeficientes
a_fir = 1.0

# Resposta ao impulso do FIR
resposta_impulso_fir = lfilter(b_fir, a_fir, impulso)

# --- Projeto do Filtro IIR Butterworth --- #
ordem_iir = 4  # Ordem do filtro IIR
fc_iir = 100   # Frequência de corte (Hz)
normal_cutoff_iir = fc_iir / nyquist
b_iir, a_iir = butter(ordem_iir, normal_cutoff_iir, btype="low", analog=False)

# Resposta ao impulso do IIR
resposta_impulso_iir = lfilter(b_iir, a_iir, impulso)

# --- Plotagem dos Resultados --- #
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.stem(np.arange(num_amostras), resposta_impulso_fir)
plt.title("Resposta ao Impulso de um Filtro FIR (Ordem={})".format(ordem_fir))
plt.xlabel("Amostras")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(np.arange(num_amostras), resposta_impulso_iir)
plt.title("Resposta ao Impulso de um Filtro IIR Butterworth (Ordem={})".format(ordem_iir))
plt.xlabel("Amostras")
plt.ylabel("Amplitude")
plt.grid(True)