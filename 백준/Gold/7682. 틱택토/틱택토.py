import sys

input = sys.stdin.readline


def check_winner(grid, player):
    for i in range(3):
        # 가로 세로 확인
        if all(grid[i][j] == player for j in range(3)):
            return True
        if all(grid[j][i] == player for j in range(3)):
            return True

    if all(grid[i][i] == player for i in range(3)):
        return True
    if all(grid[i][2 - i] == player for i in range(3)):
        return True

    return False


def solve(borad):
    grid = [[board[i * 3 + j] for j in range(3)] for i in range(3)]

    x_count = board.count('X')
    o_count = board.count('O')

    x_wins = check_winner(grid, 'X')
    o_wins = check_winner(grid, 'O')

    # x가 o보다 많아야 함
    if o_count > x_count or x_count > o_count+1:
        return False

    # 둘 다 동시 승리 불가능
    if x_wins and o_wins:
        return False

    # X가 이겼다면 x가 하나 더 많음
    if x_wins and x_count != o_count + 1:
        return False

    # O가 이겼다면 x와 o의 갯수 같음
    if o_wins and x_count != o_count:
        return False

    # 둘 다 이기지 못하는 경우
    if not x_wins and not o_wins and x_count + o_count < 9:
        return False

    return True


while True:
    board = input().strip()
    if board == 'end':
        break
    print('valid' if solve(board) else 'invalid')