FILE_NAME = 'input8.in'

DELIMETER = "|"

sumo = 0
clear_number = 0


def get_diff(first, second):
    first_set, second_set = set(first), set(second)
    return len((first_set | second_set) - (first_set & second_set))


def get_same(first, second):
    first_set, second_set = set(first), set(second)
    return len(first_set & second_set)


with open(FILE_NAME, 'r') as file:
    for line in file:
        codes = {}
        segments, digits = line.strip().split(DELIMETER)
        splitted_segments = list(map(''.join, map(sorted, segments.split())))
        splitted_digits = list(map(''.join, map(sorted, digits.split())))
        for segment in splitted_segments:
            if len(segment) == 2:
                codes[1] = segment
            elif len(segment) == 3:
                codes[7] = segment
            elif len(segment) == 4:
                codes[4] = segment
            elif len(segment) == 7:
                codes[8] = segment
        for segment in splitted_segments:
            if len(segment) == 5:
                if get_diff(codes[1], segment) == 3:
                    codes[3] = segment
                elif get_diff(codes[4], segment) == 3:
                    codes[5] = segment
                else:
                    codes[2] = segment
            elif len(segment) == 6:
                if get_same(codes[1], segment) == 1:
                    codes[6] = segment
                elif get_same(codes[4], segment) == 4:
                    codes[9] = segment
                else:
                    codes[0] = segment
        inverse_codes = {value: str(key) for key, value in codes.items()}
        clear_number += sum([1 for digit in splitted_digits if inverse_codes[digit] in ['1', '4', '7', '8']])
        sumo += int(''.join([inverse_codes[digit] for digit in splitted_digits]))

print(clear_number) #part 1
print(sumo)  #part 2
