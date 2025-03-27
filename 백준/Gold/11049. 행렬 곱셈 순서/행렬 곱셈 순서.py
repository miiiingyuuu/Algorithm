import sys

input = sys.stdin.readline


def solve(graph):
    # i부터 j까지의 행렬을 곱하는데 필요한 최소 곱셈 연산 횟수
    dp = [[0] * n for _ in range(n)]

    # 계산해야하는 체인 길이
    for i in range(n-1):
        # 시작 행렬
        for j in range(n-i-1):
            # 끝 행렬
            k = i+j+1

            dp[j][k] = float('inf')

            for l in range(j, k):
                dp[j][k] = min(dp[j][k], dp[j][l] + dp[l+1][k] + graph[j][0] * graph[l][1] * graph[k][1])

    return dp[0][-1]


n = int(input())
graph = [tuple(map(int, input().split())) for _ in range(n)]

print(solve(graph))