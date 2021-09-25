import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('DataForno2.csv', sep=',')
plt.figure(figsize=(2560/96, 1080/96))
plt.plot([-20,0,0.0001], [25,25,100], linewidth=3, color = 'tab:orange', zorder = 3)
plt.plot(data['tempo']-1000, data['referencia'], linewidth=3, color = 'tab:orange', label = 'Referência')
plt.plot(data['tempo']-1000, data['temperatura'], linewidth=3, color = 'tab:blue', label = 'Temperatura do Forno')
plt.xlim([-20, 1000])
plt.legend(loc = 'upper left', fontsize = 22)
plt.title('Controle de Temperatura do Forno', fontsize = 24)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude (°C)', fontsize = 22)
plt.grid()
plt.savefig('ControleTemperaturaForno.png', bbox_inches='tight')
plt.show()