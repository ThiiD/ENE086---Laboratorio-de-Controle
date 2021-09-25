from control.matlab import *
import numpy as np
import matplotlib.pyplot as plt

num = [-5.147997499999999, 0.12257136904761902]
den = [443, 11.547619047619, 0.0238095238095238]
w = np.logspace(-6,2,10000)
G = tf(num, den)
dbode = bode(G, w, plot = False)
GdB = 20*np.log10(dbode[0])
phase = np.rad2deg(dbode[1])
plt.figure(figsize=(2560/96, 1080/96))
plt.plot(w, GdB, linewidth = 3)
plt.xscale('log')
plt.xlim([10**-6, 10**2])
plt.xticks(fontsize = 20)
plt.yticks([-80, -60, -40, -20, 0, 14.2332], [-80, -60, -40, -20, 0, '14,23'], fontsize = 20, color = 'tab:blue')
plt.xlabel('Frequência (rad/s)', fontsize = 20)
plt.ylabel('Módulo (dB)', fontsize = 20, color = 'tab:blue')
plt.title('Diagrama de Módulo', fontsize = 24)
plt.grid()
plt.savefig("DiagramaModuloProporcional.png",bbox_inches='tight')

plt.figure(2, figsize=(2560/96, 1080/96))
plt.plot(w, phase, linewidth = 3, color = 'tab:orange')
plt.xlim([10**-6, 10**2])
plt.xticks(fontsize = 20)
plt.yticks([-270, -180, -90, 0], fontsize = 20, color = 'tab:orange')
plt.xlabel('Frequência (rad/s)', fontsize = 20)
plt.ylabel('Fase (graus)', fontsize = 20, color = 'tab:orange')
plt.title('Diagrama de Fase', fontsize = 24)
plt.xscale('log')
plt.grid()
plt.savefig('DiagramaFaseProporcional', bbox_inches = 'tight')
plt.show()