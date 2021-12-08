import re

all_draws = []
taken_draw_vals = []
max_cell_val = 100
board_dimension = 5
boards = []
boards_col_match_count = []
boards_row_match_count = []
cell_val_pointers = [[] for _ in range(max_cell_val)]
completed_board_idxs = []
not_yet_completed_board_idxs = []
completed_draw_idxs = []
completed_draw_vals = []


def is_a_completion_draw(iacd_board_idx, iacd_val_col, iacd_val_row):
    is_col_match = boards_col_match_count[iacd_board_idx][iacd_val_col] >= board_dimension
    is_row_match = boards_row_match_count[iacd_board_idx][iacd_val_row] >= board_dimension
    board_not_yet_won = iacd_board_idx not in completed_board_idxs
    return board_not_yet_won and (is_col_match or is_row_match)


def is_all_boards_complete():
    return len(not_yet_completed_board_idxs) == 0


def calculate_board_cell_sum(cbcs_board, cbcs_draw):
    cell_sum = 0
    draws = []
    for draw in taken_draw_vals:
        draws.append(draw)
        if draw == cbcs_draw:
            break
    for row_idx, row_vals in enumerate(cbcs_board):
        for col_idx, cell_val in enumerate(row_vals):
            if cell_val not in draws:
                cell_sum += cell_val
    return cell_sum


board = []
init_col_match_counts = [0 for i in range(board_dimension)]
with open("day4-2.data") as f:
    for line_idx, line in enumerate(f):
        line = line.strip()

        if line_idx == 0:
            all_draws = [int(x) for x in line.split(',')]
            continue

        board_row_idx = (line_idx - 2) % 6
        if board_row_idx == board_dimension:
            board = []
            boards.append(board)
            boards_col_match_count.append(init_col_match_counts.copy())
            boards_row_match_count.append(init_col_match_counts.copy())
            continue

        board_row_vals = [int(x) for x in re.split('\s+', line)]
        board.append(board_row_vals)
        for board_col_idx, board_row_val in enumerate(board_row_vals):
            cell_val_pointers[board_row_val].append([len(boards) - 1, board_col_idx, board_row_idx])

    not_yet_completed_board_idxs = [i for i in range(len(boards))]

for draw_idx, draw_val in enumerate(all_draws):
    taken_draw_vals.append(draw_val)
    for cell_pointer in cell_val_pointers[draw_val]:
        if len(cell_pointer) > 0:
            board_idx = cell_pointer[0]
            val_col = cell_pointer[1]
            val_row = cell_pointer[2]
            # record draw
            boards_col_match_count[board_idx][val_col] += 1
            boards_row_match_count[board_idx][val_row] += 1
            if is_a_completion_draw(board_idx, val_col, val_row):
                # record winner
                completed_draw_idxs.append(draw_idx)
                completed_draw_vals.append(draw_val)
                if board_idx not in completed_board_idxs:
                    completed_board_idxs.append(board_idx)
                if board_idx in not_yet_completed_board_idxs:
                    not_yet_completed_board_idxs.remove(board_idx)
        if is_all_boards_complete():
            break
    if is_all_boards_complete():
        break

if len(completed_board_idxs) == 0:
    print(f'no winner')
    exit()

winning_board_idx = completed_board_idxs[0]
winning_board = boards[winning_board_idx]
winning_draw_val = completed_draw_vals[0]
winning_board_cell_sum = calculate_board_cell_sum(boards[winning_board_idx], winning_draw_val)
print(f'board {winning_board_idx + 1} is the winner after {winning_draw_val} was drawn')
print(f'\t with an cell sum of {winning_board_cell_sum} and final score of {winning_board_cell_sum * winning_draw_val}')

losing_board_idx = completed_board_idxs[len(completed_board_idxs) - 1]
losing_board = boards[losing_board_idx]
losing_draw_val = completed_draw_vals[len(completed_board_idxs) - 1]
losing_board_cell_sum = calculate_board_cell_sum(losing_board, losing_draw_val)
print(f'board {losing_board_idx + 1} is the last winner after {losing_draw_val} was drawn')
print(f'\t with an cell sum of {losing_board_cell_sum} and final score of {losing_board_cell_sum * losing_draw_val}')
