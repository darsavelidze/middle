f = open("10_4322.txt", encoding="cp1251")
s = ''.join(f.readlines())
count = 0
for word in s.split():
    if all(k not in word for k in 'аоАО') and any(k in word for k in 'Вв'):
        count += 1
        print(word)
print(count)
