FILE_NAME = 'input10.in'


def are_chunks_correct(chunk):
    stack = []
    matches = {"(": ")", "[": "]", "{": "}", "<": ">"}
    for char in chunk:
        if char in MATCHES.keys():
            stack.append(char)
        else:
            if not stack:
                return False, None
            current_char = stack.pop()
            if matches[current_char] != char:
                return False, char
    if stack:
        return False, f"{INCOMPLETE_ERR}{stack[-1]}"
    return True, None


ILLEGALS_POINST = {")": 3, "]": 57, "}": 1197, ">": 25137}
INCOMPLETE_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}
MATCHES = {"(": ")", "[": "]", "{": "}", "<": ">"}
INCOMPLETE_ERR = "In stack still: "
sumo = 0
scores = []


with open(FILE_NAME, 'r') as file:
    for line in file:
        line = line.strip()
        score = 0
        res, what = are_chunks_correct(line)
        while not res:
            if INCOMPLETE_ERR not in what:
                sumo += ILLEGALS_POINST[what]
                break
            line += MATCHES[what[-1]]
            score *= 5
            score += INCOMPLETE_POINTS[MATCHES[what[-1]]]
            res, what = are_chunks_correct(line)
        if score != 0:
            scores.append(score)

print(sumo)
print(sorted(scores)[(len(scores)//2)])
