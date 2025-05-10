import sys

input = sys.stdin.readline


def solve():
    dp = [float('inf')] * (k+1) # 0 ~ k원을 만들기 위한 경우의 수 중 최소값을 저장하는 리스트
    dp[0] = 0   # 0원을 만드는 경우는 0개

    for coin in coins:
        for i in range(coin, k+1):
            # 0 ~ k원까지 해당하는 코인의 갯수는 i-coin 갯수의 + 1개 씩 늘어남
            dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[k] if dp[k] != float('inf') else -1


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

print(solve())