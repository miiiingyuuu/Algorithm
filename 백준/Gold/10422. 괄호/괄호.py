import sys

input = sys.stdin.readline


'''
문자열의 길이가 주어졌을때, 해당 문자 길이에 맞는 괄호 문자열은 몇개가 있을지 맞추는 문제
일단 문자열의 길이가 홀수면은 괄호의 짝수가 안맞으니까 안되겠지?
배열의 2n인 경우로 생각하여 2500개의 배열에 대해서 dp를 계산 (카탈란 수 활용)
'''


def solve():
    # 2*i의 경우의 수를 dp 점화식을 이용해서 계산하기
    for i in range(1, 2501):
        for j in range(i):
            dp[i] = dp[i] + dp[j] * dp[i - 1 - j]
        dp[i] %= MOD


t = int(input())
MOD = 1000000007

dp = [0] * (2501)   # 짝수만 가능하므로 가능한 갯수 2500개 -> dp[i]: 2*i의 괄호 문자열이 가능한 갯수
dp[0] = 1

solve()

for tc in range(t):
    n = int(input())
    # 문자열의 길이가 홀수면은 될 수가 없음
    if n % 2 != 0:
        print(0)
    else:
        print(dp[n // 2])
