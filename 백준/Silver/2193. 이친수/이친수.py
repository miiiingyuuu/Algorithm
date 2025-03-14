import sys

input = sys.stdin.readline


n = int(input())

# dp[i][j] = i자리 수 j(0 또는 1)로 끝나는 개수
dp = [[0, 0] for _ in range(n+1)]

dp[1][1] = 1
dp[1][0] = 0

for i in range(2, n+1):
    # i번째 자리에 0이 오는 경우
    dp[i][0] = dp[i-1][0] + dp[i-1][1]

    # i번째 자리에 1이 오는 경우
    dp[i][1] = dp[i-1][0]

print(dp[n][0] + dp[n][1])