from control.matlab import *
import numpy as np
import matplotlib.pyplot as plt

num = [1.13]
den = [443, 1]
w = np.logspace(-6,0,10000)
G = tf(num, den)
dbode = bode(G, w, plot = False)
GdB = 20*np.log10(dbode[0])
phase = np.rad2deg(dbode[1])
plt.figure(figsize=(2560/96, 1080/96))
plt.plot(w, GdB, linewidth = 3)
plt.xscale('log')
plt.xlim([10**-6, 10**0])
plt.xticks(fontsize = 20)
plt.yticks([-50, -40, -30, -20, -10, 0, 1.062], fontsize = 20, color = 'tab:blue')
plt.xlabel('Frequência (rad/s)', fontsize = 20)
plt.ylabel('Módulo (dB)', fontsize = 20, color = 'tab:blue')
plt.title('Diagrama de Módulo', fontsize = 24)
plt.grid()
plt.savefig("DiagramaModuloSemAtraso.png",bbox_inches='tight')
plt.show()

plt.figure(2, figsize=(2560/96, 1080/96))
plt.plot(w, phase, linewidth = 3, color = 'tab:orange')
plt.xlim([10**-6, 10**0])
plt.xticks(fontsize = 20)
plt.yticks([-90, -67.5, -45, -22.5, 0], fontsize = 20, color = 'tab:orange')
plt.xlabel('Frequência (rad/s)', fontsize = 20)
plt.ylabel('Fase (graus)', fontsize = 20, color = 'tab:orange')
plt.title('Diagrama de Fase', fontsize = 24)
plt.xscale('log')
plt.grid()
plt.savefig('DiagramaFaseSemAtraso', bbox_inches = 'tight')
plt.show()