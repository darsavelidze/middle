from math import dist

f = open('27_A_28978.txt')
data = []
for line in f:
    point = [float(x) for x in line.replace(',', '.').split()]
    data.append(point)


def dbscan(points, epsilon):
    clusters = []
    while points:
        cluster = [points.pop(0)]

        for core in cluster:
            for p in points:
                if dist(core, p) < epsilon:
                    cluster.append(p)
                    points.remove(p)

        clusters.append(cluster)
    return clusters

def find_center(cluster):
    dists = []
    for p1 in cluster:
        cur_sum = 0
        for p2 in cluster:
            cur_sum += dist(p1, p2)
        dists.append([cur_sum, p1])
    return min(dists)



cluster_1, cluster_2 = dbscan(data, 0.9)
count = 0
cluster_1_x = 6.080725
for p in cluster_1:
    if p[0] > cluster_1_x:
        count += 1

print(count)
print(dist([6.080725, 8.302242], [8.760804, 20.890117]) * 10000)