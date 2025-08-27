import sys

input = sys.stdin.readline


'''
모든 노래를 추가해야 함
같으 노래를 추가하려면 두 노래 사이에 최소 M개의 곡이 있어야 함
만들 수 있는 플레이리스트의 경우의 수? -> 새로운 곡을 추가하냐 vs 이미 사용한 곡을 추가를 할 것 인가(-M) 이후에 가능
'''

MOD = 1000000007


def solve():
    # dp[i][j]: i개의 곡으로 이뤄졌을 때, j개의 서로 다른 곡이 포함된 경우
    dp = [[0] * (N+1) for _ in range(P+1)]
    dp[0][0] = 1

    for i in range(1, P+1):
        for j in range(1, N+1):
            # 새로운 곡 추가
            dp[i][j] += dp[i-1][j-1] * (N - (j-1))
            dp[i][j] %= MOD

            # 이미 사용한 곡 추가(해당 곡 사이에 M개의 곡이 있어야 함)
            if j > M:
                dp[i][j] += dp[i-1][j] * (j - M)
                dp[i][j] %= MOD

    return dp[P][N]


N, M, P = map(int, input().split()) # N: 노래 수, M: 존재해야 하는 곡 수, P: 들으려는 노래 수

print(solve())
