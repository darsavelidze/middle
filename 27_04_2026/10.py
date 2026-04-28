f = open('10.txt', encoding='utf-8').readlines()
s = ''.join(f)
s = s.replace('.', '')
s = s.replace(',', '')
s = [x.strip() for x in s.split()]
k = 0
for x in s:
    if ('его' in x or 'Его' in x) and len(x) > 3:
        k += 1

print(k)
