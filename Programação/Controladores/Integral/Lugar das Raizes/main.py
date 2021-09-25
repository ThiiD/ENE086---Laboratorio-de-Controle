from control import *
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import numpy as np
import matplotlib as mpl

mpl.rc('text', usetex = True)
num = [-1.13, 0.0269047619047619]
den = [443, 11.547619047619, 0.0238095238095238]
G = tf(num, den)
Gc = tf([1], [1, 0])
FTMA = Gc*G
rlist, klist = rlocus(FTMA, plot = False)
realPolo1 = []
realPolo2 = []
realPolo3 = []
imagPolo1 = []
imagPolo2 = []
imagPolo3 = []
for i in range(len(rlist)):
    realPolo1.append(np.real(rlist[i][0]))
    realPolo2.append(np.real(rlist[i][1]))
    realPolo3.append(np.real(rlist[i][2]))
    imagPolo1.append(np.imag(rlist[i][0]))
    imagPolo2.append(np.imag(rlist[i][1]))
    imagPolo3.append(np.imag(rlist[i][2]))
plt.figure(figsize = (2560/96, 1080/96))
plt.plot(realPolo1, imagPolo1, color = 'tab:green', linewidth = 3)
plt.plot(realPolo2, imagPolo2, color = 'tab:blue', linewidth = 3)
plt.plot(realPolo3, imagPolo3, color = 'tab:orange', linewidth = 3)
plt.plot(realPolo1[0], imagPolo1[0], marker = 'x', markersize = 12, color = 'tab:green')
plt.plot(realPolo2[0], imagPolo2[0], marker = 'x', markersize = 12, color = 'tab:blue')
plt.plot(realPolo3[0], imagPolo3[0], marker = 'x', markersize = 12, color = 'tab:orange')
plt.plot(realPolo2[-1], imagPolo2[-1], marker = 'o', markersize = 8, color = 'tab:blue')
plt.plot(-0.00096, 0.00165, marker = 'D', markersize = 6, color = 'crimson')
plt.plot(-0.00096, -0.00165, marker = 'D', markersize = 6, color = 'crimson')
plt.plot(-0.0242, 0, marker = 'D', markersize = 6, color = 'crimson')
plt.xlabel('Eixo Real', fontsize = 22)
plt.ylabel('Eixo Imaginario (j)', fontsize = 22)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.title("Lugar das Raizes", fontsize = 24)
bbox_props = dict(boxstyle="square,pad=0.3", fc="cornsilk", ec="black", lw=2)
plt.annotate(r'Polo = $0,00096 + j0,00165$ \\ $K_i$ = $0{,}00145$  \\ $\zeta$ = $0,5$', xy=(-0.0235, 0.0055), xycoords='data', bbox = bbox_props, fontsize = 20)
plt.annotate(r'Polo = $-0,00096 - j0,00165$ \\ $K_i$ = $0{,}00145$ \\ $\zeta$ = $0,5$', xy=(-0.0248, -0.0035), xycoords='data', bbox = bbox_props, fontsize = 20)
plt.xlim([-0.058, 0.07])
plt.ylim([-.02, .02])
plt.grid()
plt.savefig('rootlocusIntegral', bbox_inches='tight')
plt.show()