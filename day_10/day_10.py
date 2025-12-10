from collections import deque
from pulp import *

with open("input.txt") as file:
    lines = [line.strip() for line in file]

part_1 = 0
part_2 = 0

for line in lines:
    parts = line.split(' ')
    diagram = parts[0]
    buttons = [[int(x) for x in button.strip('()').split(",")] for button in parts[1:-1]]

    end_state = [x == '#' for x in diagram[1:-1]]
    start = [False] * len(end_state)

    q = deque(((start, 0),))
    visited = set(str(start))

    while q:
        current_state, depth = q.popleft()
        if current_state == end_state:
            part_1 += depth
            break
        for button in buttons:
            new_state = current_state[:]
            for press in button:
                new_state[press] = not new_state[press]

            to_add = new_state
            if str(to_add) not in visited:
                visited.add(str(to_add))
                q.append((to_add, depth+1))

for line in lines:
    parts = line.split(" ")
    buttons = parts[1:-1]
    end_state = [int(x) for x in parts[-1].strip('{}').split(',')]

    add_values = []
    for button in buttons:
        indexes = [int(x) for x in button.strip('()').split(',')]
        change = [1 if i in indexes else 0 for i in range(len(end_state))]
        add_values.append(change)

    prob = LpProblem('day_10', LpMinimize)

    options = len(add_values)
    press_counts = [
        LpVariable(f"b{i}", lowBound=0, cat="Integer") for i in range(options)
    ]

    prob += lpSum(press_counts)

    for pos in range(len(end_state)):
        prob += (
            lpSum(press_counts[btn] * add_values[btn][pos] for btn in range(options))
            == end_state[pos],
            f"p{pos}",
        )

    prob.solve(PULP_CBC_CMD(msg=0))
    part_2 += sum([int(v.varValue) for v in press_counts])

print(part_1)
print(part_2)