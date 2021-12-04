FILE_NAME = 'input4.in'

numbers = []
BOARD_SIZE = 5
boards = []
current_board = []

with open(FILE_NAME, 'r') as file:
    for line in file:
        if not numbers:
            numbers = list(map(int, line.strip().split(',')))
        else:
            board_line = line.strip().split()
            if board_line:
                current_board.append(list(map(int, board_line)))
                if len(current_board) == BOARD_SIZE:
                    boards.append(current_board)
                    current_board = []


def mark_board(board, draw):
    for row_index, line in enumerate(board):
        for line_index, value in enumerate(line):
            if value == draw:
                board[row_index][line_index] = None


def check_boards(boards, winning_boards):
    for board_index, board in enumerate(boards):
        if board_index in winning_boards:
            continue
        if check_rows_columns(board):
            return board_index
    return None


def check_rows_columns(board):
    for i in range(BOARD_SIZE):
        all_marked_row, all_marked_column = True, True
        for j in range(BOARD_SIZE):
            if board[i][j] is not None:
                all_marked_row = False
            if board[j][i] is not None:
                all_marked_column = False
            if not all_marked_row and not all_marked_column:
                break
        if all_marked_row or all_marked_column:
            return True
    return False


def calculate_sum(board, draw):
    winner_sum = 0
    for row_index, line in enumerate(board):
        for line_index, value in enumerate(line):
            if value is not None:
                winner_sum += value
    return winner_sum * draw


winning_boards = []

for draw in numbers:
    for board_index, board in enumerate(boards):
        if board_index not in winning_boards:
            mark_board(board, draw)

    winner = 0
    while winner is not None:
        winner = check_boards(boards, winning_boards)
        if winner is not None and winner not in winning_boards:
            winning_boards.append(winner)
            winner_sum = calculate_sum(boards[winner], draw)
            #print(f'Board {winner} just won with the sum of {winner_sum}!')
            if len(winning_boards) == 1:
                print(f'First winner: {winner}, sum: {winner_sum}')


print(f'Last winner: {winning_boards[-1]}, sum: {winner_sum}')



