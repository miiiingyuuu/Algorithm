import sys
from collections import deque

input = sys.stdin.readline

'''
상어가 있는 곳을 기점으로 bfs를 돌려서 각 칸에 대해서 가까운 상어의 거리를 구할 수 있음
계산 후 가장 큰 값이 안전거리가 가장 큰 값
'''


def solve():
    visited = [[-1] * m for _ in range(n)]

    # 상어가 있는 곳을 0으로 처리, -1로 방문 여부 처리
    q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                q.append((i, j))
                visited[i][j] = 0

    while q:
        x, y = q.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    max_val = 0
    for i in range(n):
        for j in range(m):
            max_val = max(max_val, visited[i][j])

    return max_val


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

print(solve())
