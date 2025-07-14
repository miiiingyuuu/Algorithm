import sys

input = sys.stdin.readline


'''
첫 행(오른쪽으로만 가능), 첫 열(위에서만 올 수 있음)을 제외하고 둘 째 행부터 얻을 수 있는 최대의 사탕의 양을 저장하면 되지 않을까?
-> 그렇게 하나씩 하는것보다 그냥 조건을 걸어서 2중 반복문 안에서 한번에 해결하는 것이 가능
'''


def solve():
    dp = [[0] * (m+1) for _ in range(n+1)]

    for r in range(1, n+1):
        for c in range(1, m+1):
            dp[r][c] = max(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + board[r-1][c-1]

    return dp[n][m]


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(solve())
