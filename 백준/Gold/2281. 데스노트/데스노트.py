import sys

input = sys.stdin.readline

'''
마지막을 최대한 많이 남기면 손해가 최소화임
마지막줄을 최대한 채우면서 반대로 올라가면 최소 제곱의 합이 나올듯?
'''


def solve():
    INF = float('inf')

    # dp[i]: i번째 사람부터 끝까지 적었을 때, 최소 제곱의 합(top-down 방식: 마지막 칸부터 채우기) -> 답은 dp[0]
    dp = [INF] * (n+1)
    dp[n] = 0

    for i in range(n-1, -1, -1):
        cur_line = 0
        for j in range(i, n):
            cur_line += length[j]
            # 한 줄에 들어가지 못하는 경우는 다음 줄로 넘어가기
            if cur_line > m:
                break

            # 마지막 줄은 계산 x
            if j == n-1:
                cost = 0
            else:
                cost = (m - cur_line) ** 2

            dp[i] = min(dp[i], cost + dp[j + 1])
            cur_line += 1

    return dp[0]


n, m = map(int, input().split())    # 이름 수, 가로의 폭
length = [int(input()) for _ in range(n)]

print(solve())
