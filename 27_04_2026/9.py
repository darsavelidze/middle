f = open('9_28961.csv')
k = 0
for line in f:
    s = [int(x) for x in line.split('{')]
    q = [s.count(x) for x in s]
    if q.count(2) == 2 and q.count(1) == 3:
        if s.count(min(s)) == 1:
            k += 1

print(k)