import copy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from matplotlib.animation import PillowWriter

with open("input.txt") as file:
    lines = [line.strip() for line in file]

part_1 = 0
part_2 = 0

grid = []

for line in lines:
    grid.append(list(line))

rows = len(grid)
cols = len(grid[0])

def count_neighbors(board, row_index, col_index):
    total = 0
    for i in range(max(0,row_index-1), min(rows, row_index+2)):
        for j in range(max(0,col_index-1), min(cols,col_index+2)):
            if i == row_index and j == col_index:
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

grid2 = copy.deepcopy(grid)

frames = []

def board_to_array(board):
    mapping = {
        "@": 0,   # original live
        "x": 1,   # converted
        ".": 2    # empty / other
    }
    return np.array([[mapping.get(c, 0) for c in row1] for row1 in board])

while True:
    arr = board_to_array(grid2)
    frames.append(arr.copy())

    found_roll = False
    for row in range(rows):
        for col in range(cols):
            if grid2[row][col] != "@":
                continue
            neighbors = count_neighbors(grid2, row, col)
            if neighbors < 4:
                part_2 += 1
                grid2[row][col] = 'x'
                found_roll = True
    if not found_roll:
        break

fig, ax = plt.subplots()
im = ax.imshow(arr, cmap="magma")
ax.axis("off")

frame_text = fig.text(
    0.5, 0.95, "Frame 0",
    ha="center", va="top",
    fontsize=14
)

def update(i):
    im.set_data(frames[i])
    frame_text.set_text(f"Frame {i+1}")
    return im, frame_text

ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=250,blit=False)
ani.save("grid_evolution.gif", writer=PillowWriter(fps=2))

plt.show()

print(part_1)
print(part_2)