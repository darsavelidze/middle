m = 10 ** 10

for x in range(1, 2031):
    r = 6 ** 2030 + 6 ** 100 - x
    count = 0
    while r > 0:
        if r % 6 == 0:
            count += 1
        r //= 6

    if count < m:
        m = count

print(m)
