import sys

input = sys.stdin.readline


'''
dp[n][last]: n의 합을 구하는데, 마지막으로 더한 수가 last(1, 2, 3)일 때의 경우의 수를 저장
이후 해당하는 dp[n][1], dp[n][2], dp[3]의 합을 MOD로 나누기
'''


def solve():
    # 선작업
    dp[1][1] = 1
    dp[2][2] = 1
    dp[3][3] = 1
    dp[3][2] = 1
    dp[3][1] = 1

    for i in range(4, 100001):
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD


t = int(input())
MOD = 1000000009

# dp[i][j]: 합이 i이고, 마지막에 더한 수가 j인 경우의 수
dp = [[0] * 4 for _ in range(100001)]

solve()

for _ in range(t):
    n = int(input())
    print((dp[n][1] + dp[n][2] + dp[n][3]) % MOD)
