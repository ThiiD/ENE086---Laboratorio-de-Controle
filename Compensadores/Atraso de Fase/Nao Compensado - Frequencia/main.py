from control.matlab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

G = tf([-1.13, 0.0269], [443, 11.55, 0.0238])
Gint = tf([0.00145], [1, 0])
Gc = tf([11*9615.38, 11*1], [150648.96615, 1])

FTNaoCompensado = Gint*G

w = np.logspace(-5,3,10000)
dbode = bode(FTNaoCompensado, w, plot = False)
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
ax2.set_ylim([-360,-90])
ax2.set_xscale('log')
ax2.set_yticks([-360, -270, -180, -90])
ax2.grid()
plt.savefig("BodeNaoCompensadoAtrasoDeFase.png",bbox_inches='tight')



Gg = tf([11],[1]) * Gint * G
w = np.logspace(-5,3,10000)
dbode = bode(Gg, w, plot = False)
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
ax2.set_ylim([-360,-90])
ax2.set_xscale('log')
ax2.set_yticks([-360, -270, -180, -90])
ax2.grid()
plt.savefig("BodeComGanhoAtrasoDeFase.png",bbox_inches='tight')


a = 15.6675
Kc = 11
T = 9615.38

Gc = tf([Kc*T, Kc*1],[a*T, 1])
GGc = Gc *  Gint * G
w = np.logspace(-5,3,10000)
dbode = bode(GGc, w, plot = False)
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
ax2.set_ylim([-360,-90])
ax2.set_xscale('log')
ax2.set_yticks([-360, -270, -180, -90])
ax2.grid()
plt.savefig("BodeCompensadoAtrasoDeFase.png",bbox_inches='tight')

plt.show()