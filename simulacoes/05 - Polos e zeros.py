import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, tf2zpk
from matplotlib.patches import Circle

# --- Teoria --- #
# Questão 5: Representar polos e zeros de um filtro IIR; discutir relação entre localização e estabilidade.
#
# Teoria:
# A estabilidade de um filtro digital IIR (Infinite Impulse Response) é um conceito fundamental, diretamente relacionado à localização de seus polos no plano Z. Um sistema é considerado BIBO (Bounded-Input, Bounded-Output) estável se, para toda entrada limitada, a saída também for limitada. Para filtros digitais, o critério de estabilidade BIBO é satisfeito se e somente se todos os polos da função de transferência do filtro estiverem localizados estritamente DENTRO do círculo unitário no plano Z.
#
# O plano Z é uma ferramenta gráfica para analisar sistemas discretos. Ele é um plano complexo onde o eixo horizontal representa a parte real e o eixo vertical representa a parte imaginária. O círculo unitário é um círculo de raio 1 centrado na origem do plano Z.
#
# - **Polos**: São as raízes do denominador da função de transferência do filtro. A localização dos polos é crítica para a estabilidade. Se um polo estiver fora do círculo unitário, o filtro será instável. Se um polo estiver exatamente sobre o círculo unitário, o filtro é marginalmente estável (pode oscilar indefinidamente).
# - **Zeros**: São as raízes do numerador da função de transferência do filtro. A localização dos zeros afeta a resposta em frequência do filtro (onde o ganho é zero), mas não afeta diretamente a estabilidade do filtro. Eles podem estar dentro, fora ou sobre o círculo unitário sem comprometer a estabilidade.
#
# A representação gráfica dos polos e zeros no plano Z (diagrama de polos e zeros) é uma forma visual de verificar a estabilidade e entender o comportamento de frequência de um filtro.

# --- Parâmetros do Filtro IIR Butterworth --- #
fs = 1000  # Frequência de amostragem (Hz)
fc = 100   # Frequência de corte (Hz)
ordem = 4  # Ordem do filtro

# Normaliza a frequência de corte para o intervalo [0, 1]
nyquist = 0.5 * fs
normal_cutoff = fc / nyquist

# Projeta o filtro Butterworth (retorna coeficientes b e a)
b, a = butter(ordem, normal_cutoff, btype="low", analog=False)

# Calcula os polos e zeros a partir dos coeficientes do filtro
z, p, k = tf2zpk(b, a)

# --- Plotagem dos Polos e Zeros --- #
plt.figure(figsize=(8, 8))

# Desenha o círculo unitário
unit_circle = Circle((0, 0), 1, color="black", fill=False, linestyle="--", label="Círculo Unitário")
plt.gca().add_patch(unit_circle)

# Plota os zeros (círculos)
plt.plot(np.real(z), np.imag(z), "o", markersize=9, label="Zeros", color="blue")

# Plota os polos (x)
plt.plot(np.real(p), np.imag(p), "x", markersize=9, label="Polos", color="red")

plt.title("Diagrama de Polos e Zeros de um Filtro IIR Butterworth")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")
plt.grid(True)
plt.axvline(0, color="gray", linewidth=0.5)
plt.axhline(0, color="gray", linewidth=0.5)
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.legend()
plt.gca().set_aspect("equal", adjustable="box")