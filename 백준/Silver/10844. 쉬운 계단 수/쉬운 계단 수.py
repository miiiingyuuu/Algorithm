import sys

input = sys.stdin.readline


n = int(input())
MOD = 10**9

dp = [[0] * 10 for _ in range(n+1)] # dp[n][j] = 길이가 n이고 마지막 숫자가 j인 계단 수 갯수

# 길이가 1일 때 1~9는 1개씩
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i-1][j-1]
        if j < 9:
            dp[i][j] += dp[i-1][j+1]
        dp[i][j] %= MOD

print(sum(dp[n]) % MOD)