import math
import random
import matplotlib.pyplot as plt

fc = 28 * 10**9
pt = 2
hb = 10
hu = 1.5
GB = 10
GU = 2
NO = -174
sigma2 = 3
B = 400 * 10**6

C = 3 * 10**8
lambda_ = C/fc
F = 10 ** (NO/10)
z=2.1

def path_loss(R):
    y = math.sqrt(R**2 +(hu-hb)**2)
    L = 32.4 + 10*z*math.log10(y)+20*math.log10(fc)
    return L

def coverage_radius():
    R = 1
    while True:
        PL = path_loss(R)
        Pr = pt + GB + GU - PL
        SNR = Pr - (NO +10*math.log10(B)+10*math.log10(F))
        if SNR < -9.4:
            return R-1
        R += 1

def shannon (R,B_):
    PL = path_loss(R)
    Pr = pt + GB + GU - PL
    SNR = Pr - (NO + 10*math.log10(B_) + 10 * math.log10(F))
    C = B_ * math.log2(1 + 10**(SNR/10))
    return C

B_ = 10 * 10**6
R = coverage_radius()
print(f"max radius covering: {R:.2f} m")

R_10=shannon(R/10,B_)
print(f"speed  over distance R/10: {R_10/10**6:.2f} mbit/c")

R_2=shannon(R/2,B_)
print(f"speed  over distance R/2: {R_2/10**6:.2f} mbit/c")

R_=shannon(R,B_)
print(f"speed  over distance R: {R_/10**6:.2f} mbit/c")

speeds = [R_10/10**6, R_2/10**6, R_/10**6]
distances = [R/10, R/2, R]

plt.plot(distances, speeds, marker = 'o')
plt.xlabel('distance')
plt.ylabel('speed')
plt.title('change in speed with increasing distance')
plt.grid(True)
plt.show()

def coverage_radius():
    R = 1
    sigma = math.sqrt(sigma2)
    threshold = -9.4
    confidence_interal = 1.96

    SNR_threshold = threshold + random.gauss(0, sigma) * confidence_interal

    while True:
        PL = path_loss(R)
        Pr = pt + GB + GU - PL
        SNR = Pr - (NO + 10 * math.log10(B) + 10 * math.log10(F))

        if SNR < SNR_threshold:
            return R-1
        R += 1

B_ = 10 * 10**6
R = coverage_radius()
print(f"max radius covering: {R:.2f} m")

R_10=shannon(R/10,B_)
print(f"speed  over distance R/10: {R_10/10**6:.2f} mbit/c")

R_2=shannon(R/2,B_)
print(f"speed  over distance R/2: {R_2/10**6:.2f} mbit/c")

R_=shannon(R,B_)
print(f"speed  over distance R: {R_/10**6:.2f} mbit/c")

speeds = [R_10/10**6, R_2/10**6, R_/10**6]
distances = [R/10, R/2, R]

plt.plot(distances, speeds, marker = 'o')
plt.xlabel('distance')
plt.ylabel('speed')
plt.title('change in speed with increasing distance')
plt.grid(True)
plt.show()