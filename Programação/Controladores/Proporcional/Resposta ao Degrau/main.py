from control.matlab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

numRL = [-4.1584, 0.0990095238095238]
denRL = [443, 11.547619047619, 0.0238095238095238]
numF = [-5.147997499999999, 0.12257136904761902]
denF = [443, 11.547619047619, 0.0238095238095238]
GRL = tf(numRL, denRL)
GF = tf(numF, denF)
GRL = feedback(GRL, 1)
GF = feedback(GF, 1)
yRL, tRL = step(GRL, T = np.linspace(0, 1000, 20000) )
yF, tF = step(GF, T = np.linspace(0, 1000, 20000))

degrau = [[-200,0,0.0000001,1000], [0, 0, 1, 1]]
plt.figure(figsize = (2560/96, 1080/96))
plt.plot(degrau[0], degrau[1], label = 'Sinal de entrada', linewidth = 3, color = 'tab:orange')
plt.plot(tRL, yRL, label = 'Root Locus', linewidth = 3, color = 'tab:blue')
plt.plot(tF, yF, label = 'Frequência', linewidth = 3, color = 'tab:green')
plt.title('Respostas com controlador proporcional', fontsize = 24)
plt.xlabel('Tempo (s)', fontsize=22)
plt.ylabel('Amplitude (°C)', fontsize=22)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.xlim(-35, 1000)
plt.legend(loc = 4, fontsize=22)
plt.grid()
plt.savefig("RespostaControleProporcional.png",bbox_inches='tight')
plt.show()
plt.show()