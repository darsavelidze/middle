f = open('26_25363.txt')
N = int(f.readline())
data = []
k = 1
for line in f:
    wait, active = [int(x) for x in line.split()]
    if wait < active:
        data.append([wait, 'wait', k])
    else:
        data.append([active, 'active', k])
    k += 1

data = sorted(data)

front = []
back = []
for x in data:
    time, cat, n = x
    if cat == 'active':
        back.append(x)
    else:
        front.append(x)

print(data[-1][-1])
print(len(back) - 1)
