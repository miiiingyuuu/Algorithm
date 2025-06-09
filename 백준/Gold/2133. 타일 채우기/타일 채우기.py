import sys

input = sys.stdin.readline

'''
3*n를 채우는 경우를 계산해보고 dp형태로 계산
홀수인 경우에는 완성이 불가능하니까 짝수인 경우에만 계산
'''


def solve():
    if n % 2 == 1:
        return 0

    dp = [0] * (n+1)

    dp[0] = 1
    dp[2] = 3

    # n=0:1(아무것도 없는 상태) n=2:3, n=4:(3*3)+2, n=6: (11*3)+(3*2)+2 ... dp[n] = dp[n-2] * 3 + dp[n-4] * 2 (n >= 4)
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3
        for j in range(0, i - 2, 2):
            dp[i] += dp[j] * 2

    return dp[n]


n = int(input())

print(solve())