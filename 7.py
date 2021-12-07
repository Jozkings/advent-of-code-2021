FILE_NAME = 'input7.in'

DIVIDER = ","
numbers = [int(x) for x in open(FILE_NAME).read().split(DIVIDER)]
mino, maxo = min(numbers), max(numbers)
best = None
for i in range(mino, maxo+1):
    sumo = 0
    for numo in numbers:
        diff = abs(numo - i)
        sumo += int((diff/2) * (diff+1)) #part 2
        #sumo += diff             #part 1
    best = sumo if best is None else min(best, sumo)

print(best)

