import string

def f(n):
    alf = '0123456789' + string.ascii_uppercase[:17]
    s = ''
    while n > 0:
        s = alf[n % 27] + s
        n //= 27
    return s

m = []
for x in range(1, 27001):
    r = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x
    count_z = f(r).count('0')
    m.append([count_z, x])

print(max(m))
