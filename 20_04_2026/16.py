cache_g = [None] * 23000

def g(n):
    if cache_g[n] is not None:
        return cache_g[n]
    if n >= 22560:
        return n / 23 + 33
    else:
        return g(n + 11) - 4

def f(n):
    if n >= 21:
        return f(n - 8) + 1095
    else:
        return 10 * (g(n - 7) - 36)


for i in range(22560, 1, -1):
    cache_g[i] = g(i)

print(f(548))