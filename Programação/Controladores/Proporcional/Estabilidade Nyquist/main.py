from control.freqplot import nyquist_plot
from control.matlab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv('Nyquist.csv', sep=',')
num = [-1.13, 0.0269047619047619]
den = [443, 11.547619047619, 0.0238095238095238]
plt.figure(figsize=(2560/96, 1080/96))
plt.plot(dados['real'], dados['imag'], linewidth =3, color = 'tab:blue', zorder = 2.7)
plt.plot(dados['real'], -1*dados['imag'], linewidth = 3, color = 'tab:blue', zorder = 2.7)
plt.plot(-1, 0, marker = '+', markersize = 22, color = 'tab:red', zorder = 2.7)
plt.arrow(x = -.5, y = 0, dx = -.465, dy = 0, width = 0.007, color = 'black', zorder = 2.6)
plt.arrow(x = -.5, y = 0, dx = .37, dy = 0, width = 0.007, color = 'black', zorder = 2.6)
plt.annotate(text = 'd = 0,9021443986', xy = (-0.72, 0.025), fontsize = 22)
plt.xlim([-1.2, 1.5])
plt.ylim([-.8, .8])
plt.title('Diagrama de Nyquist', fontsize = 24)
plt.xlabel('Eixo real', fontsize = 22)
plt.ylabel('Eixo imaginario (j)', fontsize = 22)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.grid()
plt.savefig('nyquistProporcional', bbox_inches = 'tight')
plt.show()