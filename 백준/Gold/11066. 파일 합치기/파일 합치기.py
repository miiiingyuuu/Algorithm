import sys

input = sys.stdin.readline


t = int(input())
for _ in range(t):
    k = int(input())
    cost = list(map(int, input().split()))

    # 누적합 계산
    prefix_sum = [0] * (k+1)
    for i in range(k):
        prefix_sum[i+1] = prefix_sum[i] + cost[i]

    # dp[i][j] : i~j까지 합치는 최소 비용
    dp = [[0] * k for _ in range(k)]

    # 구간 길이
    for l in range(2, k + 1):
        # 시작 인덱스
        for i in range(k - l + 1):
            # 끝 인덱스
            j = i + l - 1
            dp[i][j] = float('inf')
            # a: 분할점
            for a in range(i, j):
                cost_sum = prefix_sum[j + 1] - prefix_sum[i]
                dp[i][j] = min(dp[i][j], dp[i][a] + dp[a+1][j] + cost_sum)

    print(dp[0][k - 1])