import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('DataPreditor.csv', sep=',')
plt.figure(figsize=(2560/96, 1080/96))
plt.plot([-20,0,0.00001,800], [0,0,1,1], color = 'tab:orange', linewidth = 3, label = 'Referência')
plt.plot(data['tempo'], data['amplitude'], linewidth = 3, color = 'tab:blue', label = 'Pi + Preditor de Smith')
plt.xlim([-20, 800])
plt.legend(loc = 'lower right', fontsize = 22)
plt.title('Resposta ao degrau', fontsize = 24)
plt.xticks([0, 84, 100, 200 ,300 ,400, 500, 600, 700, 800], fontsize = 22, rotation = 45)
plt.yticks(fontsize = 22)
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude (°C)', fontsize = 22)
plt.grid()
plt.savefig('RespostaDegrauPISmith.png', bbox_inches='tight')
plt.show()