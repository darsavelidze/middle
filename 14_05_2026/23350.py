x = 77 * 81**2031 + 23 * 729**1037 - 7 * 9**3023

count = 0
while x > 0:
    if  (x % 81) % 4 == 0:
        count += 1
    x = x // 81

print(count)
