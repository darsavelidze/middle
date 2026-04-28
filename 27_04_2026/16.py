cache = [None] * 25000

def f(n):
    if n >= 18:
        return f(n - 4) + 959
    else:
        return 9 * (g(n - 12) - 39)


def g(n):
    if cache[n] is not None:
        return cache[n]
    if n >= 24188:
        return n / 30 + 37
    else:
        return g(n + 6) - 3

for i in range(24188, 1, -1):
    cache[i] = g(i)

print(f(440))