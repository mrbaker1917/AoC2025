import math
from collections import defaultdict
data = []

with open("day8_data.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

data = [l.split(",") for l in data]

data = [[int(n) for n in l] for l in data]
data = [(l[0], l[1], l[2]) for l in data]

def closeness(p1, p2):
    return round(math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2), 2)

D = []
for i, (x1, y1,z1) in enumerate(data):
    for j, (x2, y2, z2) in enumerate(data):
        distance = closeness((x1,y1,z1), (x2,y2,z2))
        if i>j:
            D.append((distance, i, j))

uf = {i: i for i in range(len(data))}

def find(x):
    if x == uf[x]:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def mix(x, y):
    uf[find(x)] = find(y)

connections = 0
D = sorted(D)
for distance, i, j in D[:1000]:
    if find(i) != find(j):
        connections += 1
        if connections == len(data) - 1:
            print(data[i][0]*data[j][0])
        mix(i,j)

sz = defaultdict(int)

for x in range(len(data)):
    sz[find(x)] += 1
s = sorted(sz.values())
print(s[-1]*s[-2]*s[-3])