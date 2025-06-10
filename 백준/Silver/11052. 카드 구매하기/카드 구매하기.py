import sys

input = sys.stdin.readline

'''
dp[i]: 카드 i장을 살때 지불 할 수 있는 최대값 저장
그 이후에 내가 원하는 n장에 대한 dp[n]을 return
'''


def solve():
    dp = [0] + card_prices[:]

    for i in range(1, n + 1):  # 카드 i개를 구매해야할때
        for j in range(1, i + 1):  # j개짜리 팩을 사용해서 구매하는 경우
            dp[i] = max(dp[i], dp[i - j] + card_prices[j - 1])

    return dp[n]


n = int(input())
card_prices = list(map(int, input().split()))

print(solve())
