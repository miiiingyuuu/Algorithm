import sys
from collections import deque
input = sys.stdin.readline


def turn(dir, order):
    if order == 'L':
        return (dir - 1) % 4
    else:
        return (dir + 1) % 4


def solve():
    board = [[0] * n for _ in range(n)]

    for x, y in apples:
        board[x][y] = 1

    # q: 뱀이 있는 위치를 표현
    q = deque()
    q.append((0, 0))
    time = 0
    dir = 0

    x, y = 0, 0

    while True:
        time += 1
        nx = x + dx[dir]
        ny = y + dy[dir]

        # 벽 또는 자기자신과 충돌하면 끝
        if nx < 0 or ny < 0 or nx >= n or ny >= n or (nx, ny) in q:
            return time

        # 사과가 있다면
        if board[nx][ny] == 1:
            board[nx][ny] = 0
            q.appendleft((nx, ny))  # 머리 늘리기
        else:
            q.appendleft((nx, ny))
            q.pop() # 꼬리 줄이기

        x, y = nx, ny

        if time in direction_info:
            dir = turn(dir, direction_info[time])


n = int(input())    # 보드 크기
k = int(input())    # 사고의 갯수
apples = [list(map(lambda x: int(x)-1, input().split())) for _ in range(k)]    # 사과의 위치
l = int(input())    # 뱀의 방향 변환 횟수
info = []
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))
direction_info = dict(info)

# 방향 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

print(solve())