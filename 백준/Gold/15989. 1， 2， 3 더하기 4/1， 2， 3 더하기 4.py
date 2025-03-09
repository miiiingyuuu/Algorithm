import sys

input = sys.stdin.readline


def solve(n):
    dp = [0] * (n + 1)

    dp[0] = 1

    for i in [1, 2, 3]:
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]


T = int(input())
for _ in range(T):
    n = int(input())
    print(solve(n))