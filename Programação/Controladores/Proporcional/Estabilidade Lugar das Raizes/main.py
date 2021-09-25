from control.matlab import *
from matplotlib.transforms import Bbox
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rc('text', usetex = True)
num = [-1.13, 0.0269047619047619]
den = [443, 11.547619047619, 0.0238095238095238]
G = tf(num,den)
rlist, klist = rlocus(G, plot = False, print_gain= True)
realPolo1 = []
imagPolo1 = []
realPolo2 = []
imagPolo2 = []
for i in range(len(rlist)):
    realPolo1.append(np.real(rlist[i][0]))
    imagPolo1.append(np.imag(rlist[i][0]))
    realPolo2.append(np.real(rlist[i][1]))
    imagPolo2.append(np.imag(rlist[i][1]))

fig = plt.figure(figsize=(2560/96, 1080/96))
plt.plot(realPolo1, imagPolo1, linewidth = 3)
plt.plot(realPolo2, imagPolo2, linewidth = 3)
plt.plot(realPolo1[0], imagPolo1[0], marker = 'x', markersize = 24, color = 'tab:blue')
plt.plot(realPolo2[0], imagPolo2[0], marker = 'x', markersize = 24, color = 'tab:orange')
plt.plot(realPolo1[-1], imagPolo1[-1], marker = '.', markersize = 24, color = 'tab:blue')
plt.plot(0, 0.026, marker = 'D', markersize = 10, color = 'black')
plt.plot(0, -0.026, marker = 'D', markersize = 10, color = 'black')
bbox_props = dict(boxstyle="square,pad=0.3", fc="cornsilk", ec="black", lw=2)
plt.annotate(r'Polo = $0 + j0,026$ \\ Ganho = $10{,}22$ ', xy=(0.002, 0.023), xycoords='data', bbox = bbox_props, fontsize = 20)
plt.annotate(r'Polo = $0 - j0,026$ \\ Ganho = $10{,}22$ ', xy=(0.002, -0.021), xycoords='data', bbox = bbox_props, fontsize = 20)
plt.xlim([-.03, .12])
plt.title('Root Locus', fontsize = 24)
plt.yticks(fontsize = 22)
plt.xticks(fontsize = 22)
plt.xlabel('Eixo real', fontsize = 22)
plt.ylabel('Eixo Imaginario (j)', fontsize = 22)
plt.grid()
plt.savefig("RootlocusEstabilidadeProporcional.png",bbox_inches='tight')
plt.show()
