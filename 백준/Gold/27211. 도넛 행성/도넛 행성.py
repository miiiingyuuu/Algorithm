import sys
from collections import deque
input = sys.stdin.readline

def bfs(N, M, grid):
    visited = [[0] * M for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and grid[i][j] == 0:
                q = deque([(i, j)])
                visited[i][j] = 1
                ans += 1

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = (x + dx[k]) % N
                        ny = (y + dy[k]) % M

                        if not visited[nx][ny] and grid[nx][ny] == 0:
                            visited[nx][ny] = 1
                            q.append((nx, ny))

    return ans


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

print(bfs(N, M, grid))