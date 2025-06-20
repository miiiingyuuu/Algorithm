import sys


input = sys.stdin.readline


'''
dp[i] = i장을 구매할 때 쓸 수 있는 최소비용
'''


def solve():
    dp = [0] + prices[:]

    for i in range(1, n + 1): # 카드 i개를 구매할때
        for j in range(1, i + 1):   # 카드 j개를 이용해서 구매하는 경우
            dp[i] = min(dp[i], dp[i - j] + prices[j - 1])

    return dp[n]


n = int(input())
prices = list(map(int, input().split()))

print(solve())
