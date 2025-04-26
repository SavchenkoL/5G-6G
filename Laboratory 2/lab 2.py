import math
import matplotlib.pyplot as plt
import numpy as np

fc = 28 * 10**9
pt = 2
hb = 10
hu = 1.5
GB = 10
GU = 2
NO = -174
R = 124
S_A = 1.44 * 10**6
C_required = 20 * 10**6
F = 10 ** (NO/10)
z=2.1

def path_loss(R):
    y = math.sqrt(R**2 +(hu-hb)**2)
    L = 32.4 + 10*z*math.log10(y)+20*math.log10(fc)
    return L


def shannon (B_, R):
    PL = path_loss(R)
    Pr = pt + GB + GU - PL
    SNR = Pr - (NO + 10*math.log10(B_) + 10 * math.log10(F))
    C = B_ * math.log2(1 + 10**(SNR/10))
    return C

print(f'спектральная эффективность: {shannon(1,R/2)}бит/с/Гц')
print(f'размер запрашиваемых ресурсов на расстоянии R/2: {shannon(1,R/2)/C_required*S_A}ресурсные блоки')

print(f'размер запрашиваемых ресурсов на расстоянии R/10: {shannon(1,R/10)/C_required*S_A}ресурсные блоки')
print(f'размер запрашиваемых ресурсов на расстоянии R: {shannon(1,R)/C_required*S_A}ресурсные блоки')

S_A_R10 = shannon(1,R/10)/C_required*S_A
S_A_R2 = shannon(1,R/2)/C_required*S_A
S_A_R = shannon(1,R)/C_required*S_A

l1 = []
l2 = []
l3 = []
for B in range(20, 401, 20):
    b = B * 10**6
    l1.append(shannon(b, R/10)/b/C_required*S_A_R10*S_A)
    l2.append(shannon(b, R/2)/b/C_required*S_A_R2*S_A)
    l3.append(shannon(b, R)/b/C_required*S_A_R*S_A)

plt.plot(np.linspace(20,400,20), l1, label='R/10')
plt.plot(np.linspace(20,400,20), l1, label='R/2')
plt.plot(np.linspace(20,400,20), l1, label='R')
plt.legend()
plt.xlabel('B,МГц')
plt.ylabel('Ау,шт.')
plt.show()