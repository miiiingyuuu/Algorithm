import sys
from collections import deque
input = sys.stdin.readline


def solve():
    # 3차원 graph로 방문표시: visited[행][열][벽 부순 횟수]
    visited = [[[False] * (k+1) for _ in range(m)] for _ in range(n)]
    q = deque()

    # q(x, y, 부순 벽 수, 거리)
    q.append((0, 0, 0, 1))
    visited[0][0][0] = True

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y, wall_cnt, ans = q.popleft()

        # 목적지 도착
        if x == n-1 and y == m-1:
            return ans

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아닐 경우
                if board[nx][ny] == 0 and not visited[nx][ny][wall_cnt]:
                    visited[nx][ny][wall_cnt] = True
                    q.append((nx, ny, wall_cnt, ans + 1))

                # 벽이 있을 경우 + 아직 벽을 부술 수 있다면
                elif board[nx][ny] == 1 and wall_cnt < k and not visited[nx][ny][wall_cnt + 1]:
                    visited[nx][ny][wall_cnt + 1] = True
                    q.append((nx, ny, wall_cnt + 1, ans + 1))

    return -1


n, m, k = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

print(solve())