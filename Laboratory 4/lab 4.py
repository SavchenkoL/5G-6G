import math
fc = 2.4 * 10**9 # Частота (Гц)
Pt = 10 # Излучаемая мощность (дБм)
B = 20 * 10**6 # Полоса пропускания (Гц)
N0 = -174 # Спектральная плотность шума (дБм/Гц)
F = 10**(N0/10) # Фактор шума, определяемый как 10^(N0/10)

def FSPL(x):
    return 32.4 + 20*math.log10(x) + 20*math.log10(fc)

def coverage_radius():
    R = 1
    while True:
        L = FSPL(R)
        SNR = Pt - L - (N0 + 10*math.log10(B) + 10*math.log10(F))
        if SNR < 18:
            return R-1
        R += 1

R = coverage_radius()
print(f"Максимальный радиус покрытия: {R} м")
Lam = math.pi*R**2*0.8/100
print(f"Интенсивность запросов: {Lam} ")
mu = 1/0.5
ro = Lam / mu
print(f"Интенсивность нагрузки: {ro} ")
