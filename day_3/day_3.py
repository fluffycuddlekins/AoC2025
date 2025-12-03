with open("input.txt") as file:
    lines = [line.strip() for line in file]

part_1 = 0
part_2 = 0

for line in lines:
    index = 0
    tens = "0"
    ones = "0"
    for i in range(len(line)-1):
        if int(line[i]) > int(tens):
            tens = line[i]
            index = i
    for j in range(index+1,(len(line))):
        if int(line[j]) > int(ones):
            ones = line[j]
    jolt = int(tens + ones)
    part_1 += jolt

for line in lines:
    length = len(line)
    digits_left = 12
    index = 0
    result = []

    while digits_left > 0:
        end = length - digits_left
        max_digit = "0"
        position = index
        for i in range(index, end+1):
            if int(line[i]) > int(max_digit):
                max_digit = line[i]
                position = i
                if int(max_digit) == 9:
                    break
        result.append(max_digit)
        index = position + 1
        digits_left -= 1

    jolt_12 = ''.join(result)
    part_2 += int(jolt_12)

print(part_1)
print(part_2)