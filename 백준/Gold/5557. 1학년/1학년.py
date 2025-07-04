import sys

input = sys.stdin.readline


'''
중간에 계산하는 과정에서 음수가 나오거나 20이 넘는 수가 되면 안된다
숫자가 주어졌을 때, 만들 수 있는 올바른 등식의 수를 구하는 방법의 수
dp[i][j] = i번째 숫자까지 계산했을 때 결과가 j가 되는 경우의 수(0 <= j <= 20)
'''


def solve():
    # dp[i][j] = i번째 숫자까지 계산했을 때 결과가 j가 되는 경우의 수(0 <= j <= 20)
    dp = [[0] * 21 for _ in range(n - 1)]

    # nums의 첫번째 숫자로 시작
    dp[0][nums[0]] = 1

    # 마지막 숫자는 계산에 포함이 되지 않으므로 제외
    for i in range(1, n-1):
        for j in range(21):
            if dp[i-1][j] != 0:
                plus = j + nums[i]
                minus = j - nums[i]
                if 0 <= plus <= 20:
                    dp[i][plus] += dp[i-1][j]
                if 0 <= minus <= 20:
                    dp[i][minus] += dp[i-1][j]

    return dp[n-2][nums[-1]]


n = int(input())
nums = list(map(int, input().split()))

print(solve())
