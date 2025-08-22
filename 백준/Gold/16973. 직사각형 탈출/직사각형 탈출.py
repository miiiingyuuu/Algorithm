import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def solve():
    # 벽의 위치 찾기
    walls = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                walls.append((i, j))

    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    q = deque([(x, y, 0)])  # 좌표, 움직인 횟수

    while q:
        r, c, cnt = q.popleft()

        if r == tar_x and c == tar_y:
            return cnt

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 왼쪽 위의 점에서 이동할때 사각형이 이동하듯이 해당 범위 안에 벽이 있는지 체크
            if 0 <= nr < (N-h+1) and 0 <= nc < (M-w+1) and not visited[nr][nc]:
                min_r, max_r = nr, nr + h
                min_c, max_c = nc, nc + w
                move = True

                for wall_r, wall_c in walls:
                    if min_r <= wall_r < max_r and min_c <= wall_c < max_c:
                        move = False
                        break
                        
                if move:
                    visited[nr][nc] = True
                    q.append((nr, nc, cnt + 1))
        
    return -1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
h, w, x, y, tar_x, tar_y = map(int, input().split())
x -= 1
y -= 1
tar_x -= 1
tar_y -= 1

print(solve())
