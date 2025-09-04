import sys

input = sys.stdin.readline

'''
k가 있다면 나눠서 case1, case2로 나눠서 k까지 가는 경우의 수 * k에서 끝으로 가는 경우의 수 구하기
'''


def solve(start_r, start_c, end_r, end_c):
    # dp[i][j]: (i, j)로 가는 경로의 수
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[start_r][start_c] = 1

    for r in range(start_r, end_r + 1):
        for c in range(start_c, end_c + 1):
            if r == start_r and c == start_c:
                continue

            dp[r][c] = dp[r-1][c] + dp[r][c-1]

    return dp[end_r][end_c]


n, m, k = map(int, input().split())

if k == 0:
    print(solve(1, 1, n, m))
    sys.exit()

# k의 좌표
kr, kc = divmod(k-1, m)
kr += 1
kc += 1

case1 = solve(1, 1, kr, kc) # 시작 좌표 -> k로 가는 좌표
case2 = solve(kr, kc, n, m) # k 좌표 -> 끝으로 가는 좌표

print(case1 * case2)
