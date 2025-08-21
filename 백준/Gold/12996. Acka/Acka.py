import sys

input = sys.stdin.readline

'''
노래를 부를 수 있는 경우는: 혼자(3) + 듀엣(3) + 트리오(1)로 7가지
4차원 배열 dp로 문제를 해결하면 될 듯
'''


def solve():
    MOD = 1000000007

    # dp[s][d][k][h]: s개의 곡을 부를 때, d개의 곡, k의 곡, h의 곡을 불렀을 때의 앨범 개수
    dp = [[[[0] * (H+1) for _ in range(K+1)] for _ in range(D+1)] for _ in range(S+1)]

    dp[0][0][0][0] = 1

    for s in range(1, S+1):
        for d in range(D+1):
            for k in range(K+1):
                for h in range(H+1):
                    val = 0
                    if d > 0:
                        val += dp[s-1][d-1][k][h]   # dotorya
                    if k > 0:
                        val += dp[s-1][d][k-1][h]   # kesakiyo
                    if h > 0:
                        val += dp[s-1][d][k][h-1]   # hongjun
                    if d > 0 and k > 0:
                        val += dp[s-1][d-1][k-1][h] # dotorya + kesakiyo
                    if d > 0 and h > 0:
                        val += dp[s-1][d-1][k][h-1] # dotorya + kesakiyo
                    if k > 0 and h > 0:
                        val += dp[s-1][d][k-1][h-1] # kesakiyo + hongjun
                    if d > 0 and k > 0 and h > 0:
                        val += dp[s-1][d-1][k-1][h-1]   # dotorya + kesakiyo + hongjun

                    dp[s][d][k][h] = val % MOD

    return dp[S][D][K][H]


S, D, K, H = map(int, input().split())

print(solve())
