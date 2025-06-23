import sys

input = sys.stdin.readline

'''
1. dp[i][j] = i자리 오르막 수를 찾을 때 1의 자리 수가 j일 때의 오르막 수
2. 점화식 계산 결과: dp[i][j] = dp[i-1][j] + dp[i][j-1]
'''


def solve():
    dp = [[0] * 10 for _ in range(n+1)]

    for j in range(10):
        dp[1][j] = 1

    for i in range(2, n+1):
        dp[i][0] = dp[i-1][0]
        for j in range(1, 10):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

    return sum(dp[n]) % MOD


n = int(input())
MOD = 10007

print(solve())
