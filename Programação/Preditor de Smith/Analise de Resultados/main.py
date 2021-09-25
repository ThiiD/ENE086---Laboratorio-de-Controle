import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv', sep=',')
plt.figure(figsize=(2560/96, 1080/96))
plt.plot([-20,0,0.00001,800], [0,0,1,1], color = 'tab:orange', linewidth = 3, label = 'Referência')
plt.plot(data['tempo'], data['ziegler'], color = 'tab:blue', linewidth = 3, label = 'Ziegler-Nichols')
plt.plot(data['tempo'], data['itae'], color = 'tab:green', linewidth = 3, label = 'ITAE')
plt.plot(data['tempo'], data['pidtuner'], color = 'tab:red', linewidth = 3, label = 'pidtuner')
plt.xlim([-20, 800])
plt.legend(loc = 'lower right', fontsize = 22)
plt.title('Resposta ao degrau', fontsize = 24)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude (°C)', fontsize = 22)
plt.grid()
plt.savefig('RespostaDegrauControladoresPID.png', bbox_inches='tight')
plt.show()