with open("input.txt") as file:
    lines = [line.strip() for line in file]

part_1 = 0
part_2 = 0

grid = []

for line in lines:
    grid.append(list(line))

rows = len(grid)
cols = len(grid[0])

def count_neighbors(board, rowf, colf):
    total = 0
    for i in range(max(0,rowf-1), min(rows, rowf+2)):
        for j in range(max(0,colf-1), min(cols,colf+2)):
            if i == rowf and j == colf:
                continue
            if board[i][j] == "@":
                total += 1

    return total

for row in range(rows):
    for col in range(cols):
        if grid[row][col] != "@":
            continue
        neighbors = count_neighbors(grid, row, col)
        if neighbors < 4:
            part_1 += 1

grid2 = grid

loop = True

while loop:
    found_roll = False
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != "@":
                continue
            neighbors = count_neighbors(grid, row, col)
            if neighbors < 4:
                part_2 += 1
                grid[row][col] = 'x'
                found_roll = True
    if not found_roll:
        loop = False

print(part_1)
print(part_2)