import sys

input = sys.stdin.readline


def solve():
    # i번째 앱에서 비용 j로 확보할 수 있는 최대 메모리를 구하는 dp
    dp = [[-1] * total_cost for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n+1):
        app_memory = activated[i-1]
        app_cost = cost[i-1]

        for j in range(total_cost):
            # i번째 앱을 비활성화하지 않는 경우
            dp[i][j] = dp[i-1][j]

            # i번째 앱을 비활성화하는 경우
            if j >= app_cost and dp[i-1][j-app_cost] != -1:
                freed_memory = dp[i-1][j-app_cost] + app_memory
                if dp[i][j] == -1 or freed_memory > dp[i][j]:
                    dp[i][j] = freed_memory

    for k in range(total_cost):
        if dp[n][k] >= m:
            return k

    return -1


n, m = map(int, input().split())
activated = list(map(int, input().split()))
cost = list(map(int, input().split()))

total_cost = sum(cost) + 1

print(solve())