from collections import defaultdict as dd
import time

FILE_NAME = 'input19.in'

scanners = dd(list)
aligned_scanners = dd(list)
rotations = [(-1, -1, -1), (-1, -1, 1), (-1, 1, -1), (-1, 1, 1), (1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1)]
remapping = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
all_distances = [(0, 0, 0)]


def get_farthest_scanners():
    maximum_distance = 0
    for first_scanner in all_distances:
        for second_scanner in all_distances:
            if first_scanner != second_scanner:
                maximum_distance = max(maximum_distance, get_manhattan_distance(first_scanner, second_scanner))
    return maximum_distance


def get_number_of_beacons():
    all_beacons = (list(set().union(*list(map(list, aligned_scanners.values())))))
    return len(all_beacons)


def get_manhattan_distance(first, second):
    distances = [abs(first[index]-second[index]) for index in range(len(first))]
    return sum(distances)


def get_edited(beacon, remap, rotation):
    return list(map(lambda beac: (rotation[0] * beac[remap[0]], rotation[1] * beac[remap[1]], rotation[2] * beac[remap[2]]), beacon))


def find_overlapping(first_beacons, second_beacons):
    for remap in remapping:
        for rotation in rotations:
            first_copy = first_beacons
            second_copy = get_edited(second_beacons, remap, rotation)
            for first_position in first_copy:
                for second_position in second_copy:
                    overlaps = 0
                    new_remaps = tuple(second_position[index] - first_position[index] for index in range(3))
                    remapped = []
                    for new_second in second_copy:
                        new_first = tuple(new_second[index] - new_remaps[index] for index in range(3))
                        remapped.append(new_first)
                        overlaps += (new_first in first_beacons)
                    if overlaps >= 12:
                        all_distances.append(new_remaps)
                        return remapped
    return None

with open(FILE_NAME, 'r') as file:
    for line in file:
        line = line.strip()
        if "scanner" in line:
            number = int(line.split()[2])
        elif line:
            beacons = tuple(map(int, line.split(',')))
            scanners[number].append(beacons)

aligned_scanners[0] = scanners[0]

while len(aligned_scanners) != len(scanners):  #takes a while
    for i in range(len(scanners)):
        if i not in aligned_scanners:
            for j in aligned_scanners.keys():
                remapping_result = find_overlapping(aligned_scanners[j], scanners[i])
                if remapping_result is not None:
                    aligned_scanners[i] = remapping_result
                    break


print(f"Number of beacons: {get_number_of_beacons()}")
print(f"2 farthest scanners have manhattan distance of: {get_farthest_scanners()}")
