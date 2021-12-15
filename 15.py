from heapq import heappush, heappop

FILE_NAME = 'input15.in'
cave = []

with open(FILE_NAME, 'r') as file:
    for line in file:
        numbers = line.strip()
        cave.append([int(digit) for digit in numbers])


def dijkstra(cave, repeat=1):
    DUMMY = -999
    max_row = len(cave)
    max_column = len(cave[0])
    result = [[DUMMY for _ in range(repeat * max_column)] for _ in range(repeat * max_row)]
    heap = [(0, 0, 0)]
    while heap:
        distance, row, column = heappop(heap)
        if not ((0 <= row < repeat * max_row) and (0 <= column < repeat * max_column)):
            continue

        cave_value = cave[row % max_row][column % max_column] + (row // max_row) + (column // max_column)

        if cave_value > 9:
            cave_value -= 9

        new_cost = distance + cave_value

        if new_cost >= result[row][column] != DUMMY:
            continue

        result[row][column] = new_cost

        for neigh_x, neigh_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_row, new_column = row + neigh_x, column + neigh_y
            heappush(heap, (result[row][column], new_row, new_column))
    return result[repeat * max_row-1][repeat * max_column-1] - cave[0][0]


print(dijkstra(cave))
print(dijkstra(cave, 5))
