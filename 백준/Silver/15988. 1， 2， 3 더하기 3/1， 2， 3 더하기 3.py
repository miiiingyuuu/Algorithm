import sys

input = sys.stdin.readline


t = int(input())

MOD = 1000000009
max_n = 1000001

dp = [0] * (max_n + 1)

dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_n):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

for _ in range(t):
    n = int(input())
    print(dp[n])
