import sys
from collections import deque
input = sys.stdin.readline


def bfs(room, start, end, h, w):
    visited = [[False] * w for _ in range(h)]
    q = deque([(start[0], start[1], 0)]) # (x, y, distance)
    visited[start[0]][start[1]] = True

    while q:
        x, y, dist = q.popleft()

        if x == end[0] and y == end[1]:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and room[nx][ny] != 'x':
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))

    return -1


def tsp(graph, start, n):
    dp = [[float('inf')] * n for _ in range(1 << n)]

    dp[1 << start][start] = 0

    for mask in range(1 << n):
        for pos in range(n):
            if dp[mask][pos] == float('inf'):
                continue

            for next_pos in range(n):
                if mask & (1 << next_pos):
                    continue

                next_mask = mask | (1 << next_pos)

                new_cost = dp[mask][pos] + graph[pos][next_pos]
                if new_cost < dp[next_mask][next_pos]:
                    dp[next_mask][next_pos] = new_cost

    all_visited = (1 << n) - 1
    min_cost = min(dp[all_visited])

    return min_cost if min_cost != float('inf') else -1


def solve(w, h, room):
    dirty = []

    for i in range(h):
        for j in range(w):
            if room[i][j] == 'o':
                start = (i, j)
            elif room[i][j] == '*':
                dirty.append((i, j))

    if not dirty:
        return 0

    points = [start] + dirty
    n = len(points)

    distances = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                dist = bfs(room, points[i], points[j], h, w)
                if dist == -1:
                    return -1
                distances[i][j] = dist

    return tsp(distances, 0, n)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = []

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    room = [list(input()) for _ in range(h)]
    print(solve(w, h, room))