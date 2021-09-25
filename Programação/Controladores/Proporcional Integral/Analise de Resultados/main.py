import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv', sep = ',')
plt.figure(figsize = (2560/96, 1080/96))
plt.plot(data['tempo'], data['rootlocuspade'], linewidth = 3, color = 'tab:blue', label = 'Root Locus ($K_p = 3{,}56$)')
plt.plot(data['tempo'], data['bodepade'], linewidth = 3, color = 'tab:orange', label = 'Bode ($K_p = 3{,}398$)')
plt.plot(data['tempo'], data['rootlocusatraso'],'--', linewidth = 3, color = 'tab:red', label = 'Root Locus - atraso')
plt.plot(data['tempo'], data['bodeatraso'],'--', linewidth = 3, color = 'tab:green', label = 'Bode - Atraso')
plt.xlim([0, 1500])
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude (°C)', fontsize = 22)
plt.title('Resposta ao degrau', fontsize = 24)
plt.legend(loc = 'lower right', fontsize = 22)
plt.grid()
plt.savefig('ComparacaoProporcionalIntegral.png', bbox_inches = 'tight')


fig, axs = plt.subplots(2, 1, figsize = (2560/96, 1080/96))
eRlocus = abs(data['rootlocuspade'] - data['rootlocusatraso'])
eBode = abs(data['bodepade'] - data['bodeatraso'])
axs[0].plot(data['tempo'], eRlocus, linewidth = 3, color = 'tab:blue', label = '$e_{rlocus}$')
axs[0].set_xlim(0, 1500)
axs[0].set_xlabel('Tempo (s)', fontsize = 22)
axs[0].set_ylabel('|erro|', fontsize = 22)
axs[0].grid(True)
axs[0].tick_params(axis = 'both', which = 'major', labelsize = 16)
axs[0].legend(fontsize = 22)
axs[0].set_title('Modulo do erro entre as respostas', fontsize = 24)

axs[1].plot(data['tempo'], eBode, linewidth = 3, color = 'tab:orange', label = '$e_{bode}$')
axs[1].set_xlim(0, 1500)
axs[1].set_xlabel('Tempo (s)', fontsize = 22)
axs[1].set_ylabel('|erro|', fontsize = 22)
axs[1].grid()
axs[1].tick_params(axis = 'both', which = 'major', labelsize = 16)
axs[1].legend(fontsize = 22)

fig.tight_layout()
plt.savefig('graficoDosErrosProporcionalIntegral.png', bbox_inches = 'tight')
plt.show()

a = data[['tempo', 'rootlocuspade']]
print(a)
a.to_csv('dadosRootLocusPI.csv', index = False)
