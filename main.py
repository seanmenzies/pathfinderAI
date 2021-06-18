import sys
import random


# converts list of lists into a visually-friendly maze
def createboard(board):
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print(end='\n')


# find maze start
def find_start(board):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == 'O':
                return [x, y]
            else:
                continue
    print('Start point not found')
    sys.exit()


# inputs a string path, maps the path from the start and outputs the position after the final move
def find_start_point(board, path):
    x, y = find_start(board)
    for move in path:
        if move == 'L':
            x -= 1

        elif move == 'R':
            x += 1

        elif move == 'U':
            y -= 1

        elif move == 'D':
            y += 1

    return x, y


# checks if a given move is valid
def check_valid(board, x, y):
    # oops, outside of the maze
    if y not in range(0, len(board)) or x not in range(0, len(board[y])):
        return False
    # oops, hit a wall
    elif board[y][x] == '#':
        return False
    # yep, this move is fine
    else:
        return [y, x]


# check path is not doubling back
def path_by_coordinates(board, path):
    x, y = find_start(board)
    coordinates = [[x, y]]
    for move in path:
        if move == 'L':
            x -= 1
            coordinates.append([x, y])

        elif move == 'R':
            x += 1
            coordinates.append([x, y])

        elif move == 'U':
            y -= 1
            coordinates.append([x, y])

        elif move == 'D':
            y += 1
            coordinates.append([x, y])

    return coordinates


# check if goal has been reached
def find_end(board, x, y):
    if board[y][x] == 'X':
        return True
    else:
        return False


# iterate through path list and find next possible move for each path string
def find_poss_moves(board, paths):
    new_moves = []
    for path in paths:
        coordinates = path_by_coordinates(board, path)
        x, y = find_start_point(board, path)
        if not check_valid(board, x, y):
            paths.remove(path)
            continue
        else:
            # L
            x -= 1
            if not check_valid(board, x, y) or [x, y] in coordinates:
                x += 1
            else:
                new_moves.append(path + 'L')
                x += 1

            # R
            x += 1
            if not check_valid(board, x, y) or [x, y] in coordinates:
                x -= 1
            else:
                new_moves.append(path + 'R')
                x -= 1

            # U
            y -= 1
            if not check_valid(board, x, y) or [x, y] in coordinates:
                y += 1
            else:
                new_moves.append(path + 'U')
                y += 1

            # D
            y += 1
            if not check_valid(board, x, y) or [x, y] in coordinates:
                y -= 1
            else:
                new_moves.append(path + 'D')
                y -= 1

    return new_moves


def find_path(board):
    moves = ['L', 'R', 'D', 'U']
    # paths = []
    # update moves list with move + possible moves e.g. 'L' + 'L' and 'L' + 'R'
    # each string in the list will be one character longer than strings in previous list
    while True:
        paths_found = []
        if not moves:
            return False
        # loop breaks only if goal is reached and end == True
        end = False
        new_moves = find_poss_moves(board, moves)
        for path in new_moves:
            x, y = find_start_point(board, path)
            if find_end(board, x, y):
                paths_found.append(path)
                end = True
        moves = new_moves
        # paths.append(len(new_moves))
        if end:
            # print(max(paths))
            break
    return paths_found


# print paths found
def print_results(board, paths_found):
    print('1 path found:') if len(paths_found) == 1 else print(f'{len(paths_found)} paths found '
                                                               f'in {len(paths_found[0])} moves:')
    print(paths_found[0])
    # update maze to include path found
    coordinates = path_by_coordinates(board, paths_found[0])
    for coordinate in coordinates:
        x, y = list(map(str, coordinate))
        if board[int(y)][int(x)] != 'X' and board[int(y)][int(x)] != 'O':
            board[int(y)][int(x)] = 'o'
    createboard(board)


# generate board with randomly placed walls, starting and end points
def generate_board(size, difficulty=3):
    i = 0
    while True:
        i += 1
        board = []
        for _ in range(size):
            board.append([])
        for row in board:
            for _ in range(size):
                row.append(' ')
        randints = []
        for _ in range(int(difficulty/10*size**2)):
            while True:
                y = random.randint(0, size-1)
                x = random.randint(0, size-1)
                if [y, x] not in randints:
                    randints.append([y, x])
                    board[y][x] = '#'
                    break
        board[0][random.randint(0, size-1)] = 'O'
        board[size-1][random.randint(0, size-1)] = 'X'
        if find_path(board):
            print(f'{i} board/s tried')
            break
    return board


board2 = generate_board(25, difficulty=5)
createboard(board2)
findpath = find_path(board2)
print_results(board2, findpath)
