from control.matlab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
num = [1.13]
den = [443, 1]
G = tf(num, den)
y, t = step(G)
degrau = [[-200,0,0.0000001,3300], [0, 0, 1, 1]]
plt.figure(figsize = (2560/96, 1080/96))
mpl.rc('text', usetex = True)
plt.plot(t,y, label = 'Resposta ao degrau', linewidth = 3)
plt.plot(degrau[0], degrau[1], label = 'Sinal de entrada', linewidth = 3)
plt.plot([443, 443], [-1, 0.7142962314762701],'--', color = 'black')
plt.plot([-1000, 443], [0.7142962314762701, 0.7142962314762701], '--', color = 'black')
plt.plot([-1000, 4000], [1.13, 1.13], '--', color = 'black')
plt.plot([1299, 1299], [-1, 1.0737406127443136],'--', color = 'black')
plt.plot([-1000, 1299], [1.0737406127443136, 1.0737406127443136], '--', color='black')
plt.plot([1772, 1772], [-1, 1.1093033280557303],'--', color = 'black')
plt.plot([-1000, 1772], [1.1093033280557303, 1.1093033280557303], '--', color = 'black')
plt.plot(443, 0.7142962314762701, '.', color='black', markersize=15)
plt.plot(1299, 1.0737406127443136, '.', color='black', markersize=15)
plt.plot(1772, 1.1093033280557303, '.', color='black', markersize=15)
plt.xlabel('Tempo (s)', fontsize=22)
plt.ylabel('Amplitude (°C)', fontsize=22)
plt.title('Resposta ao degrau sem atraso', fontsize = 24)
plt.xticks([0, 443, 500, 1000, 1299, 1500, 1772, 2000, 2500, 3000], [0, r'$T$', 500, 1000, r'$T_{a5\%}$', 1500, r'$T_{a2\%}$', 2000, 2500, 3000], fontsize=22)
plt.yticks([0, 0.2, 0.4, 0.6, 0.7142962314762701, 0.8, 1.0, 1.0737406127443136, 1.1093033280557303, 1.13], [0, 0.2, 0.4, 0.6, r'$63,2\%$', 0.8, 1.0, r'$95\%$', r'$98,2\%$', 1.13], fontsize=11)
plt.xlim(-150, 3050)
plt.ylim(-.06, 1.2)
plt.legend(loc = 4, fontsize=22)
plt.grid()
plt.savefig("respostaSemAtraso.png",bbox_inches='tight')
plt.show()