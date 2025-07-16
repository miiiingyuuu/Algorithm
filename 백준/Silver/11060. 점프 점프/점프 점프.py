import sys

input = sys.stdin.readline


'''
dp[n] -> i번째 칸에 도달하기 위한 최소 점수 횟수
'''


def solve():
    INF = float("inf")
    dp = [INF] * n
    dp[0] = 0

    for i in range(n):
        # 도달 못하거나 점프 불가한 경우는 넘기기
        if dp[i] == INF or lst[i] == 0:
            continue

        # 점프 가능한 범위 내에서 최소 점프 횟수 갱신
        for j in range(i + 1, i + lst[i] + 1):
            if j < n:
                dp[j] = min(dp[j], dp[i] + 1)

    return dp[n-1] if dp[n-1] != INF else -1


n = int(input())
lst = list(map(int, input().split()))

print(solve())
