G = tf([-1.1, 0.0269], [443 11.55 0.0238])
Gint = tf([0.00145], [1 0])
Kc = 12
T = 95.47993082771802
alpha = 0.044
Gc = tf([Kc*T Kc], [(alpha*T) 1])
zrl = 0.0035
prl = 0.0238
Kcrl = 32.7
Gcrl = tf([Kcrl, zrl*Kcrl], [1, prl])
figure()
GGcrl = tf([1],[1 0]) * Gcrl *  Gint * G
GGc = tf([1],[1,0]) * Gc *  Gint * G
FTrl = feedback(GGcrl, 1)
step(FTrl, linspace(0,5300,5300))
FT = feedback(GGc, 1)
step(FT, linspace(0,5300,5300))
