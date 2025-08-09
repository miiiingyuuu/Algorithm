import sys

input = sys.stdin.readline

'''
오른쪽 -> 왼쪽으로 갔을 때의 최대값 vs 왼쪽 -> 오른쪽으로 갔을때의 최대값 비교 (각 행에서, 위쪽으로는 다시 못올라감)
'''


def solve():
    # dp[i][j]: (i, j)가 가질 수 있는 최대값
    dp = [[-101] * M for _ in range(N)]

    dp[0][0] = board[0][0]

    # 첫 행은 오른쪽으로만 갈 수 있음
    for l in range(1, M):
        dp[0][l] = dp[0][l-1] + board[0][l]

    for i in range(1, N):
        left_dp = [-101] * M
        right_dp = [-101] * M

        # 왼쪽 -> 오른쪽
        left_dp[0] = dp[i-1][0] + board[i][0]
        for j in range(1, M):
            left_dp[j] = max(left_dp[j-1], dp[i-1][j]) + board[i][j]

        # 오른쪽 -> 왼쪽
        right_dp[M-1] = dp[i-1][M-1] + board[i][M-1]
        for j in range(M-2, -1, -1):
            right_dp[j] = max(right_dp[j+1], dp[i-1][j]) + board[i][j]

        # 두 방향 중 최대값 선택
        for j in range(M):
            dp[i][j] = max(left_dp[j], right_dp[j])

    return dp[N-1][M-1]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, -1), (0, 1), (1, 0)]

print(solve())
