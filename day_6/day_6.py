import re

with open("input.txt") as file:
    lines = [line.strip() for line in file]

part_1 = 0
part_2 = 0

num_grid = []
opp_list = []

for line in lines:
    if re.search(r"\d", line):
        num_grid.append(list(map(int, re.findall(r"\d+", line))))
    else:
        clean = re.sub(r"\s+", "", line)
        opp_list=list(clean)

rows = len(num_grid)
cols = len(num_grid[0])

for c in range(cols):
    if opp_list[c] == '*':
        val = 1
        for r in range(rows):
            val *= num_grid[r][c]
    elif opp_list[c] == '+':
        val = 0
        for r in range(rows):
            val += num_grid[r][c]
    part_1 += val

#part 2

with open("input.txt") as file:
    p2lines = [line.rstrip("\n") for line in file]

width = max(len(line) for line in p2lines)
p2grid = [list(line.ljust(width)) for line in p2lines]

p2rows = len(p2grid)

column_nums = []
for c in range(width):
    digits = ''.join(p2grid[r][c] for r in range(p2rows-1) if p2grid[r][c].isdigit())
    column_nums.append(int(digits) if digits != '' else None)

grouped_nums = []
line = []

for num in column_nums:
    if num is not None:
        line.append(num)
    else:
        grouped_nums.append(line)
        line = []
grouped_nums.append(line)

for i in range(len(opp_list)):
    nums = grouped_nums[i]
    if opp_list[i] == '*':
        val = 1
        for n in nums:
            val *= n
    elif opp_list[i] == '+':
        val = 0
        for n in nums:
            val += n
    part_2 += val

print(part_1)
print(part_2)