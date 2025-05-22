import sys

input = sys.stdin.readline

'''
i번째 잔을 마신느 경우:
1. i번째 잔을 마시지 않는 경우: dp[i-1]
2. i번째 잔은 마시고, i-1번째는 안마시는 경우: dp[i-2] + wine[i]
3. i번째와 i-1번째를 마시고, i-2를 마시지 않는 경우: dp[i-3] + wine[i-1] + wine[i]
'''


def solve():
    if n == 1:
        return wine[0]
    elif n == 2:
        return wine[0] + wine[1]
    else:
        dp = [0] * n

        dp[0] = wine[0]
        dp[1] = wine[0] + wine[1]
        dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])

        for i in range(3, n):
            dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

        return dp[-1]


n = int(input())
wine = [int(input()) for _ in range(n)]

print(solve())