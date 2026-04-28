from math import dist

f = open('27_A_17882.txt')

cluster_1 = []
cluster_2 = []

for line in f:
    point = [float(x) for x in line.split()]
    x, y = point
    if y < 3:
        cluster_1.append(point)
    else:
        cluster_2.append(point)

min_sum = 100000000000
center = None

for p1 in cluster_1:
    cur_sum = 0
    for p2 in cluster_1:
        cur_sum += dist(p1, p2)

    if cur_sum < min_sum:
        min_sum = cur_sum
        center = p1

print(min_sum)

print((-0.530720837096502 + 2.67836329019008)/2*10000)