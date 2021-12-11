from collections import defaultdict as dd

FILE_NAME = 'input11.in'

octupuses = dd(int)
STEPS = 5000

def get_neighbours(octos, oct):
    x, y = oct
    res = []
    for a, b in [(x+1, y), (x-1, y), (x, y+1), (x,y-1), (x+1, y+1), (x+1, y-1), (x-1, y-1), (x-1, y+1)]:
        if (a, b) in octos:
            res.append((a, b))
    return res


def printo(octos): #for easier debugging
    for i in range(100):
        for j in range(100):
            if (i, j) not in octupuses:
                break
            print(octupuses[(i, j)], end="")
        print()


with open(FILE_NAME, 'r') as file:
    row = 0
    for line in file:
        column = 0
        line = line.strip()
        for character in line:
            octupuses[(row, column)] = int(character)
            column += 1
        row += 1

all_flashes = 0
FLASHING_TIME = 9

for step in range(STEPS):
    for key in octupuses.keys():
        octupuses[key] += 1

    is_changing = True
    flashing = 0
    while is_changing:
        changes = dd(int)
        for key, value in octupuses.items():
            if value > 9:
                neighs = get_neighbours(octupuses, key)
                for neigh in neighs:
                    if octupuses[neigh] == 0 or octupuses[neigh] > FLASHING_TIME:
                        continue
                    changes[neigh] += 1
                octupuses[key] = 0    #flash octopus
                flashing += 1
                all_flashes += 1
        for key in changes.keys():   #change neighbours
            octupuses[key] = min(octupuses[key] + changes[key], FLASHING_TIME+1)
        is_changing = len(changes) > 0
    if step == 99:
        print(f"Number of flashes until step 100 is {all_flashes}!")
    if flashing == len(octupuses):
        print(f"All flashed in step {step+1}!")
        break

