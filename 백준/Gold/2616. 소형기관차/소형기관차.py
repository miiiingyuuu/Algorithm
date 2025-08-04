import sys

input = sys.stdin.readline

'''
소형 기관차 3대로 최대로 실을 수 있는 인원 수 3*max_hold
dp[i][j]: i번째 소형 기관차가 j번째 객차까지 고려했을 때의 최대 승객의 수
dp[3][n]를 하면 우리가 원하는 3개의 소형 기관차를 썼을 때의 n번째 객차까지 고려했을 때의 최대 승객의 수
'''


def solve():
    # 누적합 구하기
    p_sum = [0] * (n+1)
    for i in range(n):
        p_sum[i+1] = p_sum[i] + passengers[i]

    # dp[i][j]: i번째 소형 기관차가 j번째 객차까지 고려했을 때의 최대 승객의 수
    dp = [[0] * (n+1) for _ in range(4)]

    for i in range(1, 4):
        for j in range(max_hold, n+1):
            # 현재 소형기관차에서 j번째 객차를 포함하지 않은 경우(앞에서 이미 max_hold까지 쓴 최대값) or j번째 객차를 포함하여 새로 max_hold까지 실어보는 경우
            dp[i][j] = max(dp[i][j-1], dp[i-1][j - max_hold] + p_sum[j] - p_sum[j - max_hold])

    return dp[3][n]


n = int(input())
passengers = list(map(int, input().split()))
max_hold = int(input())

print(solve())
