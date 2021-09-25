import matplotlib.pyplot as plt
import numpy as np
from control.matlab import *

G = tf([-1.13, 0.0269], [443, 11.55, 0.0238])
Gint = tf([0.00145], [1, 0])

GcBode = tf([11*9615.38, 11*1], [150648.96615, 1])
GcRLocus = tf([0.975*1, 0.975*0.0001], [1, 0.00001])
FTMABode = G*Gint*GcBode
FTMARLocus = G*Gint*GcRLocus

respBode = feedback(FTMABode, 1)
respRLocus = feedback(FTMARLocus, 1)
degrau = [[-2500, 0, 0.0000001, 65100], [0,0,1,1]]

yB, tB = step(respBode, np.linspace(0, 65100, 65100))
yR, tR = step(respRLocus, np.linspace(0, 65100, 65100))
plt.figure(figsize=(2560/96, 1080/96))
plt.plot(degrau[0], degrau[1], color = 'tab:orange', linewidth = 3, label = 'Referência')
plt.plot(tR, yR, linewidth = 3, color = 'tab:blue', label = 'Comp. RLocus')
plt.plot(tB, yB, linewidth = 3, color = 'tab:green', label = 'Comp. Bode')
plt.xlim([-2500, 65100])
plt.xticks(fontsize=22)
plt.yticks(fontsize = 22)
plt.xlabel('Tempo (s)', fontsize = 22)
plt.ylabel('Amplitude (°C)', fontsize = 22)
plt.title('Resposta ao degrau', fontsize = 22)
plt.legend(loc = 'lower right', fontsize = 22)
plt.grid()
plt.savefig('RespostaCompensadorAtrasoDegrau.png', bbox_inches='tight')
plt.show()