from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rc('text', usetex = True)

num = [-1.13, 0.0269047619047619]
den = [443, 11.547619047619,0.0238095238095238 ]
numInt = [0.00145]
denInt = [1, 0]

z = 0.0035
p = 0.0238
Gc = tf([1, z],[1, p])
G = tf(num, den)
Gint = tf(numInt, denInt)

FTMAc = Gc*Gint*G

rlist, klistr = rlocus(FTMAc, plot = False)
realPolo1 = []
realPolo2 = []
realPolo3 = []
realPolo4 = []
imagPolo1 = []
imagPolo2 = []
imagPolo3 = []
imagPolo4 = []

for i in range(len(rlist)):
    realPolo1.append(np.real(rlist[i][0]))
    realPolo2.append(np.real(rlist[i][1]))
    realPolo3.append(np.real(rlist[i][2]))
    realPolo4.append(np.real(rlist[i][3]))
    imagPolo1.append(np.imag(rlist[i][0]))
    imagPolo2.append(np.imag(rlist[i][1]))
    imagPolo3.append(np.imag(rlist[i][2]))
    imagPolo4.append(np.imag(rlist[i][3]))

plt.figure(figsize = (2560/96, 1080/96))
plt.plot(realPolo1, imagPolo1, color = 'tab:red', linewidth = 3)
plt.plot(realPolo2, imagPolo2, color = 'tab:blue', linewidth = 3)
plt.plot(realPolo3, imagPolo3, color = 'tab:orange', linewidth = 3)
plt.plot(realPolo4, imagPolo4, color = 'tab:green', linewidth = 3)
plt.plot(realPolo1[0], imagPolo1[0], marker = 'x', markersize = 12, color = 'tab:red')
plt.plot(realPolo2[0], imagPolo2[0], marker = 'x', markersize = 12, color = 'tab:blue')
plt.plot(realPolo3[0], imagPolo3[0], marker = 'x', markersize = 12, color = 'tab:orange')
plt.plot(realPolo4[0], imagPolo4[0], marker = 'x', markersize = 12, color = 'tab:green')
plt.plot(realPolo2[-1], imagPolo2[-1], marker = 'o', markersize = 8, color = 'tab:blue')
plt.plot(realPolo3[-1], imagPolo3[-1], marker = 'o', markersize = 8, color = 'tab:orange')
plt.plot(-0.00375, 0.00651, marker = 'D', markersize = 6, color = 'crimson')
plt.plot(-0.00375, -0.00651, marker = 'D', markersize = 6, color = 'crimson')

plt.xlim([-0.1, 0.1])
plt.xlabel('Eixo Real', fontsize = 22)
plt.ylabel('Eixo Imaginario (j)', fontsize = 22)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.title("Lugar das Raizes", fontsize = 24)
bbox_props = dict(boxstyle="square,pad=0.3", fc="cornsilk", ec="black", lw=2)
plt.annotate(r'Polo = $-0,00375 + j0,00651$ \\ $K$ = $32{,}7$  \\ $\zeta$ = $0,5$', xy=(0, 0.005), xycoords='data', bbox = bbox_props, fontsize = 20)
plt.annotate(r'Polo = $-0,00375 - j0,00651$ \\ $K$ = $32{,}7$ \\ $\zeta$ = $0,5$', xy=(0, -0.003), xycoords='data', bbox = bbox_props, fontsize = 20)
plt.grid()
plt.savefig('SistemaCompensadoAvanco.png', bbox_inches='tight')
plt.show()