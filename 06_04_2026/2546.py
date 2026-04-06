r = 4 ** 36 + 3 * 4 ** 20 + 4 ** 15 + 2 * 4 ** 7 + 49

s = set()

while r > 0:
    s.add(r % 16)
    r //= 16

print(s, len(s))