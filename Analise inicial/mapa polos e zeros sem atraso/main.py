from control.matlab import *
import matplotlib.pyplot as plt

num = [1.13]
den = [443, 1]
G = tf(num, den)
polos, zeros = pzmap(G, plot= False)
print(f'polos: {polos},    zeros: {zeros}')
plt.figure(figsize = (2560/96, 1080/96))
plt.plot(polos, [0], 'X', color = 'tab:red', label = 'p1 = 0.00225734 + j0',  markersize=40)
plt.grid()
plt.xlim(-.01, 0)
plt.legend(borderpad=2, loc= 'upper right', fontsize = 18)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
plt.xlabel('Eixo real', fontsize=18)
plt.ylabel('Eixo imaginario', fontsize = 18)
plt.title('Mapa de pólos e zeros sem atraso', fontsize= 22)
plt.savefig("mapaSemAtraso.png",bbox_inches='tight')
plt.show()