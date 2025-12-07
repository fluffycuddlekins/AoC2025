from collections import defaultdict

with open("input.txt") as file:
    lines = [line.strip() for line in file]

part_1 = 0
part_2 = 0

grid = []
for line in lines:
    grid.append(line)

indexes = set()
start_index = grid[0].index("S")
indexes.add(start_index)

for line in grid:
    temp_set = indexes.copy()
    for i in temp_set:
        if line[i] == '^':
            part_1 += 1
            indexes.discard(i)
            indexes.add(max(i-1,0))
            indexes.add(min(i+1, len(line)-1))

paths = {start_index: 1}

#part 2

for line in grid:
    new_path = defaultdict(int)
    for i, count in paths.items():
        if line[i] == '^':
            #part_1 += 1 could have been here instead of doing everything above
            left = max(i-1,0)
            right = min(i+1, len(line)-1)
            new_path[left] += count
            new_path[right] += count
        else:
            new_path[i] += count
    paths = new_path

part_2 = sum(paths.values())

print(part_1)
print(part_2)