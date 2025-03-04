import sys

input = sys.stdin.readline


def up(board):
    n = len(board)
    new_board = [[0] * n for _ in range(n)]

    for j in range(n):
        pos = 0
        for i in range(n):
            if board[i][j] == 0:
                continue

            if new_board[pos][j] == 0:
                new_board[pos][j] = board[i][j]

            elif new_board[pos][j] == board[i][j]:
                new_board[pos][j] *= 2
                pos += 1

            else:
                pos += 1
                new_board[pos][j] = board[i][j]

    return new_board


def down(board):
    n = len(board)
    new_board = [[0] * n for _ in range(n)]

    for j in range(n):
        pos = n - 1
        for i in range(n - 1, -1, -1):
            if board[i][j] == 0:
                continue

            if new_board[pos][j] == 0:
                new_board[pos][j] = board[i][j]
            elif new_board[pos][j] == board[i][j]:
                new_board[pos][j] *= 2
                pos -= 1
            else:
                pos -= 1
                new_board[pos][j] = board[i][j]

    return new_board


def left(board):
    n = len(board)
    new_board = [[0] * n for _ in range(n)]

    for i in range(n):
        pos = 0
        for j in range(n):
            if board[i][j] == 0:
                continue

            if new_board[i][pos] == 0:
                new_board[i][pos] = board[i][j]
            elif new_board[i][pos] == board[i][j]:
                new_board[i][pos] *= 2
                pos += 1
            else:
                pos += 1
                new_board[i][pos] = board[i][j]

    return new_board


def right(board):
    n = len(board)
    new_board = [[0] * n for _ in range(n)]

    for i in range(n):
        pos = n - 1
        for j in range(n - 1, -1, -1):
            if board[i][j] == 0:
                continue

            if new_board[i][pos] == 0:
                new_board[i][pos] = board[i][j]
            elif new_board[i][pos] == board[i][j]:
                new_board[i][pos] *= 2
                pos -= 1
            else:
                pos -= 1
                new_board[i][pos] = board[i][j]

    return new_board


def ans(board):
    return max(max(row) for row in board)


def dfs(board, depth):
    if depth == 5:
        return ans(board)

    max_value = 0

    moves = [up, down, left, right]
    for i in moves:
        new_board = i(board)

        if new_board != board:
            max_value = max(max_value, dfs(new_board, depth + 1))

    return max(max_value, ans(board))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(dfs(board, 0))