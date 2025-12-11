from functools import lru_cache

with open("input.txt") as file:
    lines = [line.strip() for line in file]

part_1 = 0
part_2 = 0

server_paths = {line.split(':')[0]: line.split(':')[1].split() for line in lines}

@lru_cache(maxsize=None)
def count_paths(server, has_dac, has_fft):
    #added for part 2
    if server == 'dac':
        has_dac = True
    if server == 'fft':
        has_fft = True

    if server == 'out':
        return 1 if (has_dac and has_fft) else 0

    total = 0

    for output in server_paths[server]:
        total += count_paths(output, has_dac, has_fft)

    return total

part_1 += count_paths('you', True, True) #assert true to count all connections
part_2 += count_paths('svr',False, False)

print(part_1)
print(part_2)