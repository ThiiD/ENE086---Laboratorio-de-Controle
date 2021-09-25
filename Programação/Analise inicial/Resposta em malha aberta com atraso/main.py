from control.matlab import *
import matplotlib.pyplot as plt
import matplotlib as mpl

num = [1.13]
den = [443, 1]
G = tf(num, den)
y, t = step(G)
t = [x+84 for x in t]
degrau = [[-200,0,0.0000001,3300], [0, 0, 1, 1]]
plt.figure(figsize = (2560/96, 1080/96))
mpl.rc('text', usetex = True)
plt.plot([-300, 84], [0,0], color = 'tab:blue', linewidth = 3)
plt.plot(t,y, label = 'Resposta com atraso', linewidth = 3, color = 'tab:blue')
plt.plot(degrau[0], degrau[1], label = 'Sinal de entrada', linewidth = 3, color = 'tab:orange')
plt.plot([527, 527], [-1, 0.7142962314762701], '--', color = 'black')
plt.plot([-300, 527], [0.7142962314762701, 0.7142962314762701], '--', color = 'black')
plt.plot([1413, 1413], [-1, 1.0737406127443136], '--', color = 'black')
plt.plot([-300, 1413], [1.0737406127443136, 1.0737406127443136], '--', color = 'black')
plt.plot([1856, 1856], [-1, 1.1093033280557303], '--', color = 'black')
plt.plot([-300, 1856], [1.1093033280557303, 1.1093033280557303], '--', color = 'black')
plt.plot([-300, 3500], [1.13, 1.13], '--', color = 'black')
plt.plot(527, 0.7142962314762701, '.', markersize = 15, color = 'black')
plt.plot(1413, 1.0737406127443136, '.', markersize = 15, color = 'black')
plt.plot(1856, 1.1093033280557303, '.', markersize = 15, color = 'black')
plt.title('Resposta ao degrau com atraso', fontsize = 24)
plt.xlabel('Tempo (s)', fontsize=22)
plt.ylabel('Amplitude (°C)', fontsize=22)
plt.xticks([0, 84, 500, 527, 1000, 1413, 1500, 1856, 2000, 2500, 3000],[0, 84,  500, r'$T$', 1000, r'$T_{a5\%}$', 1500, r'$T_{a2\%}$', 2000, 2500, 3000], fontsize=18)
plt.yticks([0, 0.2, 0.4, 0.6, 0.7142962314762701, 0.8, 1.0, 1.0737406127443136, 1.1093033280557303, 1.13], [0, 0.2, 0.4, 0.6, r'$63,2\%$', 0.8, 1.0, r'$95\%$', r'$98,2\%$', 1.13], fontsize=11)
plt.xlim(-150, 3050)
plt.ylim(-.06, 1.2)
plt.legend(loc = 4, fontsize=22)
plt.grid()
plt.savefig("respostaComAtraso.png",bbox_inches='tight')
plt.show()