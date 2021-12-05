from collections import defaultdict as dd

FILE_NAME = 'input5.in'

lines = dd(list)
line_counter = 0

with open(FILE_NAME, 'r') as file:
    for line in file:
        value = line.strip().split("->")
        x1, y1 = list(map(int, value[0].strip().split(",")))
        x2, y2 = list(map(int, value[1].strip().split(",")))
        if y1 == y2: #vertical line
            maxo, mino = max(x1, x2), min(x1, x2)
            for i in range(mino, maxo+1):
                lines[f'{i, y1}'].append(line_counter)
        elif x1 == x2: #horizontal line
            maxo, mino = max(y1, y2), min(y1, y2)
            for i in range(mino, maxo+1):
                lines[f'{x1, i}'].append(line_counter)
        elif x1 - y1 == x2 - y2: #first diagonal line, comment for part 1
            maxo, mino = max(x1, x2), min(x1, x2)
            diff = maxo-mino
            ty = y2 if x1 >= x2 else y1
            for i in range(diff+1):
                lines[f'{mino+i, ty+i}'].append(line_counter)
        elif x1 + y1 == x2 + y2: #second diagonal line, comment for part 1
            maxo, mino = max(x1, x2), min(x1, x2)
            diff = maxo-mino
            ty = y2 if x1 >= x2 else y1
            for i in range(diff+1):
                lines[f'{mino+i, ty-i}'].append(line_counter)
        else:
            raise Exception("This input is not a line!")
        line_counter += 1

print(len(list(filter(lambda val: len(val) > 1, lines.values()))))


