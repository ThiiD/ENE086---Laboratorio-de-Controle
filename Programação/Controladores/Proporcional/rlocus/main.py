from control.matlab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rc('text', usetex = True)
num = [-1.13, 0.0269047619047619]
den = [443, 11.547619047619, 0.0238095238095238]
G = tf(num,den)
rlist, klistr = rlocus(G, plot = False)
realPolo1 = []
realPolo2 = []
imagPolo1 = []
imagPolo2 = []
for i in range(len(rlist)):
    realPolo1.append(np.real(rlist[i][0]))
    realPolo2.append(np.real(rlist[i][1]))
    imagPolo1.append(np.imag(rlist[i][0]))
    imagPolo2.append(np.imag(rlist[i][1]))

plt.figure(figsize=(2560/96, 1080/96))    
plt.plot(realPolo1, imagPolo1, color = 'tab:orange', linewidth = 3)
plt.plot(realPolo2, imagPolo2, color = 'tab:blue', linewidth = 3)
plt.plot(realPolo1[0], imagPolo1[0], marker = 'x', markersize = 12, color = 'tab:orange')
plt.plot(realPolo2[0], imagPolo2[0], marker = 'x', markersize = 12, color = 'tab:blue')
plt.plot(realPolo1[-1], imagPolo1[-1], marker = 'o', markersize = 8, color = 'tab:orange')
plt.plot(-0.00833, 0.0144, 'D', color = 'crimson', markersize = 6)
plt.plot(-0.00833, -0.0144, 'D', color = 'crimson', markersize = 6)
plt.xlim([-0.05, 0.12])
plt.xlabel('Eixo Real', fontsize = 22)
plt.ylabel('Eixo imaginario (j)', fontsize = 22)
plt.title('Root locus', fontsize = 24)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
bbox_props = dict(boxstyle="square,pad=0.3", fc="cornsilk", ec="black", lw=2)
plt.annotate(r'Polo = $-0.00833 + j0.0144$ \\ $K_p$ = $3{,}68$  \\ $\zeta$ = $0,5$', xy=(-0.006, 0.011), xycoords='data', bbox = bbox_props, fontsize = 20)
plt.annotate(r'Polo = $-0.00833 - j0.0144$ \\ $K_p$ = $3{,}68$ \\ $\zeta$ = $0,5$', xy=(-0.006, -0.007), xycoords='data', bbox = bbox_props, fontsize = 20)
plt.grid()
plt.savefig('ControleProporcionalRootlocus.png', bbox_inches = 'tight')
plt.show()