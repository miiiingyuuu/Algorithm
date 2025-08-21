import sys

input = sys.stdin.readline

'''
처음에는 x1, x2, y1, y2를 -1씩 해서 board 크기에 맞게 정답을 구하려 했는데,
점화식이 그렇게 해버리니 범위 밖으로 나가서 0행 0열을 만들어줘야했다...
이렇게 하니 코드가 훨씬 깔끔하네
'''


def solve(x1, y1, x2, y2):
    return dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

# dp[i][j]: (0, 0)에서 (i, j)까지의 사람 수의 합
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + board[i - 1][j - 1] - dp[i - 1][j - 1]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    print(solve(x1, y1, x2, y2))
