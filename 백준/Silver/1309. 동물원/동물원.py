import sys

input = sys.stdin.readline

'''
dp[i][j]: i번째 칸에
j: 0 -> 사자를 놓지 않음
j: 1 -> 왼쪽(위칸)에 사자를 놓음
j: 2 -> 오른쪽(아랫칸)에 사자를 놓음
이전 칸에 사자를 어떻게 배치했는지에 따라 다음 칸의 배치 가능성이 달라짐
'''


def solve():
    dp = [[0] * 3 for _ in range(n+1)]

    dp[1][0] = 1    # 사자 없음
    dp[1][1] = 1    # 왼쪽에 사자
    dp[1][2] = 1    # 오른쪽에 사자

    for i in range(2, n + 1):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD # i번째 사자를 놓지 않는 경우 = i-1번째의 모든 경우
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD  # i번쨰 왼쪽에 놓는 경우 = i-1번째에 안놓은 경우 + i-1번째 오른쪽에 놓은 경우
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD  # 아래에 사자가 있는 경우 = i-1번째에 안놓은 경우 + i-1번째 왼쪽에 놓은 경우

    return (dp[n][0] + dp[n][1] + dp[n][2]) % MOD


n = int(input())
MOD = 9901

print(solve())
