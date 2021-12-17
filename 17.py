FILE_NAME = 'input17.in'


def simulate(velocity_x, velocity_y):
    bounded_highest = -999
    x, y = 0, 0
    possible = True
    while possible:
        x += velocity_x
        y += velocity_y
        velocity_x = velocity_x + 1 if velocity_x < 0 else velocity_x - 1 if velocity_x > 0 else velocity_x
        bounded_highest = max(bounded_highest, y)
        velocity_y -= 1
        if MIN_X <= x <= MAX_X and MIN_Y <= y <= MAX_Y:
            return True, bounded_highest
        if (y < MIN_Y and velocity_y < 0) or (x < MIN_X and velocity_x < 0):
            possible = False
    return False, None


with open(FILE_NAME, 'r') as file:
    for line in file:
        data = line.split("=")
        xdata, ydata = data[1][:-3], data[2]
        xdatas, ydatas = list(map(int, xdata.split(".."))), list(map(int, ydata.split("..")))
        (MIN_X, MAX_X), (MIN_Y, MAX_Y) = xdatas, ydatas

highest_y = -99999
all_good = []
for velocity_x in range(MAX_X+10):  #not proven bounds in any way
    for velocity_y in range(-abs(MIN_Y), abs(MIN_Y)):
        result, bounded_highest = simulate(velocity_x, velocity_y)
        if result:
            all_good.append((velocity_x, velocity_y))
            highest_y = max(highest_y, bounded_highest)

print(highest_y)  #part 1
print(len(all_good)) #part 2
