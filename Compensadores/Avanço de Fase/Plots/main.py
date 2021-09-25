from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np

G = tf([-1.13, 0.0269], [443, 11.55, 0.0238])
Gint = tf([0.00145], [1, 0])

# --------------------- Root Locus ----------------------
KcRL = 32.7
zRL = 0.0035
pRL = 0.0238
GcRL = tf([KcRL, KcRL*zRL], [1, pRL])
print(f'GcRL: {GcRL}')

# ---------------- Análise na Frequencia ---------------
alpha = 0.044
T = 329.710
KcB = 12

GcB = tf([KcB*T, KcB], [alpha*T, 1] )
print(f'GcB: {GcB}')

# -------------------------------------------------------
# ----------------- Definindo FTs -----------------------
# -------------------------------------------------------
FTMAcRL = GcRL * Gint * G
FTMAcB = GcB * Gint * G

FTMFcRL = feedback(FTMAcRL, 1)
FTMFcB = feedback(FTMAcB, 1)

# -------------------------------------------------------
# ----------------- Diagrama de Bode --------------------
# -------------------------------------------------------

w = np.logspace(-5,3,10000)
dbode = bode(FTMAcB, w, plot = False)
GdB = 20*np.log10(dbode[0])
phase = np.rad2deg(dbode[1])
fig, ax1 = plt.subplots(figsize = (2560/96, 1080/96))
ax1.set_xlabel('Frequência (rad/s)', fontsize = 22)
ax1.set_xlim([10**-5, 10**3])
ax1.set_ylabel('Modulo (dB)', color = 'tab:blue', fontsize = 22)
ax1.xaxis.set_tick_params(labelsize = 20)
ax1.yaxis.set_tick_params(labelsize = 20)
ax1.plot(w, GdB, color = 'tab:blue', linewidth = 3)
ax1.tick_params(axis='y', labelcolor = 'tab:blue')
ax1.set_xscale('log')
ax1.grid()

ax2 = ax1.twinx()
ax2.set_ylabel('Fase (graus)', color = 'tab:orange', fontsize = 22)
ax2.plot(w, phase, color = 'tab:orange', linewidth = 3)
ax2.tick_params(axis='y', labelcolor = 'tab:orange')
ax2.yaxis.set_tick_params(labelsize = 20)
ax2.set_ylim([-360, -90])
ax2.set_xscale('log')
ax2.set_yticks([-360, -270, -180, -90])
ax2.grid()

plt.title('Diagrama de Bode', fontsize = 24)
plt.savefig('BodeCompensadoAvancoDeFase.png',bbox_inches = 'tight')



# -------------------------------------------------------
# ---------------- Resposta ao Degrau -------------------
# -------------------------------------------------------

yDRL, tDRL = step(FTMFcRL, np.linspace(0,5000, 5000))
yDB, tDB = step(FTMFcB, np.linspace(0,5000, 5000))
refD = ([-200, 0, 0.00001, 5000], [0,0,1,1])

plt.figure(figsize = (2560/96, 1080/96))
plt.plot(refD[0], refD[1], color = 'tab:orange', linewidth = 3, label = 'Referência')
plt.plot(tDB, yDB, color = 'tab:blue', linewidth = 3, label = 'Sis. Compensado - Bode')
plt.plot(tDRL, yDRL, color = 'tab:green', linewidth = 3, label = 'Sis. Compensado - Root Locus')
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude (°C)', fontsize = 22)
plt.title('Respostas com Compensador por Avanço de Fase', fontsize = 24)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.xlim([-200, 5000])
plt.legend(loc = 'upper right', fontsize = 22)
plt.grid()
plt.savefig('RespostaDegrauBode.png',bbox_inches = 'tight')


# -------------------------------------------------------
# ----------------- Resposta a Rampa --------------------
# -------------------------------------------------------

integrador = tf([1], [1,0])
yRRL, tRRL = step(FTMFcRL*integrador, np.linspace(0,5000, 5000))
yRB, tRB = step(FTMFcB*integrador, np.linspace(0,5000, 5000))
yR, tR = step(integrador, np.linspace(0,5000, 5000))

plt.figure(figsize = (2560/96, 1080/96))
plt.plot(tR, yR, color = 'tab:orange', linewidth = 3, label = 'Referência')
plt.plot(tRB, yRB, color = 'tab:blue', linewidth = 3, label = 'Sis. Compensado - Bode' )
plt.plot(tRRL, yRRL, color = 'tab:green', linewidth = 3, label = 'Sis. Compensado - Root Locus')
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude (°C)', fontsize = 22)
plt.title('Respostas com Compensador por Avanço de Fase', fontsize = 24)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.xlim([0, 5000])
plt.legend(loc = 'upper left', fontsize = 22)
plt.grid()
plt.savefig('RespostaRampaBode.png',bbox_inches = 'tight')
plt.show()