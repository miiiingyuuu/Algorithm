import sys

input = sys.stdin.readline


def solve():
    dp = [[0] * N for _ in range(N)]

    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            num = board[i][j]
            if num != 0 and dp[i][j] != 0:
                if j+num < N:
                    dp[i][j+num] += dp[i][j]
                if i+num < N:
                    dp[i+num][j] += dp[i][j]

    return dp[N-1][N-1]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(solve())
