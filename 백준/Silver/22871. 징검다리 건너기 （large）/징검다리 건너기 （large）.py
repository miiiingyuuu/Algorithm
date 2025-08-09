import sys

input = sys.stdin.readline


def solve():
    INF = float('inf')
    
    dp = [INF] * N
    dp[0] = 0

    # dp[i] i번 돌까지 도달하는데 필요한 최소 K
    for i in range(1, N):
        for j in range(i):
            energy = (i-j) * (1 + abs(A[i] - A[j]))
            dp[i] = min(dp[i], max(dp[j], energy))

    return dp[N-1]


N = int(input())
A = list(map(int, input().split()))

print(solve())
