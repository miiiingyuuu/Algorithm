import sys
from collections import deque
input = sys.stdin.readline


def find_shark(grid):
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] == 9:
                return x, y


def get_edible_fish(grid, shark_size, n):
    fish = []
    for i in range(n):
        for j in range(n):
            if 0 < grid[i][j] < shark_size:
                fish.append((i, j))
    return fish


def get_distance(grid, start, end, shark_size, n):
    if start == end:
        return 0

    visited = [[False] * n for _ in range(n)]
    q = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, dist = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if grid[nx][ny] <= shark_size:
                    if nx == end[0] and ny == end[1]:
                        return dist + 1
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))

    return float('inf')


def solve(n, grid):
    time = 0
    shark_size = 2
    eaten_fish = 0
    shark_x, shark_y = find_shark(grid)
    grid[shark_x][shark_y] = 0

    while True:
        edible_fish = get_edible_fish(grid, shark_size, n)
        if not edible_fish:
            break

        distances = []
        for fish_x, fish_y in edible_fish:
            dist = get_distance(grid, (shark_x, shark_y), (fish_x, fish_y), shark_size, n)
            if dist != float('inf'):
                distances.append((dist, fish_x, fish_y))

        if not distances:
            break

        distances.sort()

        dist, fish_x, fish_y = distances[0]
        time += dist
        eaten_fish += 1
        grid[fish_x][fish_y] = 0

        shark_x, shark_y = fish_x, fish_y

        if eaten_fish == shark_size:
            shark_size += 1
            eaten_fish = 0

    return time


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

print(solve(n, grid))