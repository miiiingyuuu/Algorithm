import sys
from collections import deque
input = sys.stdin.readline


def solve(x, y, group_num):
    q = deque()
    q.append((x, y))
    visited[x][y] = group_num
    count = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = group_num
                    q.append((nx, ny))
                    count += 1

    return count


n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

result = [[0] * m for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

group_size = []
group_num = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 0인 곳을 기준으로 그룹화
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and visited[i][j] == -1:
            size = solve(i, j, group_num)
            group_size.append(size)
            group_num += 1

# 벽인 곳을 순회하며 결과 계산
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            around = set()
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < n and 0 <= nj < m:
                    g = visited[ni][nj]
                    if g != -1:
                        around.add(g)
            cnt = 1
            for g in around:
                cnt += group_size[g]
            result[i][j] = str(cnt % 10)
        else:
            result[i][j] = '0'

for row in result:
    print(''.join(row))