from control.matlab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
num = [1.13]
den = [443, 1]
G = tf(num, den)
y, t = step(G)
t1 = [x+84 for x in  t]
plt.figure(figsize = (2560/96, 1080/96))
mpl.rc('text', usetex = True)
plt.plot([-300, 0],[0,0], linewidth = 3, color = 'tab:blue')
plt.plot(t, y, label = 'Resposta sem atraso', linewidth = 3, color = 'tab:blue')
plt.plot([-300, 84],[0,0], linewidth = 3, color = 'tab:orange')
plt.plot(t1, y, label = 'Resposta com atraso', linewidth = 3, color = 'tab:orange')
plt.xlabel('tempo (s)', fontsize=22)
plt.ylabel('Amplitude (°C)', fontsize=22)
plt.title('Resposta ao degrau com e sem atraso', fontsize = 24)
plt.xticks([0,84,500,1000,1500,2000,2500,3000], fontsize=22)
plt.yticks(fontsize=22)
plt.xlim(-150, 3050)
plt.ylim(-.06, 1.2)
plt.legend(loc = 4, fontsize=22)
plt.grid()
plt.savefig("FTPlantaExponencial.png",bbox_inches='tight')
plt.show()