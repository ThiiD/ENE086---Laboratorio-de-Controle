import pandas as pd
import matplotlib.pyplot as plt

dadosPI = pd.read_csv('dadosRootLocusPI.csv', sep = ',')
dadosEE = pd.read_csv('dadosEE.csv', sep=',')
ref = [[-200, 0, 0.00001, 1500], [0, 0, 1, 1]]

# ---------------- Kr = 1 --------------------------------
plt.figure(figsize=(2560/96, 1080/96))
plt.plot(ref[0], ref[1], linewidth = 3, color = 'tab:orange', label = 'Referência')
plt.plot(dadosEE['tKr1'], dadosEE['yKr1'], linewidth = 3, color = 'tab:green', label = 'Sis. Compensado ($k_r = 1$)')
plt.yticks(fontsize = 22)
plt.xticks(fontsize = 22)
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude (°C)', fontsize = 22)
plt.title('Resposta ao degrau', fontsize = 22)
plt.legend(loc = 'lower right', fontsize = 22)
plt.grid()
plt.xlim([-50, 1500])
plt.savefig('RespostaDegrauEEkr1.png', bbox_inches='tight')


# ---------------- Kr = 0,01 -----------------------------
plt.figure(figsize=(2560/96, 1080/96))
plt.plot(ref[0], ref[1], linewidth = 3, color = 'tab:orange', label = 'Referência')
plt.plot(dadosEE['tKr'], dadosEE['yKr'], linewidth = 3, color = 'tab:blue', label = 'Sis. Compensado')
plt.yticks(fontsize = 22)
plt.xticks(fontsize = 22)
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude (°C)', fontsize = 22)
plt.title('Resposta ao degrau', fontsize = 22)
plt.legend(loc = 'lower right', fontsize = 22)
plt.grid()
plt.xlim([-50, 1500])
plt.savefig('RespostaDegrauEEkr.png', bbox_inches='tight')

# -------------- Comparação -----------------------------
plt.figure(figsize=(2560/96, 1080/96))
plt.plot(ref[0], ref[1], linewidth = 3, color = 'tab:orange', label = 'Referência')
plt.plot(dadosEE['tKr'], dadosEE['yKr'], linewidth = 3, color = 'tab:blue', label = 'Alocação de Polos - EE')
plt.plot(dadosPI['tempo'], dadosPI['rootlocuspade'], linewidth = 3, color = 'tab:red', label = 'Controlador PI')
plt.yticks(fontsize = 22)
plt.xticks(fontsize = 22)
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude (°C)', fontsize = 22)
plt.title('Resposta ao degrau', fontsize = 22)
plt.legend(loc = 'lower right', fontsize = 22)
plt.grid()
plt.xlim([-50, 1500])
plt.savefig('ComparaçãoPIeEE.png', bbox_inches='tight')
plt.show()






# plt.figure(figsize = (2560/96, 1080/96))
# plt.plot(dadosPI['tempo'], dadosPI['rootlocuspade'])
# plt.plot(dadosEE['tempo'], dadosEE['controleEE'])
# plt.grid()
# plt.show()


