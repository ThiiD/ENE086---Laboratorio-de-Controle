from control.matlab import *
import matplotlib.pyplot as plt

plt.figure(figsize = (2560/96, 1080/96))
degrau = [[-200,0,0.0000001,3300], [0, 0, 1, 1]]
plt.plot(degrau[0], degrau[1], linewidth = 3, color = 'tab:orange', label = 'Sinal de entrada')


num = [1.13]
den = [443, 1]
G = tf(num, den)
y, t = step(G)
plt.plot(t,y, linewidth = 3, color = 'tab:blue', label = 'Resposta sem atraso')


numD = [-1.13, 0.0269047619047619]
denD = [443, 11.547619047619, 0.0238095238095238]
GD = tf(numD, denD)
yD, tD = step(GD)
plt.plot(tD, yD, linewidth = 3, color = 'tab:green', label = 'Resposta com atraso')

plt.xlabel('Tempo (t)', fontsize=22)
plt.ylabel('Amplitude (°C)', fontsize=22)
plt.title('Resposta do sistema', fontsize = 24)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.xlim(-150, 3050)
plt.legend(loc = 4, fontsize=22)
plt.grid()
plt.savefig("respostasEmMalhaAberta.png",bbox_inches='tight')
plt.show()
