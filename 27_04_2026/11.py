from math import *

for N in range(1, 10000):
    i = ceil(log2(N))
    I = ceil(75 * i / 8)
    if I * 32768 < 3 * 1024 * 1024:
        print(N)
