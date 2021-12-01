FILE_NAME = 'input1.in'

with open(FILE_NAME, 'r') as file:
    vals = [int(line.strip()) for line in file]

last_three = []
sumo = 0
first_res = 0
second_res = 0

for val in vals:
    if len(last_three) < 3:
        last_three.append(val)
        sumo = sum(last_three)
    else:
        last_three[0], last_three[1], last_three[2] = last_three[1], last_three[2], val
        second_res += (sum(last_three) > sumo)
        sumo = sum(last_three)
    if len(last_three) > 1:
        first_res += (last_three[-1] > last_three[-2])

print(first_res)
print(second_res)
