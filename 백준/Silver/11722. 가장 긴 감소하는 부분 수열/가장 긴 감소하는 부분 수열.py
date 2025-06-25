import sys

input = sys.stdin.readline


def solve():
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if a[i] < a[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


n = int(input())
a = list(map(int, input().split()))

print(solve())
