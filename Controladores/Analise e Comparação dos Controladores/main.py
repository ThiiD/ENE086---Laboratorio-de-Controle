import matplotlib.pyplot as plt
import pandas as pd
from control.matlab import *

dataP = pd.read_csv('dataP.csv', sep=',')
dataI = pd.read_csv('dataI.csv', sep=',')
dataPI = pd.read_csv('dataPI.csv', sep=',')

fig, axs = plt.subplots(3,1, figsize = (2560/96, 1080/96))

# --------- 1 grafico
axs[0].plot(dataP['tempo'], dataP['pade'], linewidth = 3, color = 'tab:blue', label = 'P - Padé')
axs[0].plot(dataP['tempo'], dataP['atraso'], linewidth = 3, color = 'tab:orange', label = 'P - Atraso')
axs[0].set_xlim([0, 2000])
axs[0].grid()
axs[0].legend(loc = 'lower right', fontsize = 22)
axs[0].tick_params(axis = 'both', which = 'major', labelsize = 16)
axs[0].set_xlabel('Tempo (s)', fontsize = 18)
axs[0].set_ylabel('Amplitude (°C)', fontsize = 18)
axs[0].set_title('Comparação entre os controladores', fontsize = 24)

# --------- 2 grafico
axs[1].plot(dataI['tempo'], dataI['kirootlocus'], linewidth = 3, color = 'tab:blue', label = 'I - Padé')
axs[1].plot(dataI['tempo'], dataI['kiatrasorootlocus'], '--', linewidth = 3, color = 'tab:orange', label = 'I - Atraso')
axs[1].set_xlim([0, 6500])
axs[1].grid()
axs[1].legend(loc = 'lower right', fontsize = 22)
axs[1].tick_params(axis = 'both', which = 'major', labelsize = 16)
axs[1].set_xlabel('Tempo (s)', fontsize = 18)
axs[1].set_ylabel('Amplitude (°C)', fontsize = 18)

# --------- 3 grafico
axs[2].plot(dataPI['tempo'], dataPI['rootlocuspade'], linewidth = 3, color = 'tab:blue', label = 'PI - Padé')
axs[2].plot(dataPI['tempo'], dataPI['rootlocusatraso'], linewidth = 3, color = 'tab:orange', label = 'PI - Atraso')
axs[2].set_xlim([0, 1500])
axs[2].grid()
axs[2].legend(loc = 'lower right', fontsize = 22)
axs[2].tick_params(axis = 'both', which = 'major', labelsize = 16)
axs[2].set_xlabel('Tempo (s)', fontsize = 18)
axs[2].set_ylabel('Amplitude (°C)', fontsize = 18)

fig.tight_layout()
plt.savefig('comparacaoControladores.png', bbox_inches = 'tight')

# -------------------------------- Erro ---------------------------------------------------------------------------
fig2, axs2 = plt.subplots(3,1, figsize = (2560/96, 1080/96))

eP = abs(dataP['pade'] - dataP['atraso'])
eI = abs(dataI['kirootlocus'] - dataI['kiatrasorootlocus'])
ePI = abs(dataPI['rootlocuspade'] - dataPI['rootlocusatraso'])

# --------- 1 grafico
axs2[0].plot(dataP['tempo'], eP, linewidth = 3, color = 'tab:blue', label = 'Erro - P')
axs2[0].set_xlim([0, 2000])
axs2[0].grid()
axs2[0].legend(loc = 'upper right', fontsize = 22)
axs2[0].tick_params(axis = 'both', which = 'major', labelsize = 16)
axs2[0].set_xlabel('Tempo (s)', fontsize = 18)
axs2[0].set_ylabel('|erro|', fontsize = 18)
axs2[0].set_title('Comparação de erro dos controladores', fontsize = 24)

# --------- 2 grafico
axs2[1].plot(dataI['tempo'], eI, linewidth = 3, color = 'tab:orange', label = 'Erro - I')
axs2[1].set_xlim([0, 6500])
axs2[1].grid()
axs2[1].legend(loc = 'upper right', fontsize = 22)
axs2[1].tick_params(axis = 'both', which = 'major', labelsize = 16)
axs2[1].set_xlabel('Tempo (s)', fontsize = 18)
axs2[1].set_ylabel('|erro|', fontsize = 18)

# --------- 2 grafico
axs2[2].plot(dataPI['tempo'], ePI, linewidth = 3, color = 'tab:green', label = 'Erro - PI')
axs2[2].set_xlim([0, 1500])
axs2[2].grid()
axs2[2].legend(loc = 'upper right', fontsize = 22)
axs2[2].tick_params(axis = 'both', which = 'major', labelsize = 16)
axs2[2].set_xlabel('Tempo (s)', fontsize = 18)
axs2[2].set_ylabel('|erro|', fontsize = 18)


fig2.tight_layout()
plt.savefig('comparacaoErroControladores.png', bbox_inches = 'tight')
plt.show()