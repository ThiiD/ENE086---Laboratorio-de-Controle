from control.matlab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

G = tf([-1.13, 0.0269], [443, 11.55, 0.0238])
Gint = tf([0.00145], [1, 0])
Kc = 12
T = 95.47993082771802
alpha = 0.044
Gc = tf([Kc*T, Kc], [(alpha*T), 1])

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
plt.savefig("BodeNaoCompensadoAvançoDeFase.png",bbox_inches='tight')



Gg = tf([12],[1]) * Gint * G
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
plt.savefig("BodeComGanhoAvançoDeFase.png",bbox_inches='tight')



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
ax2.set_ylim([-360,0])
ax2.set_xscale('log')
ax2.set_yticks([-360, -270, -180, -90, 0])
ax2.grid()
plt.savefig("BodeCompensadoAvancoDeFase.png",bbox_inches='tight')

#------------------------------------------------------------------------
zrl = 0.0035
prl = 0.0238
Kcrl = 32.7
Gcrl = tf([Kcrl, zrl*Kcrl], [1, prl])

GGcrl = Gcrl *  Gint * G
FTrl = feedback(GGcrl, 1)
yRL, tRL = step(FTrl, np.linspace(0,5300,5300))

plt.figure(figsize = (2560/96, 1080/96))
FT = feedback(GGc, 1)
y, t = step(FT)
degrau = [[-200,0,0.0000001,6000], [0, 0, 1, 1]]
plt.plot(degrau[0], degrau[1], label = 'Referência', linewidth = 3, color = 'tab:orange')
plt.plot(t,y, color = 'tab:blue', label = 'Sis. Compensado - Bode', linewidth = 3)
plt.plot(tRL,yRL, color = 'tab:green', label = 'Sis. Compensado - RL', linewidth = 3)
#plt.plot([1830,5300],[1,1], color = 'tab:green', linewidth = 3)
plt.xlim([-200, 5300])
plt.title('Respostas com Compensador por avanço de fase', fontsize = 24)
plt.xlabel('Tempo (s)', fontsize=22)
plt.ylabel('Amplitude (°C)', fontsize=22)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.legend(loc = 'upper right', fontsize=22)
plt.grid()
plt.savefig("RespostaDegrauBode.png",bbox_inches='tight')




# ---------------------------------------------------------------------
plt.figure(figsize = (2560/96, 1080/96))
GGcrl = Gcrl *  Gint * G
GGc = Gc *  Gint * G
FTrl = feedback(GGcrl, 1)
FTrl = FTrl * tf([1], [1, 0])
yRL, tRL = step(FTrl, np.linspace(0,5300,5300))
FT = feedback(GGc, 1)
FT = FT * tf([1], [1, 0])
y, t = step(FT, np.linspace(0,5300,5300))
yR, tR = ref = step(tf([1],[1, 0]), np.linspace(0,4000,4000))
plt.plot(tR,yR, color = 'tab:orange', label = 'Referência', linewidth = 3)
plt.plot(t,y, color = 'tab:blue', label = 'Sis. Compensado - Bode', linewidth = 3)
plt.plot(tRL,yRL, color = 'tab:green', label = 'Sis. Compensado - RL', linewidth = 3)
plt.xlim([0, 4000])
plt.ylim([-200, 4000])
plt.title('Respostas com Compensador por avanço de fase', fontsize = 24)
plt.xlabel('Tempo (s)', fontsize=22)
plt.ylabel('Amplitude (°C)', fontsize=22)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.legend(loc = 'upper right', fontsize=22)
plt.grid()
plt.savefig("RespostaRampaBode.png",bbox_inches='tight')
plt.show()
