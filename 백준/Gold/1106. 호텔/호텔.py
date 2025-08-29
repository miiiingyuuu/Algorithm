import sys

input = sys.stdin.readline


'''
적어도 C명의 고객을 늘리기 위해 투자해야하는 돈의 최소값?
'''


def solve():
    # dp[i] = i명의 고객을 얻기 위해 사용할 수 있는 돈의 최소 비용 -> 적어도 C명을 늘려야 하므로 여유있게 C + 100 만큼 계산하면 되지 않을까?
    max_customer = C + 100
    dp = [float('inf')] * (max_customer+1)
    dp[0] = 0

    for cost, customer in cities:
        for i in range(customer, max_customer + 1):
            dp[i] = min(dp[i], dp[i - customer] + cost)

    return min(dp[C:max_customer + 1])  # 적어도 C명이기 때문에, C ~ max_customer 중에 최소 비용 찾기


C, N = map(int, input().split())    # C: 목표 고객 수, N: 도시의 개수
cities = [list(map(int, input().split())) for _ in range(N)] # 홍보에 드는 비용, 얻을 수 있는 고객 수

print(solve())
