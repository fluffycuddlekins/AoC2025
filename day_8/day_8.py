from collections import Counter
from itertools import combinations

with open("input.txt") as file:
    lines = [line.strip() for line in file]

part_1 = 0
part_2 = 0

def d_squared(p,q):
    return (p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[2] - q[2])**2


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.junctions = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.junctions -= 1
        return True

points = []

for line in lines:
    x,y,z = map(int, line.split(','))
    points.append((x,y,z))

distances = []
for i,j in combinations(range(len(points)), 2):
    distance = d_squared(points[i], points[j])
    distances.append((distance, i, j))

distances.sort()

dsu = DSU(len(points))

connections = 1000

for k in range(connections):
    d, i, j = distances[k]
    dsu.union(i,j)

roots = [dsu.find(i) for i in range(len(points))]
counts = Counter(roots)
sizes = sorted(counts.values(), reverse=True)

top3 = sizes[:3]
part_1 += (top3[0] * top3[1] * top3[2])

dsu2 = DSU(len(points))

for d, i, j in distances:
    connected = dsu2.union(i,j)
    if not connected:
        continue
    if dsu2.junctions == 1:
        part_2 += (points[i][0] * points[j][0])

print(part_1)
print(part_2)