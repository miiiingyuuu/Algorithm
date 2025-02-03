import sys

input = sys.stdin.readline


R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
alpha = set(graph[0][0])
ans = 1
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]

        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] not in alpha:
                alpha.add(graph[nx][ny])
                dfs(nx, ny, cnt+1)
                alpha.remove(graph[nx][ny])

dfs(0, 0, ans)
print(ans)