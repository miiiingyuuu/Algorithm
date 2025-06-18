import sys


input = sys.stdin.readline

'''
dp[i] = 숫자 i를 제곱수의 합으로 표현할 때 필요한 최소 항의 개수
dp[1] = 1, dp[2] = 2, dp[3] = 3, dp[4] = 1, dp[5] = 2, dp[6] = 3, dp[7] = 4, dp[8] = 2, dp[9] = 1 ...
해당하는 i보다 작거나 같은 모든 제곱수 j*j를 뺀 후, 그 수를 만드는 최소 개수에 +1한 값 중 최소를 선택
'''


def solve():
    dp = [0] * (n+1)

    for i in range(1, n+1):
        min_cnt = float('inf')
        j = 1
        while j*j <= i:
            min_cnt = min(min_cnt, dp[i - j*j])
            j += 1
        dp[i] = min_cnt + 1

    return dp[n]


n = int(input())

print(solve())