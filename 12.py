from collections import defaultdict as dd

FILE_NAME = 'input12.in'

#for part 1 solution, uncomment commented line and comment lines with # at the end of them


def dfs(caves, current, visited, two):
    if current == "end":
        return 1
    neighbours = caves[current]
    res = 0
    for neigh in neighbours:
        if neigh == "start":
            continue
        small = neigh.upper() != neigh
        if small:
            if (neigh in two) or (two and neigh in visited):   #
                continue                                       #
            if neigh in visited:                               #
                two.add(neigh)                                 #
            else:                                              #
                visited.add(neigh)                             #
            # if neigh in visited:
            #     continue
            # visited.add(neigh)
        res += dfs(caves, neigh, visited, two)
        if small:
            # visited.remove(neigh)
            if neigh in two:                                   #
                two.remove(neigh)                              #
            elif neigh in visited:                             #
                visited.remove(neigh)                          #
    return res

caves = dd(list)

with open(FILE_NAME, 'r') as file:
    for line in file:
        s, f = line.strip().split('-')
        caves[s].append(f)
        caves[f].append(s)
res = dfs(caves, "start", {"start"}, set())
print(res)

