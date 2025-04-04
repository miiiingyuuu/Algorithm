import sys

input = sys.stdin.readline


def dfs(x, y, dist):
    global count
    # 도착지에 도달했고 거리가 정확히 K인 경우
    if x == 0 and y == C - 1:
        if dist == K:
            count += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and graph[nx][ny] == '.':
                visited[nx][ny] = True
                dfs(nx, ny, dist + 1)
                visited[nx][ny] = False


R, C, K = map(int, input().split())
graph = [list(input()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]

# 이동 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0

# 시작점: 왼쪽 아래
visited[R - 1][0] = True
dfs(R - 1, 0, 1)

print(count)