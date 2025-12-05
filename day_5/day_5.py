with open("input.txt") as file:
    lines = [line.strip() for line in file]

part_1 = 0
part_2 = 0

split_index = lines.index("")

ranges = []
ingredients = lines[split_index+1:]

for r in lines[:split_index]:
    r1, r2 = r.split('-')
    ranges.append((int(r1), int(r2)))

ranges.sort()

for i in ingredients:
    for r in ranges:
        r1, r2 = r
        if r1 <= int(i) <= r2:
            part_1 += 1
            break

check_value = 0

for start, end in ranges:
    if check_value < start:
        part_2 += (end - start + 1)
        check_value = end + 1
    elif check_value <= end:
        part_2 += (end - check_value + 1)
        check_value = end + 1

print(part_1)
print(part_2)