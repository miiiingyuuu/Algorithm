import sys
from collections import deque

input = sys.stdin.readline

'''
나이트, 비숍, 룩의 이동 방식은 각각 다름
해당 위치에서 위의 3말로 각각 움직이다가 안되면 교체하는 방식으로 가면 되지 않을까?
다음 번호로 넘어갈때는, 한 번에 가는게 아닌 다른 번호를 거쳤다가 가도 됨
행동은 말을 이동시키거나, 말을 바꾸기
'''

knights_dir = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1)]
bishop_dir = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
rook_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solve():
    # visited[x][y][horses][num]: 해당 좌표를 num과 horse와 함께 방문했는지 안했는지
    visited = [[[[False] * (N*N+1) for _ in range(3)] for _ in range(N)] for _ in range(N)]
    q = deque()
    start_x, start_y = pos[1]

    # 세 가지 말을 이용해서 bfs 하기
    for horse in range(3):
        visited[start_x][start_y][horse][1] = True
        q.append((start_x, start_y, horse, 1, 0))   # 좌표, 현재 말, num, time

    while q:
        x, y, horse, num, time = q.popleft()

        # 기저 조건
        if num == N*N:
            return time

        # 말 바꿔서 이동시켜보기
        for other in range(3):
            if other != horse and not visited[x][y][other][num]:
                visited[x][y][other][num] = True
                q.append((x, y, other, num, time+1))

        # 나이트, 비숍, 룩 일때 각각 다르게 이동시켜야 함
        if horse == 0:  # knight
            for dx, dy in knights_dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    # 가는 좌표가 내가 찾는 다음 번호의 좌표와 맞다면 번호 +1 하기
                    if (nx, ny) == pos[num+1]:
                        nxt_num = num + 1
                    else:
                        nxt_num = num

                    if not visited[nx][ny][horse][nxt_num]:
                        visited[nx][ny][horse][nxt_num] = True
                        q.append((nx, ny, horse, nxt_num, time + 1))

        elif horse == 1:    # bishop
            for dx, dy in bishop_dir:
                nx, ny = x, y
                while True:
                    nx += dx
                    ny += dy
                    if not (0 <= nx < N and 0 <= ny < N):
                        break

                    if (nx, ny) == pos[num+1]:
                        nxt_num = num + 1
                    else:
                        nxt_num = num

                    if not visited[nx][ny][horse][nxt_num]:
                        visited[nx][ny][horse][nxt_num] = True
                        q.append((nx, ny, horse, nxt_num, time + 1))

        elif horse == 2:    # rook
            for dx, dy in rook_dir:
                nx, ny = x, y
                while True:
                    nx += dx
                    ny += dy
                    if not (0 <= nx < N and 0 <= ny < N):
                        break

                    if (nx, ny) == pos[num + 1]:
                        nxt_num = num + 1
                    else:
                        nxt_num = num

                    if not visited[nx][ny][horse][nxt_num]:
                        visited[nx][ny][horse][nxt_num] = True
                        q.append((nx, ny, horse, nxt_num, time + 1))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 각 자리의 좌표 저장
pos = [None] * (N*N+1)
for i in range(N):
    for j in range(N):
        pos[board[i][j]] = (i, j)

print(solve())
