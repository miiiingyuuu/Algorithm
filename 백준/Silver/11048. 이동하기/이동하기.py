import sys

input = sys.stdin.readline


'''
첫 행(오른쪽으로만 가능), 첫 열(위에서만 올 수 있음)을 제외하고 둘 째 행부터 얻을 수 있는 최대의 사탕의 양을 저장하면 되지 않을까?
-> 그렇게 하나씩 하는것보다 그냥 조건을 걸어서 2중 반복문 안에서 한번에 해결하는 것이 가능
'''


def solve():
    dp = board

    for r in range(n):
        for c in range(m):
            # board[0][0]은 그냥 그 자리 출발이니까 그 값을 그대로 유지하기 위해 조건 걸기
            if r == 0 and c == 0:
                continue

            # 매 칸을 조사할때 이전의 왼쪽, 왼쪽 대각 위, 위의 값을 더한 값을 비교해서 최대값을 갱신
            max_val = 0
            for d in range(3):
                nr = r - dr[d]
                nc = c - dc[d]
                if 0 <= nr < n and 0 <= nc < m:
                    if board[r][c] + dp[nr][nc] > max_val:
                        max_val = board[r][c] + dp[nr][nc]

            dp[r][c] = max_val

    return dp[n-1][m-1]


n, m = map(int, input().split())
board = [list(map(int ,input().split())) for _ in range(n)]

# 갈 수 있는 방향: 아래, 오른쪽, 대각 오른 아래
dr = [1, 0, 1]
dc = [0, 1, 1]

print(solve())
