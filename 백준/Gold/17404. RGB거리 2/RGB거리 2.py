import sys

input = sys.stdin.readline


def solve():
    INF = 1e999999
    # dp[i][j][k] -> i : 현재 집, j : 현재 집의 색, k : 첫 집의 색
    dp = [[[INF for _ in range(3)] for _ in range(3)] for _ in range(n)]

    for i in range(3):
        dp[0][i][i] = rgbs[0][i]

    for i in range(1, n):
        for current_color in range(3):
            for first_color in range(3):
                for prev_color in range(3):
                    if prev_color != current_color:
                        if i == n-1 and current_color == first_color:
                            continue

                        dp[i][current_color][first_color] = min(dp[i][current_color][first_color], dp[i-1][prev_color][first_color] + rgbs[i][current_color])

    ans = INF
    for last_color in range(3):
        for first_color in range(3):
            if last_color != first_color:
                ans = min(ans, dp[n-1][last_color][first_color])

    return ans


n = int(input())
rgbs = [list(map(int, input().split())) for _ in range(n)]
print(solve())