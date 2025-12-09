from itertools import combinations

with open("input.txt") as file:
    lines = [line.strip() for line in file]

part_1 = 0
part_2 = 0

def rect_area(p, q):
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) +1)

def is_red_green(p, q, point_list):
    x_min, x_max = sorted([p[0], q[0]])
    y_min, y_max = sorted([p[1], q[1]])
    for k in range(len(point_list)):
        x1, y1 = point_list[k]
        x2, y2 = point_list[(k + 1) % len(point_list)]
        if y1 == y2:
            if y_min < y1 < y_max and (min(x1, x2) <= x_min < max(x1, x2) or min(x1, x2) < x_max <= max(x1, x2)):
                return False
        elif x1 == x2:
            if x_min < x1 < x_max and (min(y1, y2) <= y_min < max(y1, y2) or min(y1, y2) < y_max <= max(y1, y2)):
                return False
        else:
            return False
    return True


points = []

for line in lines:
    x, y = map(int, line.split(','))
    points.append((x,y))

for i,j in combinations(range(len(points)), 2):
    area = rect_area(points[i],points[j])
    part_1 = max(part_1, area)

for i,j in combinations(range(len(points)), 2):
    if not is_red_green(points[i], points[j], points):
        continue
    area = rect_area(points[i],points[j])
    part_2 = max(part_2, area)

print(part_1)
print(part_2)