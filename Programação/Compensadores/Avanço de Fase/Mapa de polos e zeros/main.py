from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np


num = [-1.13, 0.0269047619047619]
den = [443, 11.547619047619,0.0238095238095238 ]
numInt = [0.00145]
denInt = [1, 0]
G = tf(num, den)
Gint = tf(numInt, denInt)
FTMA = Gint * G
polos, zeros = pzmap(FTMA, plot= False)
k = 1
print(f'polos: {polos},       zeros: {zeros}')
plt.figure(figsize = (2560/96, 1080/96))
for i in polos:
    plt.plot(np.real(i), 0, 'X', label = f'p{k} = {i}', markersize=30)
    k = k+1

plt.plot(np.real(zeros), [0], 'o', label = f'z1 = {zeros[0]}', markersize = 30)
# plt.figure(figsize = (2560/96, 1080/96))
# plt.plot(polos[0][0], [0], 'X', color = 'tab:orange', label = 'p1 = -0.02380952 + j0',  markersize=30)
# plt.plot(polos[0][1], [0], 'X', color = 'tab:red', label = 'p2 = -0.00225734 + j0',  markersize=30)
# plt.plot(zeros, [0], 'o', color ='tab:blue', label = 'z1 = 0.02380952 + j0',  markersize=30 )

plt.xlim(-.03, .03)
plt.legend(borderpad=1, loc= 'upper right', fontsize = 20)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
plt.xlabel('Eixo real', fontsize=18)
plt.ylabel('Eixo imaginario', fontsize = 18)
plt.title('Mapa de pólos e zeros do Sistema não compensado', fontsize= 22)
plt.grid()
plt.savefig("mapaSistemaNaoCompensado.png",bbox_inches='tight')
plt.show()