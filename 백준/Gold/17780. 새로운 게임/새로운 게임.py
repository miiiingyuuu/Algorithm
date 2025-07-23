import sys
from collections import deque

input = sys.stdin.readline

'''
한 턴에 아래와 같이 이동
- 흰색: 그 칸으로 이동, 이미 말이 있는 경우 업히기
- 빨강: 순서를 반대로 뒤집기
- 파랑 or 범위 밖: 방향만 바꾸기
말이 4개 이상 쌓이면 게임 종료
'''


def reverse_directions(d):
    return [1, 0, 3, 2][d]


def solve():
    for turn in range(1, 1001):
        for i in range(k):
            x, y, d = horses[i]
            idx = board[x][y].index(i)  # i번째 말이 현재 칸에서 몇 번째인지

            # 가장 아래에 있는 말만 움직일 수 있음
            if idx != 0:
                continue

            moving = board[x][y][idx:]  # 움직이는 말 슬라이싱
            board[x][y] = board[x][y][:idx]  # 해당 칸의 남는 말 표시

            dx, dy = directions[d]
            nx, ny = x + dx, y + dy

            # 범위 밖이거나 파란색인 경우 방향만 뒤집기
            if not (0 <= nx < n and 0 <= ny < n) or colors[nx][ny] == 2:
                d = reverse_directions(d)
                horses[i][2] = d
                nx, ny = x + directions[d][0], y + directions[d][1]
                # 방향을 바꿔도 이동하지 못한다면 제자리 유지
                if not (0 <= nx < n and 0 <= ny < n) or colors[nx][ny] == 2:
                    board[x][y].extend(moving)
                    continue

            # 빨강인 경우 순서를 반대로 뒤집기
            if colors[nx][ny] == 1:
                moving.reverse()

            # 흰색인 경우 그냥 이동
            for m in moving:
                horses[m][0], horses[m][1] = nx, ny
            board[nx][ny].extend(moving)

            if len(board[nx][ny]) >= 4:
                return turn

    return -1


n, k = map(int, input().split())
colors = [list(map(int, input().split())) for _ in range(n)]  # 0: 흰색, 1: 빨강, 2: 파랑
board = [[[] for _ in range(n)] for _ in range(n)]  # 말 표시할 board

horses = []
for i in range(k):
    r, c, d = map(int, input().split())
    horses.append([r - 1, c - 1, d - 1])
    board[r - 1][c - 1].append(i)

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

print(solve())
