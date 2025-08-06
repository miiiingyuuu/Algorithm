import sys
import copy
from itertools import permutations

input = sys.stdin.readline

'''
order가 가능한 순열에 따라 값이 다르게 나온다 했으므로 순열을 통해
board를 deepcopy하여 각 케이스마다 나오는 board의 행의 값 중 최소값을 게속 갱신
'''


def solve(x, y, s, tmp_board):
    for layer in range(1, s+1):
        top = x - layer
        left = y - layer
        bottom = x + layer
        right = y + layer

        prev = tmp_board[top][left]

        # 왼쪽 -> 위쪽
        for i in range(top, bottom):
            tmp_board[i][left] = tmp_board[i+1][left]
        # 아래 -> 왼쪽
        for i in range(left, right):
            tmp_board[bottom][i] = tmp_board[bottom][i+1]
        # 오른쪽 -> 아래
        for i in range(bottom, top, -1):
            tmp_board[i][right] = tmp_board[i-1][right]
        # 위쪽 -> 오른쪽
        for i in range(right, left + 1, -1):
            tmp_board[top][i] = tmp_board[top][i-1]

        tmp_board[top][left+1] = prev



N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
orders = [list(map(int, input().split())) for _ in range(K)]

min_val = float('inf')
for order in permutations(orders):
    tmp_board = copy.deepcopy(board)
    for r, c, s in order:
        solve(r-1, c-1, s, tmp_board)
    row_sums = [sum(row) for row in tmp_board]
    min_val = min(min_val, min(row_sums))

print(min_val)
