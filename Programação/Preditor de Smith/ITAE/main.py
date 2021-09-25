# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 02:08:59 2021

@author: Thiago Saber
"""

# ----------- Parametros Planta --------
K = 1.13
tau = 443
theta = 84

# --------- Parametros ITAE ------------
A = 0.965
B = -0.850
C = 0.796
D = -0.147
E = 0.308
F = 0.929

# ----------- Formula Parametros ------

Kp = 1/K * (A * (theta/tau)**B)
Ti = tau / (C + D * (theta/tau))
Td = tau * (E * (theta/tau)**F)

# --------------------------------------
Ki = Kp/Ti
Kd = Kp*Td