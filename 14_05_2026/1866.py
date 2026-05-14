s = open('24_1866.txt').readline()

left = 0
max_len = float('-inf')
for right in range(1, len(s)):
    if s[right] + s[right - 1] in 'da ad':
        left = right

    cur_len = right - left + 1
    if cur_len > max_len:
        max_len = cur_len

print(max_len)
