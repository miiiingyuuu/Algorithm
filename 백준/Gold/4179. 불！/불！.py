import sys
from collections import deque

input = sys.stdin.readline

'''
불의 확산을 담은 bfs를 먼저 해서 각 시간을 담고
J가 가는 곳을 bfs로 해보고 시간 안에 갈 수 있다면 탈출
'''


def solve():
    # 각 초 마다 움직이는 위치를 담을 행렬 2개
    j_time = [[-1] * c for _ in range(r)]
    fire_time = [[-1] * c for _ in range(r)]

    j_q = deque()
    fire_q = deque()

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'J':
                j_q.append((i, j))
                j_time[i][j] = 0
            elif board[i][j] == 'F':
                fire_q.append((i, j))
                fire_time[i][j] = 0

    # 불 확산
    while fire_q:
        x, y = fire_q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] != '#' and fire_time[nx][ny] == -1:
                    fire_time[nx][ny] = fire_time[x][y] + 1
                    fire_q.append((nx, ny))

    # J의 이동
    while j_q:
        x, y = j_q.popleft()

        if x == 0 or x == r - 1 or y == 0 or y == c - 1:
            return j_time[x][y] + 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] != '#' and j_time[nx][ny] == -1:
                    # 불보다 먼저 도착해야 함
                    if fire_time[nx][ny] == -1 or j_time[x][y] + 1 < fire_time[nx][ny]:
                        j_time[nx][ny] = j_time[x][y] + 1
                        j_q.append((nx, ny))

    return "IMPOSSIBLE"


r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]  # #: 벽, .: 지나갈 수 있는 공간, j: 초기 위치, f: 불이 난 공간

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

print(solve())