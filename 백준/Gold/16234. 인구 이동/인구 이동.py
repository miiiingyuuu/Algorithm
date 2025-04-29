import sys
from collections import deque
input = sys.stdin.readline


def solve(x, y, visited):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append((x, y))
    visited[x][y] = True

    union = [(x, y)]
    population_sum = graph[x][y]

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[cx][cy] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union.append((nx, ny))
                    population_sum += graph[nx][ny]

    if len(union) > 1:
        new_population = population_sum // len(union)
        for x, y in union:
            graph[x][y] = new_population
        return True

    return False


n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = 0
while True:
    visited = [[False] * n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if solve(i, j, visited):
                    moved = True

    if not moved:
        break

    ans += 1

print(ans)
