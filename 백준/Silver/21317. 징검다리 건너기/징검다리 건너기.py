import sys

input = sys.stdin.readline

'''
i -> i+1: 작은 점프
i -> i+2: 큰 점프
i -> i+3: 매우 큰 점프 (k 에너지 사용, 한 번 밖에 못 뜀)
dp[i][j]: i번째까지 오는데 최소 에너지 비용, j: 0-> 매우 큰 점프 사용하지 않고 도달, 1-> 매우 큰 점프를 한 번 사용하고 도달했을 경우
'''


def solve():
    INF = float('inf')
    dp = [[INF] * 2 for _ in range(N)]

    dp[0][0] = 0

    for i in range(N-1):
        # 작은 점프: i -> i+1
        if i + 1 < N:
            dp[i+1][0] = min(dp[i+1][0], dp[i][0] + jump_energy[i][0])
            dp[i+1][1] = min(dp[i+1][1], dp[i][1] + jump_energy[i][0])

        # 큰 점프: i -> i+2
        if i + 2 < N:
            dp[i+2][0] = min(dp[i+2][0], dp[i][0] + jump_energy[i][1])
            dp[i+2][1] = min(dp[i+2][1], dp[i][1] + jump_energy[i][1])

        # 매우 큰 점프(한 번만 가능): i -> i+3으로 가는데 매우 큰 점프를 사용하지 않은 상태여야 가능(dp[i][0]에 값이 있음)
        if i + 3 < N and dp[i][0] != INF:
            dp[i+3][1] = min(dp[i+3][1], dp[i][0] + K)

    return min(dp[N-1][0], dp[N-1][1])


N = int(input())
jump_energy = [list(map(int, input().split())) for _ in range(N-1)]   # 0: 작은 점프, 1: 큰 점프
K = int(input())

print(solve())
