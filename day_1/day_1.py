with open("day_1_input.txt") as file:
    lines = [line.strip() for line in file]

dial = 50
zero_part1 = 0
zero_part2 = 0

for line in lines:
    direction = line[0]
    k = int(line[1:])

    if direction == 'R':
        hits = (dial + k) // 100
        dial = (dial + k) % 100

    else:
        q, r = divmod(k, 100)
        if dial == 0:
            hits = q
        else:
            hits = q + (1 if r >= dial else 0)
        dial = (dial - k) % 100

    zero_part2 += hits

    if dial == 0:
        zero_part1 += 1

print(zero_part1)
print(zero_part2)



