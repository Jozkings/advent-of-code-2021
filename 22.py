from itertools import product

FILE_NAME = 'input22.in'


def get_current_coords(cube_data, first_part=False):
    switch, data = cube_data.split(' ')
    datas = data.split(',')
    all_coords = []
    for dato in datas:
        axis, coords = dato.split('=')
        coords_range = list(map(int, coords.split('..')))
        if first_part and not (-50 <= coords_range[0] <= 50):  # not really correct but works for input(s)
            break
        all_coords.append(coords_range)
    return switch, all_coords


def has_overlap(first, second):
    first_one, first_two, first_three = first
    second_one, second_two, second_three = second
    return first_one[0] <= second_one[1] and first_one[1] >= second_one[0] and \
           first_two[0] <= second_two[1] and first_two[1] >= second_two[0] and \
           first_three[0] <= second_three[1] and first_three[1] >= second_three[0]


def is_overlapping(first, second):
    return has_overlap(first, second) or has_overlap(second, first)


def is_correct(cube):
    first, second, third = cube
    return first[1] >= first[0] and second[1] >= second[0] and third[1] >= third[0]


def get_cuboid_size(cuboid):
    return (cuboid[0][1] - cuboid[0][0] + 1) * (cuboid[1][1] - cuboid[1][0] + 1) * (cuboid[2][1] - cuboid[2][0] + 1)


def get_correct(first, second):
    first_one, first_two, first_three = first
    second_one, second_two, second_three = second
    xs = [[first_one[0], second_one[0] - 1], [second_one[1] + 1, first_one[1]],
          [max(first_one[0], second_one[0]), min(first_one[1], second_one[1])]]
    ys = [[first_two[0], second_two[0] - 1], [second_two[1] + 1, first_two[1]],
          [max(first_two[0], second_two[0]), min(first_two[1], second_two[1])]]
    zs = [[first_three[0], second_three[0] - 1], [second_three[1] + 1, first_three[1]],
          [max(first_three[0], second_three[0]), min(first_three[1], second_three[1])]]

    result = []
    for combo in product(xs, ys, zs):
        if is_correct(combo) and not is_overlapping(combo, second):
            result.append(combo)
    return result


def remove_duplicates(cubes, new_cubes):
    result = []
    for cube in cubes:
        if is_overlapping(cube, new_cubes):
            result += get_correct(cube, new_cubes)
        else:
            result.append(cube)
    return result


with open(FILE_NAME, 'r') as file:
    cubes = []
    all_data = []
    for line in file:
        all_data.append(line)

    for cube_data in all_data:
        switch, all_coords = get_current_coords(cube_data, first_part=True)
        if all_coords:
            cubes = remove_duplicates(cubes, all_coords)
            if switch == 'on':
                cubes.append(all_coords)
    print(sum([get_cuboid_size(cuboid) for cuboid in cubes])) #part 1

    cubes = []

    for cube_data in all_data:
        switch, all_coords = get_current_coords(cube_data)
        cubes = remove_duplicates(cubes, all_coords)
        if switch == 'on':
            cubes.append(all_coords)
    print(sum([get_cuboid_size(cuboid) for cuboid in cubes])) #part 2
