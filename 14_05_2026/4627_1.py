s = open('24_4627.txt').readline()
print(len(s))
left = 0
right = 0
max_count = float('-inf')
cur_count = 0
i = 0
while i < len(s) - 3:
    if s[i:i + 3] in 'PNO NPO':
        cur_count += 1
        i += 3
    else:
        cur_count = 0
        i += 1

    if cur_count > max_count:
        max_count = cur_count

print(max_count)