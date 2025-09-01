import sys

input = sys.stdin.readline


def solve():
    # dp[i]: i원을 제출하기 위한 최소 동전 개수
    dp = [float('inf')] * (N+1)
    dp[0] = 0   # 0원 나타내는 방법은 없음

    for i in range(1, N+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[N]


N = int(input())
coins = [1, 2, 5, 7]

print(solve())
