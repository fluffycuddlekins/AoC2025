import re

with open("input.txt") as file:
    lines = [line.strip() for line in file]

id_ranges = lines[0].split(',')

invalid_sum = 0
invalid_2 = 0

for i in id_ranges:
    j,k = i.split('-')

    for l in range(int(j),int(k)+1):
        l_str = str(l)
        if len(l_str) % 2 != 0:
            if re.match(r"^(.+)\1+$", l_str):
                invalid_2 += l
                continue
        if re.match(r"^(.+)\1$",l_str):
            invalid_sum += l
        if re.match(r"^(.+)\1+$",l_str):
            invalid_2 += l

print(invalid_sum)
print(invalid_2)
