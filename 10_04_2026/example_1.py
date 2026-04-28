s = 'EABEEABEAB'
sub = 'EAB'
count = 0
max_count = 0
for ch in s:
    if sub[count % 3] == ch:
        count += 1
        if count > max_count:
            max_count = count
    elif ch == 'E':
        count = 1
    else:
        count = 0
print(max_count)
