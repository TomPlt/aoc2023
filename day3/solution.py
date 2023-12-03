import re

def is_adjacent_to_symbol(schematic, x, y):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(schematic) and 0 <= ny < len(schematic[nx]):
                if schematic[nx][ny] not in '.0123456789':
                    return True
    return False

def sum_part_numbers(schematic):
    sum_of_parts = 0
    for x, line in enumerate(schematic):
        for match in re.finditer(r'\d+', line):
            number = int(match.group())
            start, end = match.start(), match.end()
            if any(is_adjacent_to_symbol(schematic, x, y) for y in range(start, end)):
                sum_of_parts += number
    return sum_of_parts

def sum_prod_gears(schematic):
    sum_of_gears = 0

    number_positions = []
    for x, line in enumerate(schematic):
        number_positions.append([])
        for match in re.finditer(r'\d+', line):
            number_positions[x].append((int(match.group()), match.start(), match.end() - 1))

    for x, line in enumerate(schematic):
        for match in re.finditer(r'\*', line):
            pos_y = match.start()
            adjacent_parts = set()
            prod_adjacent_parts = 1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, pos_y + dy
                    if 0 <= nx < len(schematic):
                        for num, start, end in number_positions[nx]:
                            if start <= ny <= end:
                                adjacent_parts.add(num)
            
            if len(adjacent_parts) == 2:
                prod_adjacent_parts = adjacent_parts.pop() * adjacent_parts.pop()
                sum_of_gears += prod_adjacent_parts
    return sum_of_gears


                                        
with open("data.txt") as f:
    schematic = f.read().splitlines()

print(sum_part_numbers(schematic), sum_prod_gears(schematic))

