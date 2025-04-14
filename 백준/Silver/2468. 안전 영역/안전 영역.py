import sys
from collections import deque
input = sys.stdin.readline


def solve(r, c, height):
    q = deque([(r, c)])
    visited[r][c] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > height and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


n = int(input())
board = []
h = set()
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    h.update(row)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_ans = 0

for height in sorted(list(h) + [0]):
    visited = [[False] * n for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] > height and not visited[i][j]:
                ans += 1
                solve(i, j, height)

    max_ans = max(max_ans, ans)

print(max_ans)