from collections import Counter

FILE_NAME = 'input14.in'

rules = {}

first = 1
frequencies = Counter()

with open(FILE_NAME, 'r') as file:
    for line in file:
        if first == 1:
            start = line.strip()
            first += 1
        elif first == 2:
            first += 1
        else:
            f, s = line.strip().split(" -> ")
            rules[f] = s

for i in range(len(start)-1):
    frequencies[f'{start[i]}{start[i+1]}'] += 1

STEPS = 40  #change to 10 for part 1

for i in (range(STEPS)):
    new_freqs = frequencies.copy()
    for key, value in frequencies.items():
        if value > 0:
            change = rules[key]
            new_freqs[f'{key[0]}{change}'] += value
            new_freqs[f'{change}{key[1]}'] += value
            new_freqs[key] -= value
    frequencies = new_freqs

letters = Counter()
for key, value in frequencies.items():
    for character in key:
        letters[character] += value

letters[start[0]] += 1
letters[start[-1]] += 1

for key in letters.keys():
    letters[key] //= 2

print(max(letters.values()) - min(letters.values()))


