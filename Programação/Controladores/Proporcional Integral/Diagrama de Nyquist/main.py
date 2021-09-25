# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 01:52:14 2021

@author: Thiago Saber
"""

from control.matlab import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_semicircle(center_x, center_y, radius, stepsize=0.1):
    """
    generates coordinates for a semicircle, centered at center_x, center_y
    """        

    x = np.arange(center_x, center_x+radius+stepsize, stepsize)
    y = np.sqrt(radius**2 - x**2)

    # since each x value has two corresponding y-values, duplicate x-axis.
    # [::-1] is required to have the correct order of elements for plt.plot. 
    x = np.concatenate([x,x[::-1]])

    # concatenate y and flipped y. 
    y = np.concatenate([y,-y[::-1]])

    return x, y + center_y



real = pd.read_csv('real.csv', sep = ',')
imag = pd.read_csv('imag.csv', sep = ',')
# real = real.T
# imag = imag.T
# # real.to_csv('real.csv', sep = ',')
# imag.to_csv('imag.csv', sep = ',')

plt.figure(figsize = (2560/96, 1080/96))
plt.plot(real['real'], imag['imag'], linewidth = 3, color = 'tab:blue')
plt.plot(real['real'], -1*imag['imag'], linewidth = 3, color = 'tab:blue')
plt.plot(-1, 0, marker = '+', markersize = 22, color = 'tab:red', zorder = 2.7)
plt.arrow(x = -0.5535, y = 0, dx = -0.4465, dy = 0, width = 0.007, color = 'black', zorder = 2.5, length_includes_head = True, head_length = .02, head_width = .08)
plt.arrow(x = -0.5535, y = 0, dx = 0.4465, dy = 0, width = 0.007, color = 'black', zorder = 2.5, length_includes_head = True, head_length = .02, head_width = .08)
plt.annotate(text = 'd = 0,893', xy = (-0.63, 0.15), fontsize = 22)
plt.xlabel('Eixo Real', fontsize = 22)
plt.ylabel('Eixo Imaginario (j)', fontsize = 22)
plt.title('Diagrama de Nyquist', fontsize = 24)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.ylim([-2.8, 2.8])
plt.xlim([-1.2, 0.2])
x,y = generate_semicircle(real['real'].iloc[0], 0, abs(imag['imag'].iloc[-0]))
plt.plot(x,y,  '--', linewidth = 3, color = 'tab:blue', )
plt.grid()
plt.savefig('nyquistProporcionalIntegral', bbox_inches = 'tight')
plt.show()