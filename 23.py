from heapq import heappush, heappop

FILE_NAME = 'input23.in'
mapo = ''
row = 0
COLUMN_LENGTH = 0
MOVES_COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
AMPHIPODS = 'ABCD'


def move(map):
    new_maps, upps, distances = [], [], []

    for final_positions in positions:
        top = None
        freedom = len(AMPHIPODS) + 1
        for position in final_positions:
            if map[position] == '.':
                break
            top = position
            freedom -= 1
        upps.append(top)
        distances.append(freedom)

    for i in range(len(AMPHIPODS)):
        if not upps[i]:
            continue
        entrance = entrances[i]
        for position in halls:
            if all(map[next_cell] == '.' for next_cell in range(min(position, entrance), max(position, entrance)+1)):
                what = map[upps[i]]
                new_map = map[:position] + what + map[position + 1:]
                new_map = new_map[:upps[i]] + '.' + new_map[upps[i] + 1:]
                distance = (distances[i] + abs(position - entrance)) * MOVES_COST[what]

                new_distance = 1
                while new_distance:
                    new_distance, new_map = go(new_map)
                    if new_distance == 0:
                        break
                    distance += new_distance
                new_maps.append((distance, new_map))

    return new_maps


def go(map):
    for index, final_positions in enumerate(positions):
        empty = None
        character = AMPHIPODS[index]
        distance = len(AMPHIPODS)
        for position in final_positions:
            if map[position] == '.':
                empty = position
                break
            if map[position] != character:
                break
            distance -= 1
        if empty is None:
            continue

        entrance = entrances[index]
        for position in halls:
            if all((position == new_position and map[new_position] == character) or
                   (new_position != position and map[new_position] == '.')
                   for new_position in range(min(position, entrance), max(position, entrance)+1)):
                distance = (abs(position - entrance) + distance) * MOVES_COST[character]
                new_map = map[:position] + '.' + map[position+1:]
                new_map = new_map[:empty] + character + new_map[empty+1:]
                return distance, new_map
    return 0, map


def check_win(map):
    for index, final_positions in enumerate(positions):
        if not all(map[position] == AMPHIPODS[index] for position in final_positions):
            return False
    return True


with open(FILE_NAME, 'r') as file:
    for line in file:
        mapo += line
        row += 1
        if row == 3:
            mapo += '  #D#C#B#A#  \n'
            row += 1
            mapo += '  #D#B#A#C#  \n'
            row += 1
        if COLUMN_LENGTH == 0:
            COLUMN_LENGTH = len(line)
        if len(line) != COLUMN_LENGTH:
            mapo = mapo[:-1]
            mapo += ' ' * (COLUMN_LENGTH - len(line))
            mapo += '\n'


positions = [[] for _ in range(4)]
halls = []
entrances = []
MODULOS = {3: 0, 5: 1, 7: 2, 9: 3}

for index, character in enumerate(mapo):
    if character == '.':
        if mapo[index + COLUMN_LENGTH].isalpha():
            entrances.append(index)
        else:
            halls.append(index)
    elif character.isalpha():
        hall_index = MODULOS[index % COLUMN_LENGTH]
        positions[hall_index].append(index)

for i in range(len(positions)):
    positions[i] = positions[i][::-1]

heap = []
heappush(heap, (0, mapo))
visited = set()


while heap:
    distance, current_map = heappop(heap)

    if current_map in visited:
        continue

    visited.add(current_map)

    if check_win(current_map):
        break

    for new_distance, new_map in move(current_map):
        heappush(heap, (distance + new_distance, new_map))

print(distance)  #part 2 only


