from functools import reduce
from operator import mul

FILE_NAME = 'input16.in'
mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
           '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000',
           '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
           'E': '1110', 'F': '1111'
           }


def convert_to_decimal_int(value):
    return int(value, 2)


def parse_operator(index, depth):
    length_type_id = digits[index]
    index += 1
    print(f"{'-' * depth}{'> ' if depth else ''}Length type id: {length_type_id}")
    index, values = parse_length_type_id(length_type_id, index, depth)
    return index, values


def parse_length_type_id(length_type_id, index, depth):
    if length_type_id == "1":
        index, values = parse_number_of_sub_packets(index, depth)
    else:
        index, values = parse_total_length_in_bits(index, depth)
    return index, values


def parse_total_length_in_bits(index, depth):
    total_length = ''.join(digits[index:index + TOTAL_LENGTH_IN_BITS_LENGTH])
    index += TOTAL_LENGTH_IN_BITS_LENGTH
    length = convert_to_decimal_int(total_length)
    print(f"{'-' * depth}{'> ' if depth else ''}Length of subpackets: {length}")
    end_index = index + length
    values = []
    while index != end_index:
        index, value = parse_packet(index, depth + 1)
        values.append(value)
    return index, values


def parse_number_of_sub_packets(index, depth):
    no_subpackets = ''.join(digits[index:index + NUMBER_OF_SUBPACKETS_LENGTH])
    number = convert_to_decimal_int(no_subpackets)
    index += NUMBER_OF_SUBPACKETS_LENGTH
    print(f"{'-' * depth}{'> ' if depth else ''}Number of subpackets: {number}")
    values = []
    for _ in range(number):
        index, value = parse_packet(index, depth + 1)
        values.append(value)
    return index, values


def parse_packet(index, depth):
    version = ''.join(digits[index:index + HEADER_LENGTH])
    index += HEADER_LENGTH
    type_id = ''.join(digits[index:index + HEADER_LENGTH])
    index += HEADER_LENGTH

    version_decimal = convert_to_decimal_int(version)
    type_id_decimal = convert_to_decimal_int(type_id)
    print(f"{'-' * depth}{'> ' if depth else ''}Version: {version} ({version_decimal}), Type_id: {type_id} ({type_id_decimal})")
    all_versions.append(version_decimal)
    if type_id_decimal != 4:
        index, values = parse_operator(index, depth)
        if type_id_decimal == 0:
            operation_type, res = "Sum", sum(values)
        elif type_id_decimal == 1:
            operation_type, res = "Product", reduce(mul, values)
        elif type_id_decimal == 2:
            operation_type, res = "Minimum", min(values)
        elif type_id_decimal == 3:
            operation_type, res = "Maximum", max(values)
        elif type_id_decimal == 5:
            operation_type, res = "Greater than", values[0] > values[1]
        elif type_id_decimal == 6:
            operation_type, res = "Less than", values[0] < values[1]
        elif type_id_decimal == 7:
            operation_type, res = "Equal to", values[0] == values[1]
        else:
            raise Exception(f"Unknown type_id: {type_id}!")
        print(f"{'-' * depth}{'> ' if depth else ''}{operation_type}: {res}")
        literal_value_decimal = res
    else:
        literal_value = ""
        while digits[index] != '0':
            literal_value += ''.join(digits[index + 1:index + 1 + LITERAL_VALUE_LENGTH])
            index += 1 + LITERAL_VALUE_LENGTH
        literal_value += ''.join(digits[index + 1:index + 1 + LITERAL_VALUE_LENGTH])
        index += 1 + LITERAL_VALUE_LENGTH
        literal_value_decimal = convert_to_decimal_int(literal_value)
        print(f"{'-' * depth}{'> ' if depth else ''}Literal value: {literal_value} ({literal_value_decimal})")
    return index, literal_value_decimal


def recursive_parse():
    parse_packet(0, 0)


digits = [x for x in open(FILE_NAME).read().strip()]
digits = ''.join(list(map(lambda val: mapping[val], digits)))
all_versions = []
TOTAL_LENGTH_IN_BITS_LENGTH = 15
NUMBER_OF_SUBPACKETS_LENGTH = 11
HEADER_LENGTH = 3
LITERAL_VALUE_LENGTH = 4
recursive_parse()  #part 1 + 2
print(f"Sum of all versions: {sum(all_versions)}") #part 1
