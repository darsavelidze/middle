max_z = -10 ** 10
min_x = -1
for x in range(1, 27001):
    r = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x
    cur_z = 0
    while r > 0:
        if r % 27 == 0:
            cur_z += 1
        r //= 27
    if cur_z > max_z:
        max_z = cur_z
        min_x = x

print(max_z, min_x)

