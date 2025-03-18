import sys

input = sys.stdin.readline


def is_valid(board, r, c, num):
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False

    start_r, start_c = (r // 3) * 3, (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_r + i][start_c + j] == num:
                return False

    return True


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def solve(board):
    empty = find_empty(board)

    if not empty:
        return True

    r, c = empty

    for num in range(1, 10):
        if is_valid(board, r, c, num):
            board[r][c] = num

            if solve(board):
                return True

            board[r][c] = 0

    return False


board = [list(map(int, input().strip())) for _ in range(9)]
solve(board)
for i in range(9):
    for j in range(9):
        print(board[i][j], end="")
    print()