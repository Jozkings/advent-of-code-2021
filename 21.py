FILE_NAME = 'input21.in'


def wrap(position):
    return (position % SPACES) + (SPACES * (position % SPACES == 0))


def turn(player):
    rolls = [dice_number, dice_number+1, dice_number+2]
    dices_sum = sum(rolls) % 100
    positions[player] += dices_sum
    positions[player] = wrap(positions[player])
    scores[player] += positions[player]


def recursive_memo(first_position, second_position, first_score, second_score):
    first_end = first_score >= reach
    second_end = second_score >= reach
    if first_end or second_end:
        return first_end, second_end
    if (first_position, second_position, first_score, second_score) in memo:
        return memo[(first_position, second_position, first_score, second_score)]

    wins, losses = 0, 0

    for first_dice_value in DICE_OUTCOMES:
        for second_dice_value in DICE_OUTCOMES:
            for third_dice_value in DICE_OUTCOMES:
                rolls = [first_dice_value, second_dice_value, third_dice_value]
                dices_sum = sum(rolls)
                new_first_position = first_position + dices_sum
                new_first_position = wrap(new_first_position)
                new_first_score = first_score + new_first_position
                future_losses, future_wins = recursive_memo(second_position, new_first_position, second_score, new_first_score)
                wins += future_wins
                losses += future_losses

    memo[(first_position, second_position, first_score, second_score)] = (wins, losses)
    return wins, losses


start_positions = {}

with open(FILE_NAME, 'r') as file:
    for line in file:
        line = line.split()
        start_positions[int(line[1])] = int(line[-1])

rolls = 0
reach = 1000
scores = {1: 0, 2: 0}
dice_number = 1
SPACES = 10
positions = start_positions.copy()

while scores[2] < reach:
    for player in [1, 2]:
        turn(player)
        dice_number = (dice_number + 3) % 100
        rolls += 3
        if scores[1] >= reach:
            break

print(min(scores.values()) * rolls) #part1

reach = 21
DICE_OUTCOMES = list(range(1, 4))
memo = {}
positions = start_positions.copy()
print(max(recursive_memo(positions[1], positions[2], 0, 0))) #part2

