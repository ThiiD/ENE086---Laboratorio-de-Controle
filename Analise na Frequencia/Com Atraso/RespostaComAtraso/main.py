from control.matlab import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, lsim
import matplotlib as mpl

mpl.rc('text', usetex = True)
num = [-1.13, 0.0269047619047619]
den = [443, 11.547619047619, 0.0238095238095238]
G = lti(num,den)
w_baixa = 10**(-5)
w_media = 10**(-2)
w_alta = 10

# -------------------------- w_baixa ---------------------------
t = np.linspace(0,2*2513274.1228718343,100000)
u_baixa = 1*np.sin(w_baixa*t)
tout_baixa, y_baixa, x_baixa = lsim(G, u_baixa, t)
plt.figure(figsize=(2560/96, 1080/96))
plt.plot(t, u_baixa, linewidth = 3, color = 'tab:orange', label = 'Sinal de Entrada')
plt.plot(t, y_baixa, linewidth = 3, color = 'tab:blue', label = 'Sinal de Saída')
plt.plot([2513274.1228718343, 2*2513274.1228718343], [1.13, 1.13], '--', color = 'black')
plt.plot([2513274.1228718343, 2*2513274.1228718343], [-1.13, -1.13], '--', color = 'black')
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude', fontsize = 22)
plt.title(r'$w = 10^{-5} \, rad/s$', fontsize = 24)
plt.legend(loc = 1, fontsize = 20)
plt.xticks(fontsize = 22)
plt.yticks([-1.13, -1, -.5, 0, .5, 1, 1.13], fontsize = 22)
plt.xlim([2513274.1228718343, 2*2513274.1228718343])
plt.grid()
plt.savefig("w10^-5SemAtraso.png",bbox_inches='tight')

# -------------------------- w_media ---------------------------
t = np.linspace(0, 65973.44572538565, 100000)
u_media = 1*np.sin(w_media*t)
tout_media, y_media, x_media = lsim(G, u_media, t)
plt.figure(figsize=(2560/96, 1080/96))
plt.plot(t, u_media, linewidth = 3, color = 'tab:orange', label = 'Sinal de Entrada')
plt.plot(t, y_media, linewidth = 3, color = 'tab:blue', label = 'Sinal de Saída')
plt.plot([62831.85307179586, 65973.44572538565], [0.24881751098004878, 0.24881751098004878], '--', color = 'black')
plt.plot([62831.85307179586, 65973.44572538565], [-0.24881751098004878, -0.24881751098004878], '--', color = 'black')
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude', fontsize = 22)
plt.title(r'$w = 10^{-2} \, rad/s$', fontsize = 24)
plt.legend(loc = 1, fontsize = 20)
plt.xticks(fontsize = 22)
plt.yticks([-1, -.5, -0.24881751098004878, 0, 0.24881751098004878, .5, 1,], fontsize = 22)
plt.xlim([62831.85307179586, 65973.44572538565])
plt.ylim([-1.1, 1.1])
print(y_media[70000:].max())
plt.grid()
plt.savefig("w10^-2SemAtraso.png",bbox_inches='tight')

# -------------------------- w_alta ---------------------------
t = np.linspace(0, 10002, 10000000)
u_alta = 1*np.sin(w_alta*t)
tout_alta, y_alta, x_alta = lsim(G, u_alta, t)
fig, ax1 = plt.subplots(figsize = (2560/96, 1080/96))
ax1.set_xlabel('Tempo (s)', fontsize = 22)
ax1.set_xlim([9996.521975601947, 10001.296623894705 ])
ax1.set_ylabel('Amplitude', color='tab:orange', fontsize = 22)
ax1.xaxis.set_tick_params(labelsize=22)
ax1.yaxis.set_tick_params(labelsize=22)
entrada, = ax1.plot(t, u_alta, color='tab:orange', linewidth = 3, label = 'Sinal de Entrada')
ax1.tick_params(axis='y', labelcolor='tab:orange')
ax1.grid()

ax2 = ax1.twinx()  

ax2.set_ylabel('Amplitude', color='tab:blue', fontsize = 22) 
saida, = ax2.plot(t, y_alta, color='tab:blue', linewidth = 3, label = 'Sinal de Saída')
ax2.plot([9996.521975601947, 10001.296623894705 ], [-0.0002570395782768865, -0.0002570395782768865], '--', color = 'black')
ax2.plot([9996.521975601947, 10001.296623894705 ], [0.0002570395782768865, 0.0002570395782768865], '--', color = 'black')
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.yaxis.set_tick_params(labelsize=22)
ax2.set_ylim([-0.0004, 0.0004])
plt.legend([entrada, saida], ['Sinal de Entrada', 'Sinal de Saída'], fontsize = 20, loc = 1)
ax2.set_yticks([-.0004, -.0003, -0.0002570395782768865, -0.0002, -0.0001, 0, .0001, .0002, 0.0002570395782768865, .0003, .0004])

plt.title(r'$w = 10^{1} \, rad/s$', fontsize = 24)
plt.savefig("w10^1SemAtraso.png",bbox_inches='tight')
plt.show()