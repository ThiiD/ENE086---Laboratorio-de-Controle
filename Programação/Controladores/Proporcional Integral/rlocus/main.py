# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 01:18:29 2021

@author: Thiago Saber
"""

from control.matlab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rc('text', usetex = True)
G = tf([-0.00255, 6.0714285714285715e-05],[1, 0.023809523809523808, 0])
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
    
plt.figure(figsize = (2560/96, 1080/96))
plt.plot(realPolo1, imagPolo1, color = 'tab:orange', linewidth = 3)
plt.plot(realPolo2, imagPolo2, color = 'tab:blue', linewidth = 3)
plt.plot(realPolo1[0], imagPolo1[0], marker = 'x', markersize = 12, color = 'tab:orange')
plt.plot(realPolo2[0], imagPolo2[0], marker = 'x', markersize = 12, color = 'tab:blue')
plt.plot(realPolo1[-1], imagPolo1[-1], marker = 'o', markersize = 8, color = 'tab:orange')
plt.plot(-0.00736, 0.0127, marker = 'D', markersize = 6, color = 'crimson')
plt.plot(-0.00736, -0.0127, marker = 'D', markersize = 6, color = 'crimson')
plt.xlabel('Eixo Real', fontsize = 22)
plt.ylabel('Eixo Imaginario (j)', fontsize = 22)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.title("Lugar das Raizes", fontsize = 24)
bbox_props = dict(boxstyle="square,pad=0.3", fc="cornsilk", ec="black", lw=2)
plt.annotate(r'Polo = $-0,00736 + j0,0127$ \\ $K_p$ = $3{,}56$  \\ $\zeta$ = $0,5$', xy=(-0.006, 0.009), xycoords='data', bbox = bbox_props, fontsize = 20)
plt.annotate(r'Polo = $-0,00736 - j0,0127$ \\ $K_p$ = $3{,}56$ \\ $\zeta$ = $0,5$', xy=(-0.006, -0.005), xycoords='data', bbox = bbox_props, fontsize = 20)
plt.xlim([-0.04, 0.14])
plt.ylim([-.04, .04])
plt.grid()
plt.savefig('rootlocusProporcionalntegral', bbox_inches='tight')
plt.show()