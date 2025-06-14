import sys

input = sys.stdin.readline

'''
인접한 칸끼리 가로 or 세로로 교환해보기
그 후 연속된 사탕의 수를 세보기
'''


def check(board):
    max_cnt = 1
    for i in range(n):
        # 행 검사
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1

        # 열 검사
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j - 1][i]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1

    return max_cnt


def solve(board):
    result = 0
    for i in range(n):
        for j in range(n):
            # 가로 바꾸기
            if j + 1 < n:
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                result = max(result, check(board))
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

            # 세로 바꾸기
            if i + 1 < n:
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                result = max(result, check(board))
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

    return result


n = int(input())
board = [list(input().strip()) for _ in range(n)]

print(solve(board))