FILE_NAME = 'input3.in'

numbers = []


def digits_frequency(numbers, bit, reverse=False):
    ones = 0
    zeroes = 0
    for numo in numbers:
        if numo[bit] == "1":
            ones += 1
        else:
            zeroes += 1
    if reverse:
        return "0" if zeroes <= ones else "1"
    return "1" if ones >= zeroes else "0"


def get_ratings(numbers, LENGTH, reverse=False):
    good = []
    new_good = numbers[:]
    for bit in range(LENGTH):
        most_common = digits_frequency(new_good, bit, reverse=reverse)
        for number in new_good:
            if number[bit] == most_common:
                good.append(number)
        if len(good) == 1:
            return good.pop()
        new_good = good[:]
        good = []
    return -1


def solve_first_part(numbers, LENGTH):
    gamma, epsilon = "", ""
    for bit in range(LENGTH):
        most_common = digits_frequency(numbers, bit)
        gamma += most_common
        epsilon += str(1 - int(most_common))
    return gamma, epsilon


def solve_second_part(numbers, LENGTH):
    oxygen = get_ratings(numbers, LENGTH)
    co2 = get_ratings(numbers, LENGTH, reverse=True)
    return oxygen, co2


with open(FILE_NAME, 'r') as file:
    for line in file:
        value = line.strip().split()[0]
        numbers.append(value)

LENGTH = len(numbers[0])

gamma, epsilon = solve_first_part(numbers, LENGTH)
print(int(gamma, 2) * int(epsilon, 2))  #part 1 result

oxygen, co2 = solve_second_part(numbers, LENGTH)
print(int(oxygen, 2) * int(co2, 2))  #part 2 result







