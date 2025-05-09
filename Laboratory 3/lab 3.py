import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def LinToLog(a):
    return 10*np.log10(a)

def LogToLin(a):
    return np.power(10,a/10)

#def shannon(snr, bandwidth):
#    return bandwidth*np.log2(1 + LogToLin(snr))

LogToLin(10*np.log10(2/0.001))

#начальные значения
fc = 28 * 10**9 # Частота
pt = 2/0.001 # Излучаемая мощность
gb = 10 # Усиление антенны БС
gu = 2 # Усиление антенны АУ
n0 = -174 # Спектральная плотность шума
z = 2.1 # константа распространения
b = 400 * 10**6 # Полоса пропускания

r = 124

block_size = 1.44 * 10**6 # размер первичного ресурсного блока

C = pt*LogToLin(gb)*LogToLin(gu)/(np.power(10,2*np.log10(fc)+3.24)*LogToLin(n0)*b)


def snr_lin(y):
    return C * np.power(y, -z)


def Fx(x):
    if x > 0 and x < r:
        return x * x / r ** 2
    elif x <= 0:
        return 0
    elif x >= r:
        return 1


def Fs(s):
    return 1 - Fx(np.power(C / s, 1 / z))


SNR = np.array([-9.478, -6.658, -4.098, -1.798, 0.399, 2.424, 4.489, 6.367, 8.456, 10.266,
                12.218, 14.122, 15.849, 17.786, 19.809])

fs = []

for i in SNR:
    if len(fs) == 0:
        fs.append(Fs(LogToLin(i)))
        continue
    fs.append(Fs(LogToLin(i)) - sum(fs))

for i, j in zip(SNR, fs):
    print(i, "-->", j)

s5=5000000
s10=10000000
s20=20000000

SE = [
    0.15237, 0.2344, 0.377, 0.6016, 0.877, 1.1758, 1.4766, 1.9141,
    2.4063, 2.7305, 3.3223, 3.9023, 4.5234, 5.1152, 5.5547
]



rb5 = []
rb10 = []
rb20 = []
for s in SE:
    rb5.append(s5/(s*block_size))
    rb10.append(s10/(s*block_size))
    rb20.append(s20/(s*block_size))

print('для скорости 5 мбит/с')
for i,j in zip(rb5, fs):
    print(i,"-->",j)

print('для скорости 10 мбит/с')
for i,j in zip(rb10, fs):
    print(i,"-->",j)

print('для скорости 20 мбит/с')
for i,j in zip(rb20, fs):
    print(i,"-->",j)

