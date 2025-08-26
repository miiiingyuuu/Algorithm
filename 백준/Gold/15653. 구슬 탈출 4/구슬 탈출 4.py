import sys
from collections import deque

input = sys.stdin.readline

'''
구멍에 빨간 구슬이 들어가야 성공
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def move(x, y, dx, dy):
    cnt = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
        if board[x][y] == 'O':
            break

    return x, y, cnt


def solve(rx, ry, bx, by):
    visited = set()
    q = deque()

    visited.add((rx, ry, bx, by))
    q.append((rx, ry, bx, by, 0))   # 각 구슬 좌표, cnt

    while q:
        rx, ry, bx, by, cnt = q.popleft()

        for d in range(4):
            # 구슬이 동일 선상에 있을 때, 구슬이 같은 좌표에 있을 수 없기 때문에, 더 먼 거리를 간 구슬이 한 칸 덜 가야됨
            nrx, nry, rcnt = move(rx, ry, dx[d], dy[d])
            nbx, nby, bcnt = move(bx, by, dx[d], dy[d])

            # 파란 구슬이 구멍에 빠지면 실패
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬만 구멍에 들어가면 성공
            if board[nrx][nry] == 'O':
                return cnt + 1

            # 같은 위치에 있으면 이동 거리 비교해서 조정
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[d]
                    nry -= dy[d]
                else:
                    nbx -= dx[d]
                    nby -= dy[d]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, cnt + 1))

    return -1


N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

rx = ry = bx = by = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

print(solve(rx, ry, bx, by))
