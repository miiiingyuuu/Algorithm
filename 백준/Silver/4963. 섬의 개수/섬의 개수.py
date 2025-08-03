import sys
from collections import deque

input = sys.stdin.readline


def solve(m, n, curr_board):
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    q = deque()

    for i in range(n):
        for j in range(m):
            if curr_board[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                q.append((i, j))

                while q:
                    x, y = q.popleft()

                    for d in range(8):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and curr_board[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

                cnt += 1

    return cnt


dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = [list(map(int, input().split())) for _ in range(h)]

    print(solve(w, h, board))
