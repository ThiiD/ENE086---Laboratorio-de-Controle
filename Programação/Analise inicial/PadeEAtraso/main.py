from control.matlab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
num = [1.13]
den = [443, 1]
numD= [-1.13, 0.0269047619047619]
denD = [443, 11.547619047619, 0.0238095238095238]
G = tf(num, den)
GD = tf(numD, denD)
y, t = step(G)
yD, tD = step(GD)
t = [x+84 for x in  t]
plt.figure(figsize = (2560/96, 1080/96))
mpl.rc('text', usetex = True)
plt.plot([-300, 0],[0,0], '--', linewidth = 3, color = 'tab:blue', zorder = 3)
plt.plot(tD, yD, '--', label = 'Aproximação de Padé', linewidth = 3, color = 'tab:blue', zorder = 3)
plt.plot([-300, 84],[0,0], linewidth = 3, color = 'tab:orange')
plt.plot(t, y, label = 'Resposta com atraso', linewidth = 3, color = 'tab:orange')
plt.title('Comparação entre a resposta com atraso e Aproximação de Padé', fontsize = 24)
plt.xlabel('Tempo (s)', fontsize=22)
plt.ylabel('Amplitude (°C)', fontsize=22)
plt.xticks([0,84,500,1000,1500,2000,2500,3000], fontsize=22)
plt.yticks(fontsize=22)
plt.xlim(-150, 3050)
plt.ylim(-.06, 1.2)
plt.legend(loc = 4, fontsize=22)
plt.grid()
plt.savefig("PadeEAtraso.png",bbox_inches='tight')
plt.show()