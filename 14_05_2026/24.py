s = 'aaaa11bbbbbb11ccccc1ddddd1eeeee1f1g1hhhhhh1'
max_len = float('-inf')
left = 0
count_1 = 0
for right in range(len(s)):
    if s[right] == '1':
        count_1 += 1

    while count_1 > 3:
        if s[left] == '1':
            count_1 -= 1
        left += 1

    if count_1 == 3:
        cur_len = right - left + 1
        if cur_len > max_len:
            max_len = cur_len

print(max_len)
