# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 17:06:04 2021

@author: Thiago Saber
"""

import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *


kp = np.linspace(0,10.22, 5000)
ki = (0.03*kp**2 - 0.284*kp - 0.27489) / (1.276*kp - 24.967) 
plt.figure(figsize = (2560/96, 1080/96))
plt.plot(kp, ki, linewidth= 3)
plt.fill_between(kp, 0, ki, color = 'tab:blue', alpha = .3)
plt.xlim([0, 10.22])
plt.ylim([0, 0.055])
plt.xlabel('$K_p$', fontsize = 22)
plt.ylabel('$K_i$ maximo', fontsize = 22)
plt.title('Relação entre $K_p$ e $K_i$', fontsize = 24)
plt.yticks(fontsize = 22)
plt.xticks([0, 2, 4, 6, 8, 10, 10.22], fontsize = 22, rotation = 45)
plt.grid()
plt.savefig('relacaokpkicontrolepi' ,bbox_inches='tight')
plt.show()