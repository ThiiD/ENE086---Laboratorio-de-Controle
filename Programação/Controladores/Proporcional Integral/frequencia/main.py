from control.matlab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

G = tf([-0.00255, 6.0714285714285715e-05],[1, 0.023809523809523808, 0])
w = np.logspace(-5,3,10000)
dbode = bode(G, w, plot = False)
GdB = 20*np.log10(dbode[0])
phase = np.rad2deg(dbode[1])
fig, ax1 = plt.subplots(figsize = (2560/96, 1080/96))
ax1.set_xlabel('Frequência (rad/s)', fontsize = 22)
ax1.set_xlim([10**-5, 10**3])
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
ax2.set_ylim([-270,-90])
ax2.set_xscale('log')
ax2.set_yticks([-270, -180, -90])
ax2.grid()

plt.title('Diagrama de Bode', fontsize = 24)
plt.savefig("DiagramaBodeProporcionalIntegralInicial.png",bbox_inches='tight')


G = tf([-0.00866, 0.00020630714285714287],[1, 0.023809523809523808, 0])
w = np.logspace(-5,3,10000)
dbode = bode(G, w, plot = False)
GdB = 20*np.log10(dbode[0])
phase = np.rad2deg(dbode[1])
fig, ax1 = plt.subplots(figsize = (2560/96, 1080/96))
ax1.set_xlabel('Frequência (rad/s)', fontsize = 22)
ax1.set_xlim([10**-5, 10**3])
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
ax2.set_ylim([-270,-90])
ax2.set_xscale('log')
ax2.set_yticks([-270, -180, -90])
ax2.grid()

plt.title('Diagrama de Bode', fontsize = 24)
plt.savefig("DiagramaBodeProporcionalIntegralInicialFinal.png",bbox_inches='tight')
plt.show()
