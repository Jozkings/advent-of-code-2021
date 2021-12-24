FILE_NAME = 'input24.in'


def run_commands(z, model_digit, index):
    z_division, x_addition, y_addition = actual_operations[index]
    w = model_digit                       #line 1
    x = 0                                 #line 2
    x += z                                #line 3
    x %= 26                               #line 4
    z //= z_division                      #line 5
    x += x_addition                       #line 6
    x = x == w                            #line 7
    x = x == 0                            #line 8
    y = 0                                 #line 9
    y += 25                               #line 10
    y *= x                                #line 11
    y += 1                                #line 12
    z *= y                                #line 13
    y *= 0                                #line 14
    y += w                                #line 15
    y += y_addition                       #line 16
    y *= x                                #line 17
    z += y                                #line 18
    #or shorter:
    # x = (z % 26) + x_addition != w
    # z //= z_division
    # z *= (25 * x) + 1
    # z += (w + y_addition) * x
    return z


def extract_important(code):
    results_index = -1
    results = [[] for _ in range(CYCLES_NUMBER)]
    for index, line in enumerate(code):
        if 'inp' in line:
            results_index += 1
            was_add_y = 0
        else:
            command, variable, important = line
            if command == 'div' or (command == 'add' and variable == 'x' and not important.isalpha()): #isdigit() not
                results[results_index].append(int(important))                              #working for negative values
            elif command == 'add' and variable == 'y' and important.isdigit():
                if was_add_y < 2:
                    was_add_y += 1
                else:
                    results[results_index].append(int(important))
    return results


def get_model_numbers(current_index, current_result):
    if current_index == CYCLES_NUMBER:
        if current_result == 0:
            return [0]
        return []

    if current_result > maximum_allowed_z[current_index]:
        return []

    if (current_index, current_result) in memo:
        return memo[(current_index, current_result)]

    model_digits = list(range(9, 0, -1))
    final_result = []

    for w in model_digits:
        cycle_result = run_commands(current_result, w, current_index)
        results = get_model_numbers(current_index + 1, cycle_result)
        for model_number in results:
            final_result.append((w * 10**(CYCLES_NUMBER - current_index - 1)) + model_number)

    memo[(current_index, current_result)] = final_result
    return final_result


with open(FILE_NAME, 'r') as file:
    alu_code = [line.strip().split() for line in file]

CYCLE_LENGTH = [command[0] for index, command in enumerate(alu_code) if index != 0].index('inp') + 1
CYCLES_NUMBER = len(alu_code) // CYCLE_LENGTH  #some of constructions are from observation of input

actual_operations = extract_important(alu_code)
maximum_allowed_z = [26 ** (len(actual_operations) - index) for index in range(len(actual_operations))] #otherwise z
memo = {}                                                                                       #cannot be 0 in the end

solutions = get_model_numbers(0, 0)
print(max(solutions))  #part1
print(min(solutions))  #part2


