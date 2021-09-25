from control.matlab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

data = pd.read_csv('data', sep =',')
fig, ax1 = plt.subplots(figsize = (2560/96, 1080/96))
ax1.set_xlabel('Tempo (s)', fontsize = 22)
ax1.set_xlim([0, 3050])
ax1.set_ylabel('Amplitude', color='tab:orange', fontsize = 22)
ax1.xaxis.set_tick_params(labelsize=22)
ax1.yaxis.set_tick_params(labelsize=22)
entrada, = ax1.plot(data['tempo'], data['pade'], color='tab:orange', linewidth = 3, label = 'Aproximação de Padé')
ax1.tick_params(axis='y', labelcolor='tab:orange')
ax1.grid()

ax2 = ax1.twinx()  

ax2.set_ylabel('Amplitude', color='tab:blue', fontsize = 22) 
saida, = ax2.plot(data['tempo'], data['atraso'], color='tab:blue', linewidth = 3, label = 'Atraso de transporte')
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.yaxis.set_tick_params(labelsize=22)
plt.legend([entrada, saida], ['Aproximação de Padé', 'Atraso de transporte'], fontsize = 22, loc = 'upper left')
#ax2.set_yticks([-.0004, -.0003, -0.0002570395782768865, -0.0002, -0.0001, 0, .0001, .0002, 0.0002570395782768865, .0003, .0004])

plt.title('Comparação entre as respostas com ganho marginalmente estável', fontsize = 24)
plt.savefig("MarginalmenteEstavelProporcional.png",bbox_inches='tight')
plt.show()