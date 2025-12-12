from collections import defaultdict

with open("input.txt") as file:
    lines = [line.strip() for line in file]

part_1 = 0
part_2 = 0

shapes = []
regions = []

i = 0
length = len(lines)

while i < len(lines):
    line = lines[i]
    if not line:
        i += 1
        continue

    if 'x' in line.split()[0]:
        break

    if line.endswith(':'):
        i += 1
        shape = []
        while i < len(lines):
            row = lines[i].strip()
            if not row:
                break
            shape.append(row)
            i+=1
        shapes.append(shape)
    else:
        i+=1

while i < len(lines):
    line = lines[i]
    if not line:
        i += 1
        continue
    left, right = line.split(':')
    w, h = left.split('x')
    width, height = int(w), int(h)
    counts = [int(x) for x in right.split()]
    regions.append((width, height, counts))
    i += 1

for region in regions:
    width = region[0] // 3
    height = region[1] // 3
    no_overlap = width * height
    if no_overlap >= sum(region[2]):
        part_1 += 1

print(part_1)
print(part_2)