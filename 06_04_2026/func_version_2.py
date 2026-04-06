x = 3256723123

k = 0

while x > 0:
    if x % 400 > 35:
        k += 1
    x //= 400
print(k)
