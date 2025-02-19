import sys
from collections import deque
input = sys.stdin.readline


def solve(N, M, board):
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(0, 0, 0)])

    while q:
        x, y, wall = q.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1 and wall == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))

                elif board[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))

    return -1


N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

print(solve(N, M, board))