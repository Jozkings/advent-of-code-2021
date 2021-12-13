FILE_NAME = 'input13.in'


dots = {}
fold_start = False
folds = []


def print_paper(dots):
    max_x, max_y = max(dots, key=lambda val:val[0])[0], max(dots, key=lambda val:val[1])[1]
    for i in range(max_y+1):
        for j in range(max_x+1):
            if (j, i) in dots:
                print(dots[(j, i)], end="")
            else:
                print(".", end="")
        print()


with open(FILE_NAME, 'r') as file:
    for line in file:
        data = line.strip()
        if not data:
            fold_start = True
        else:
            if not fold_start:
                x, y = list(map(int, data.split(',')))
                dots[(x, y)] = "#"
            else:
                axis, lines_number = line.split("=")
                folds.append((axis[-1], int(lines_number)))

for index, fold in enumerate(folds):
    new_dots = {}
    axis, lines_number = fold
    x_axis = True
    if axis == "y":
        x_axis = False
    for position in dots.keys():
        x, y = position
        coord = x if x_axis else y
        if coord < lines_number:
            new_dots[position] = "#"
            continue
        new_coord = lines_number - (coord - lines_number)
        new_position = (new_coord, y) if x_axis else (x, new_coord)
        new_dots[new_position] = "#"
    dots = new_dots
    if index == 0:
        print(len(dots))

print_paper(dots)

