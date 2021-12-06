FILE_NAME = 'input6.in'

DIVIDER = ","
values = [int(x) for x in open(FILE_NAME).read().split(DIVIDER)]
DAYS = 256 #for part 1, change here
map = {i:0 for i in range(0, 9)}
for val in values:
    map[val] += 1
for day in range(DAYS):
    new = map[0]
    for i in range(8):
        map[i] = map[i+1]
    map[8] = new
    map[6] += new
print(sum(map.values()))
