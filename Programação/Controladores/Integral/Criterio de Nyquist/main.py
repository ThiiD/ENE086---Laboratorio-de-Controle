# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 19:09:19 2021

@author: Thiago Saber
"""

from control import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

real = pd.read_csv('real.csv', sep=',')
imag = pd.read_csv('imag.csv', sep=',')

plt.figure(figsize=(2560/96, 1080/96))
plt.plot(real['real'],imag['imag'], color = 'tab:blue', linewidth = 3)
plt.plot(real['real'],-1*imag['imag'], color = 'tab:blue', linewidth = 3)
plt.plot(-1, 0, marker = '+', markersize = 22, color = 'tab:red', zorder = 2.7)
plt.arrow(x = -44.9, y = 0, dx = -44.9, dy = 0, width = 0.007, color = 'black', zorder = 2.5, length_includes_head = True, head_width = .4)
plt.arrow(x = -44.9, y = 0, dx = 44.9, dy = 0, width = 0.007, color = 'black', zorder = 2.5, length_includes_head = True, head_width = .4)
plt.annotate(text = 'd = 89,8', xy = (-50, 0.25), fontsize = 22)
plt.xlabel('Eixo Real', fontsize = 22)
plt.ylabel('Eixo Imaginario (j)', fontsize = 22)
plt.title('Diagrama de Nyquist', fontsize = 24)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.xlim([-120, 2])
plt.ylim([-15, 15])
plt.grid()
plt.savefig('nyquistIntegral', bbox_inches = 'tight')
plt.show()
