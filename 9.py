from functools import reduce

FILE_NAME = 'input9.in'


def get_basin(point, points):
    queue = [point]
    used = set()
    while queue:
        current = queue.pop(0)
        used.add(current)
        x, y = current
        current_value = points[current]
        for neighbour in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if neighbour in points:
                if current_value < points[neighbour] < 9 and neighbour not in used:
                    queue.append(neighbour)
    return len(used)


points = {}
row = 0
for line in open(FILE_NAME).readlines():
    column = 0
    for character in line.strip():
        points[(row, column)] = int(character)
        column += 1
    row += 1

maxos = []
sumo = 0

for key, value in points.items():
    x, y = key
    potential_neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    neighbours = []
    for neigh in potential_neighbours:
        if neigh in points:
            neighbours.append(neigh)
    if value < min(map(lambda val: points[val], neighbours)) and neighbours.count(key) == 0:
        sumo += 1 + value
        maxos.append(get_basin(key, points))

maxos = sorted(maxos, reverse=True)
prod = reduce(lambda x, y: x * y, maxos[:3])
print(sumo)  #part 1
print(prod)  #part 2
