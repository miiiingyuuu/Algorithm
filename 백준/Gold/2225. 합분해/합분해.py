import sys

input = sys.stdin.readline


def solve():
    dp = [[0] * (k+1) for _ in range(n+1)]  # dp[i][j]: 정수 j개를 사용해서 합이 i가 되는 경우의 수
    dp[0][0] = 1

    for i in range(n+1):
        for j in range(1, k+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

    return dp[n][k]


n, k = map(int, input().split())

print(solve())
