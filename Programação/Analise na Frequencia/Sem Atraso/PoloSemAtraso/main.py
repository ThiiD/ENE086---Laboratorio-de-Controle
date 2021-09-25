from control.matlab import *
import numpy as np
import matplotlib.pyplot as plt

num = [1]
den = [443, 1]
w = np.logspace(-6,0,10000)
G = tf(num, den)
dbode = bode(G, w,plot = False)
GdB = 20*np.log10(dbode[0])
phase = np.rad2deg(dbode[1])
fig, ax1 = plt.subplots(figsize = (2560/96, 1080/96))
ax1.set_xlabel('Frequência (rad/s)', fontsize = 22)
ax1.set_xlim([10**-6, 10**0])
ax1.set_ylabel('Módulo (dB)', color='tab:blue', fontsize = 22)
ax1.xaxis.set_tick_params(labelsize=20)
ax1.yaxis.set_tick_params(labelsize=20)
ax1.plot(w, GdB, color='tab:blue', linewidth = 3)
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_xscale('log')
ax1.grid()

ax2 = ax1.twinx()  
ax2.set_ylabel('Fase (graus)', color='tab:orange', fontsize = 22) 
ax2.plot(w, phase, color='tab:orange', linewidth = 3)
ax2.tick_params(axis='y', labelcolor='tab:orange')
ax2.yaxis.set_tick_params(labelsize=20)
ax2.set_ylim([-180,180])
ax2.set_xscale('log')
ax2.set_yticks([-135, -90, -45, 0, 45, 90, 135])
ax2.grid()

plt.title('Diagrama de Bode', fontsize = 24)
plt.savefig("PoloSemAtraso.png",bbox_inches='tight')
plt.show()
