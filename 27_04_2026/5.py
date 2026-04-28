def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s
m = []
for i in range(1, 100):
    N = f(i)
    if i % 3 == 0:
        N = N + N[-2:]
    else:
        r = N.count('1') + N.count('2') * 2
        N = N + f(r * 2)
    R = int(N, 3)
    if R > 350:
        m.append([R, i])

print(min(m))


