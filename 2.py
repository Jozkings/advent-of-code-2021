FILE_NAME = 'input2.in'

pos = 0
depth = 0
aim = 0

with open(FILE_NAME, 'r') as file:
    for line in file:
        value = line.strip().split()
        command, units = value[0], int(value[1])
        if command == "forward":
            pos += units
            depth += (aim * units)
        elif command == "up":
            #depth -= units
            aim -= units
        elif command == "down":
            #depth += units
            aim += units
        else:
            raise Exception("bad command!")

print(pos * depth) #for the first part, comment line 13, for the second, comment lines 15, 18