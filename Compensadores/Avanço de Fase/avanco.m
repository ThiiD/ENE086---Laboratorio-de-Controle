clc, clear all

G = tf([-1.13 0.0269],[443 11.55 0.0238])
Gint = tf([0.00145],[1 0])
FTRD = G*Gint

alpha = .1
z = 0.0035
p = 0.0238
Gc = tf([1 z],[1 p])

FTMAc = Gc*Gint*G

figure(1)
rlocus(FTRD)
figure(2)
rlocus(FTMAc)
%gain = tf([320],[1])
%FTMF = gain*FTMAc
%figure(4)
%pzmap(FTMF)
%FTMF = feedback(FTMF, 1)
%figure(5)
%step(FTMF)
figure(3)
bode(FTRD)
grid()

[Num,Den] = tfdata(FTMAc,'v');
syms s
sys_syms=poly2sym(Num,s)/poly2sym(Den,s);
lim = limit(s*sys_syms,s,0)


%z = 0.0035

