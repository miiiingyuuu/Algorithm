import sys
from collections import deque

input = sys.stdin.readline

'''
전에 이동한 방향으로는 또 갈 수 없고, C 두 곳에 모두 배달 완료해야 함
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solve(x, y, c_list):
    # visited[x][y][dir][curr_c]: dir 방향으로 들어와서, curr_c의 상태로 방문한 경우 체크
    visited = [[[[False] * (1 << 2) for _ in range(4)] for _ in range(M)] for _ in range(N)]
    q = deque()

    q.append((x, y, -1, 0, 0))  # 좌표, 이전에 간 방향(초기: -1), C 현황(0: 안함, 1: 첫 번째만, 2: 두 번째만, 3: 배달 완료), 시간

    while q:
        x, y, dir, curr_c, time = q.popleft()

        # 배달이 완료된 상태라면 == 3
        if curr_c == 3:
            return time

        for d in range(4):
            if d == dir:
                continue

            nx = x + dx[d]
            ny = y + dy[d]

            if not (0 <= nx < N and 0 <= ny < M) or board[nx][ny] == '#':
                continue

            new_c = curr_c
            for idx, (cx, cy) in enumerate(c_list):
                if nx == cx and ny == cy:
                    new_c |= (1 << idx)

            # 방문하지 않았거나, 더 많은 C를 배달했다면 갱신
            if not visited[nx][ny][d][new_c]:
                visited[nx][ny][d][new_c] = True
                q.append((nx, ny, d, new_c, time + 1))

    return -1


N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
c_list = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 'S':
            x, y = i, j
        elif board[i][j] == 'C':
            c_list.append((i, j))

print(solve(x, y, c_list))
