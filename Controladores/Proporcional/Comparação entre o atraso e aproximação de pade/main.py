import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('plotRootLocusComPadeEAtraso.csv', sep=',')
plt.figure(figsize = (2560/96, 1080/96))
plt.plot(data['tempo'], data['atraso'], label = 'Resposta com atraso', linewidth = 3, color = 'tab:orange')
plt.plot(data['tempo'], data['pade'], label = 'Resposta com Padé', linewidth = 3, color = 'tab:blue')
plt.grid()
plt.xlim([0, 2000])
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.title('Comparação entre a resposta com Padé e Atraso de Transporte', fontsize = 24)
plt.legend(loc = 'lower right', fontsize = 22)
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude (°C)', fontsize = 22)
plt.savefig('ComparaçãoPadeEAtrasoDeTransporteControladorProporcional.png', bbox_inches='tight')
plt.show()