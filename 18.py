import math

FILE_NAME = 'input18.in'
STRING_NUMBERS = [str(digit) for digit in range(10)]


def round_down(number):
    return int(number)


def round_up(number):
    return int(math.ceil(number))


def add(first, second):
    return f'[{first},{second}]'


def reduce(fish):
    change = True
    while change:
        fish, change = explode(fish)
    fish, change = split(fish)
    if change:
        fish = reduce(fish)
    return fish


def get_replacement(index, braces):
    current = ''
    while braces[index] != ']':
        current += braces[index]
        index += 1
    if current[0] == '[':
        current = current[1:]
    if current[-1] == ']':
        current = current[:-1]
    return f'[{current}]'


def get_left_and_right(fish, index):
    current_index = index
    left_start, left_end = None, None
    right_start, right_end = None, None
    while fish[current_index] not in STRING_NUMBERS:
        current_index -= 1
        if current_index < 0:
            break
    if current_index > 0:
        left_end = current_index
        while fish[current_index] in STRING_NUMBERS:
            left_start = current_index
            current_index -= 1

    current_index = index + 6

    while current_index < len(fish) and fish[current_index] not in STRING_NUMBERS:
        current_index += 1
        if current_index == len(fish):
            break
    if current_index < len(fish):
        right_start = current_index
        while fish[current_index] in STRING_NUMBERS:
            right_end = current_index
            current_index += 1
    return left_start, left_end, right_start, right_end


def explode(fish):
    left_start = None
    right_start = None
    leno = 0
    for index, character in enumerate(fish):
        if character in ['[', ']']:
            if character == '[':
                leno += 1
            else:
                leno -= 1
                if leno > 4:
                    replacement = get_replacement(index, fish)
                    new_index = index-1
                    left_start, left_end, right_start, right_end = get_left_and_right(fish, new_index)
                    break
        else:
            if leno > 4:
                replacement = get_replacement(index, fish)
                new_index = index-1
                left_start, left_end, right_start, right_end = get_left_and_right(fish, new_index)
                break

    if left_start is None and right_start is None:
        return fish, False

    if leno > 4 and left_start is None:
        replacement = get_replacement(index, fish)
        new_index = index-1
        left_start, left_end, right_start, right_end = get_left_and_right(fish, new_index)

    new_numbers = replacement.split(',')
    new_numbers[0] = int(new_numbers[0][1:])
    new_numbers[1] = int(new_numbers[1][:-1])

    if left_end is not None:
        new_left_value = new_numbers[0] + int(fish[left_start:left_end+1])
        start_index = left_start
        end_index = left_end
        new_mid_value = new_left_value
    if right_end is not None:
        new_right_value = new_numbers[1] + int(fish[right_start:right_end + 1])
        start_index = right_start
        end_index = right_end
        new_mid_value = new_right_value
    if left_end is not None and right_end is not None:
        fish = fish[:left_start] + str(new_left_value) + fish[left_end + 1:right_start] + str(new_right_value) + fish[right_end + 1:]
    else:
        fish = fish[:start_index] + str(new_mid_value) + fish[end_index + 1:]

    fish = fish[:new_index] + fish[new_index:].replace(replacement, '0', 1)
    return fish, True


def split(fish):
    current = ''
    number_index = -999
    for index, character in enumerate(fish):
        if character in STRING_NUMBERS:
            if number_index == -999:
                number_index = index
            current += character
        else:
            if current and int(current) >= 10:
                break
            current = ''
            number_index = -999
    if number_index == -999:
        return fish, False
    new_left, new_right = round_down(int(current)/2), round_up(int(current)/2)
    new = f'[{new_left},{new_right}]'
    fish = f'{fish[:number_index]}{new}{fish[number_index+len(current):]}'
    return fish, True


def get_magnitude(res):
    if not res:
        return 0
    first = res.count('[')
    second = res.count(']')
    if res[0] not in ['[', ']']:
        return int(res[0]) + get_magnitude(res[2:])
    if first == 1 and second == 1:
        return int(res[1]) * 3 + int(res[3]) * 2
    current = 1
    for index, character in enumerate(res[1:-1]):
        if character == ']':
            current -= 1
            if current == 1:
                if len(res[index+3:-1]) == 1:
                    return 3 * get_magnitude(res[1:index+2]) + 2 * int(res[index+3:-1])
                if len(res[1:index+2]) == 1:
                    return 3 * res[1:index+2] + 2 * get_magnitude(res[index+3:-1])
                return 3 * get_magnitude(res[1:index+2]) + 2 * get_magnitude(res[index+3:-1])
        elif character == '[':
            current += 1


def solve(part2=False):
    snailfish = []
    with open(FILE_NAME, 'r') as file:
        for line in file:
            snailfish.append(line.strip())
    if not part2:
        current = snailfish[0]
        for fish in snailfish[1:]:
            current = add(current, fish)
            current = reduce(current)
        return get_magnitude(current)
    else:
        maximum = 0
        for i, first_fish in enumerate(snailfish):
            for j, second_fish in enumerate(snailfish):
                if i != j:
                    current = add(first_fish, second_fish)
                    current = reduce(current)
                    maximum = max(maximum, get_magnitude(current))
        return maximum


res = solve(True)
print(res)