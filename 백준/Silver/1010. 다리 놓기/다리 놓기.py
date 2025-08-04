import sys

input = sys.stdin.readline


dp = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    dp[1][i] = i
    dp[i][i] = 1

for i in range(2, 31):
    for j in range(i+1, 31):
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]


t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])
