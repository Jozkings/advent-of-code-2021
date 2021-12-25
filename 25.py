from collections import defaultdict as dd


FILE_NAME = 'input25.in'


def print_map(sea, row, column, step): #for debugging
    print(f'SEA AFTER STEP {step}:\n')
    for i in range(row+1):
        for j in range(column+1):
            print(sea[(i, j)], end='')
        print()
    print()


def move_sea_monsters(sea_monsters, direction):
    change_to_dot = set()
    new_sea_monsters = dd(str)
    changes = 0

    for key, value in sea_monsters.items():
        if value == direction:
            x, y = key
            new_x = x if direction == '>' else x + 1 if x + 1 < row else 0
            new_y = y if direction == 'v' else y + 1 if y + 1 < column else 0
            if sea_monsters[(new_x, new_y)] == '.':
                new_sea_monsters[(new_x, new_y)] = direction
                changes += 1
                change_to_dot.add((x, y))

    for x, y in change_to_dot:
        if direction == '>':
            sea_monsters[(x, y)] = '.'
        else:
            new_sea_monsters[(x, y)] = '.'

    for key in sea_monsters.keys():
        if key not in new_sea_monsters:
            new_sea_monsters[key] = sea_monsters[key]

    return new_sea_monsters, changes


sea_monsters = dd(str)
row = 0

with open(FILE_NAME, 'r') as file:
    for line in file:
        column = 0
        for character in line:
            sea_monsters[(row, column)] = character
            column += 1
        row += 1


steps = 0
changes = 1
while changes:
    sea_monsters, changes = move_sea_monsters(sea_monsters, '>')
    sea_monsters, second_changes = move_sea_monsters(sea_monsters, 'v')
    steps += 1
    #print_map(sea_monsters, row, column, steps)

    changes += second_changes

print(steps)
