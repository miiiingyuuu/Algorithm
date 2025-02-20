import sys
from collections import deque
input = sys.stdin.readline


def bfs(board):
    visited = [[False] * M for _ in range(N)]
    q = deque([(0, 0)])
    visited[0][0] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        board[x][y] = 2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] != 1:
                visited[nx][ny] = True
                q.append((nx, ny))


def solve():
    time = 0

    while True:
        cheese_exists = False
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    cheese_exists = True
                    break
            if cheese_exists:
                break

        if not cheese_exists:
            return time

        bfs(board)

        melting = []
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for x in range(N):
            for y in range(M):
                if board[x][y] == 1:
                    cnt = 0
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 2:
                            cnt += 1
                    if cnt >= 2:
                        melting.append((x, y))

        for x, y in melting:
            board[x][y] = 0

        for i in range(N):
            for j in range(M):
                if board[i][j] == 2:
                    board[i][j] = 0

        time += 1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

print(solve())