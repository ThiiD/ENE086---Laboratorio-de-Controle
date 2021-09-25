from control.matlab import *
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv', sep=',')
plt.figure(figsize = (2560/96, 1080/96))
plt.plot(data['tempo'], data['kirootlocus'], linewidth = 3, zorder = 2.5, color = 'tab:blue', label = 'Root Locus ($K_i = 0,00145$)')
plt.plot(data['tempo'], data['kibode'], linewidth = 3, zorder = 2.5, color = 'tab:orange', label = 'Bode ($K_i = 0,00165$)')
plt.plot(data['tempo'], data['kiatrasorootlocus'], '--', linewidth = 3, zorder = 2.5, color = 'tab:red', label = 'Root locus - Atraso')
plt.plot(data['tempo'], data['kiatrasobode'], '--', linewidth = 3, zorder = 2.5, color = 'tab:green', label = 'Bode - Atraso')

plt.legend(loc= 'lower right', fontsize = 22)
plt.title('Resposta ao degrau', fontsize = 24)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude (°C)', fontsize = 22)
plt.xlim([0, 6500])
plt.grid()
plt.savefig('RespostaIntegrador.png', bbox_inches = 'tight')

fig, axs = plt.subplots(2, 1, figsize = (2560/96, 1080/96))
eRlocus = abs(data['kirootlocus'] - data['kiatrasorootlocus'])
eBode = abs(data['kibode'] - data['kiatrasobode'])
axs[0].plot(data['tempo'], eRlocus, linewidth = 3, color = 'tab:blue', label = '$e_{rlocus}$')
axs[0].set_xlim(0, 6500)
axs[0].set_xlabel('Tempo (s)', fontsize = 22)
axs[0].set_ylabel('|erro|', fontsize = 22)
axs[0].grid(True)
axs[0].tick_params(axis = 'both', which = 'major', labelsize = 16)
axs[0].legend(fontsize = 22)
axs[0].set_title('Modulo do erro entre as respostas', fontsize = 24)

axs[1].plot(data['tempo'], eBode, linewidth = 3, color = 'tab:orange', label = '$e_{bode}$')
axs[1].set_xlim(0, 6500)
axs[1].set_xlabel('Tempo (s)', fontsize = 22)
axs[1].set_ylabel('|erro|', fontsize = 22)
axs[1].grid()
axs[1].tick_params(axis = 'both', which = 'major', labelsize = 16)
axs[1].legend(fontsize = 22)

fig.tight_layout()
plt.savefig('graficoDosErrosIntegral.png', bbox_inches = 'tight')
plt.show()