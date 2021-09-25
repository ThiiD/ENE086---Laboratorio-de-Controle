from control.matlab import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, lsim
import matplotlib as mpl

mpl.rc('text', usetex = True)
num = [1.13]
den = [443, 1]
G = lti(num,den)
w_baixa = 10**-4
w_media = 10**-3
w_alta = 10**-1

# -------------------------- w_baixa ---------------------------
t = np.linspace(0,2*251327.41228718346,100000)
u_baixa = 1*np.sin(w_baixa*t)
tout_baixa, y_baixa, x_baixa = lsim(G, u_baixa, t)
plt.figure(figsize=(2560/96, 1080/96))
plt.plot(t, u_baixa, linewidth = 3, color = 'tab:orange', label = 'Sinal de Entrada')
plt.plot(t, y_baixa, linewidth = 3, color = 'tab:blue', label = 'Sinal de Saída')
plt.plot([251327.41228718346, 2*251327.41228718346], [1.13, 1.13], '--', color = 'black')
plt.plot([251327.41228718346, 2*251327.41228718346], [-1.13, -1.13], '--', color = 'black')
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude', fontsize = 22)
plt.title(r'$w = 10^{-4} \, rad/s$', fontsize = 24)
plt.legend(loc = 1, fontsize = 20)
plt.xticks(fontsize = 22)
plt.yticks([-1.13, -1, -.5, 0, .5, 1, 1.13], fontsize = 22)
plt.xlim([251327.41228718346, 2*251327.41228718346 ])
plt.grid()
plt.savefig("w10^-4SemAtraso.png",bbox_inches='tight')

# -------------------------- w_media ---------------------------
t = np.linspace(0,2*31415.92653589793,100000)
u_media = 1*np.sin(w_media*t)
tout_media, y_media, x_media = lsim(G, u_media, t)
plt.figure(figsize=(2560/96, 1080/96))
plt.plot(t, u_media, linewidth = 3, color = 'tab:orange', label = 'Sinal de Entrada')
plt.plot(t, y_media, linewidth = 3, color = 'tab:blue', label = 'Sinal de Saída')
plt.plot([31415.92653589793, 2*31415.92653589793], [1.0379249317835233, 1.0379249317835233], '--', color = 'black')
plt.plot([31415.92653589793, 2*31415.92653589793], [-1.0379249317835233, -1.0379249317835233], '--', color = 'black')
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude', fontsize = 22)
plt.title(r'$w = 10^{-3} \, rad/s$', fontsize = 24)
plt.legend(loc = 1, fontsize = 20)
plt.xticks(fontsize = 22)
plt.yticks([-1.0379249317835233, -1, -.5, 0, .5, 1, 1.0379249317835233], fontsize = 22)
plt.xlim([31415.92653589793, 2*31415.92653589793 ])
plt.grid()
plt.savefig("w10^-3SemAtraso.png",bbox_inches='tight')

# -------------------------- w_alta ---------------------------
t = np.linspace(0, 63146.01233715484, 100000)
u_alta = 1*np.sin(w_alta*t)
tout_alta, y_alta, x_alta = lsim(G, u_alta, t)
fig, ax1 = plt.subplots(figsize = (2560/96, 1080/96))
ax1.set_xlabel('Tempo (s)', fontsize = 22)
ax1.set_xlim([62831.853071795864, 63146.01233715484 ])
ax1.set_ylabel('Amplitude', color='tab:orange', fontsize = 22)
ax1.xaxis.set_tick_params(labelsize=22)
ax1.yaxis.set_tick_params(labelsize=22)
entrada, = ax1.plot(t, u_alta, color='tab:orange', linewidth = 3, label = 'Sinal de Entrada')
ax1.tick_params(axis='y', labelcolor='tab:orange')

ax1.grid()

ax2 = ax1.twinx()  
ax2.set_ylabel('Amplitude', color='tab:blue', fontsize = 22) 
saida, = ax2.plot(t, y_alta, color='tab:blue', linewidth = 3, label = 'Sinal de Saída')
ax2.plot([62831.853071795864, 63146.01233715484 ], [-0.02549292980957059, -0.02549292980957059], '--', color = 'black')
ax2.plot([62831.853071795864, 63146.01233715484 ], [0.02549292980957059, 0.02549292980957059], '--', color = 'black')
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.yaxis.set_tick_params(labelsize=22)
ax2.set_ylim([-0.03, 0.03])
plt.legend([entrada, saida], ['Sinal de Entrada', 'Sinal de Saída'], fontsize = 20, loc = 1)
ax2.set_yticks([-0.03, -0.02549292980957059, -0.02, -0.01, 0, 0.01, 0.02, 0.02549292980957059, 0.03])

plt.title(r'$w = 10^{-1} \, rad/s$', fontsize = 24)
plt.savefig("w10^-1SemAtraso.png",bbox_inches='tight')
plt.show()