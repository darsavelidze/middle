from math import dist


def find_center(cluster):
    min_sum = 10 ** 10
    center = None
    for p1 in cluster:
        cur_sum = 0
        for p2 in cluster:
            cur_sum += dist(p1, p2)
        if cur_sum < min_sum:
            min_sum = cur_sum
            center = p1
    return center


f = open('27_B_28978.txt')
data = []
for line in f:
    point = [float(x) for x in line.replace(',', '.').split()]
    data.append(point)

cluster_1 = []
cluster_2 = []
cluster_3 = []
for point in data:
    x, y = point
    if y > 22:
        cluster_1.append(point)
    elif x > 24:
        cluster_2.append(point)
    else:
        cluster_3.append(point)

xc, yc = find_center(cluster_3)
k = 0
for p in cluster_3:
    x, y = p
    if abs(x - xc) <= 1 and abs(y - yc) <= 1:
        k += 1

print(k)
center_1 = find_center(cluster_1)
center_2 = find_center(cluster_2)
print(abs(center_1[1] - center_2[1]) * 10000)
