from control.matlab import *
import matplotlib.pyplot as plt


num = [-1.13, 0.0269047619047619]
den = [443, 11.547619047619,0.0238095238095238 ]
G = tf(num, den)
polos, zeros = pzmap(G, plot= False)
print(f'polos: {polos},       zeros: {zeros}')
plt.figure(figsize = (2560/96, 1080/96))
plt.plot(polos[0], [0], 'X', color = 'tab:orange', label = 'p1 = -0.02380952 + j0',  markersize=30)
plt.plot(polos[1], [0], 'X', color = 'tab:red', label = 'p2 = -0.00225734 + j0',  markersize=30)
plt.plot(zeros, [0], 'o', color ='tab:blue', label = 'z1 = 0.02380952 + j0',  markersize=30 )

plt.xlim(-.03, .03)
plt.legend(borderpad=1, loc= 'upper right', fontsize = 20)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
plt.xlabel('Eixo real', fontsize=18)
plt.ylabel('Eixo imaginario', fontsize = 18)
plt.title('Mapa de pólos e zeros com atraso', fontsize= 22)
plt.grid()
plt.savefig("mapaComAtraso.png",bbox_inches='tight')
plt.show()