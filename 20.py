from collections import defaultdict as dd

FILE_NAME = 'input20.in'
conversion = {'.': '0', '#': '1'}
STEPS = 50 #takes a little while
MARGIN = 3
NEIGHBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


def print_image(dicto, min_row, min_column, max_row, max_column, background): #help for debugging
    for i in range(min_row-3, max_row+3):
        for j in range(min_column-3, max_column+3):
            print(background if (i, j) not in dicto else dicto[(i,j)], end='')
        print()


def get_pixel_value(key, input_image_dict, background):
    row, column = key
    value = ''
    for (row_change, column_change) in NEIGHBOURS:
        neighbour_key = row + row_change, column + column_change
        value += background if neighbour_key not in input_image_dict else input_image_dict[neighbour_key]
    return value


def convert_to_binary_string(value):
    return ''.join(list(map(lambda character: conversion[character], value)))


first = True
input_image_dict = dd(str)
enhancement_algo = ''
min_row, min_column = 0, 0
max_row, max_column = 0, 0

with open(FILE_NAME, 'r') as file:
    row = 0
    for line in file:
        line = line.strip()
        if line:
            if first:
                enhancement_algo += line
                first = False
            else:
                for column in range(len(line)):
                    input_image_dict[(row, column)] = line[column]
                max_column = column
                max_row = row
                row += 1

SPECIALS = ['.', '#'] if enhancement_algo[0] == '#' and enhancement_algo[-1] == '.' else ['.', '.'] #case #, # handled below
                                                                    #in case of . first, background will be always .
for step in range(STEPS):
    new_input_image = dd(str)
    background = SPECIALS[step % 2]
    for row in range(min_row-MARGIN, max_row+MARGIN):
        for column in range(min_column-MARGIN, max_column+MARGIN):
            key = (row, column)
            new_value = get_pixel_value(key, input_image_dict, background)
            binary_value = convert_to_binary_string(new_value)
            decimal_value = int(binary_value, 2)
            final_value = enhancement_algo[decimal_value]
            new_input_image[key] = final_value

    input_image_dict = new_input_image
    min_row -= MARGIN
    min_column -= MARGIN
    max_row += MARGIN
    max_column += MARGIN

    #print_image(input_image_dict, min_row, min_column, max_row, max_column, background)
    if step == 0 and enhancement_algo[0] == '#' and enhancement_algo[-1] == '#':  #case #, #
        SPECIALS = ['#', '#']   #doesn't work in practice (because of infinite space) but
                               #input is (probably) never in this form; this only shows the idea
print(sum(pixel == '#' for pixel in input_image_dict.values()))


