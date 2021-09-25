K = 1.13
tau = 443
theta = 84

Kp = 1.2 * (tau / (K * theta))
Ti = 2 * theta
Td = .5 * theta

print(f'Kp = {Kp}\n')
print(f'Ti = {Ti}\n')
print(f'Td = {Td}')

print('-----------------')
print(f'Kp = {Kp}')
print(f'Ki = {Kp/Ti}')
print(f'Kd = {Kp*Td}')