import sys
from collections import deque

input = sys.stdin.readline

'''
움직이거나, 칸에 머물 수 있음(머문 경우에도 횟수는 증가)
낮과 밤이 번갈아가면서 등장 -> 낮에만 벽을 부술 수 있음
가만히 있어야 이득을 보는 경우는? -> 벽을 부술 수 있지만, 밤인 경우
'''


def solve():
    visited = [[[False] * (k+1) for _ in range(m)] for _ in range(n)]   # visited[행][열][벽 부순 횟수]
    q = deque()

    q.append((0, 0, 0, 1))  # x, y, 부순 벽 수, 거리
    visited[0][0][0] = True

    while q:
        x, y, wall_cnt, ans = q.popleft()

        if x == n-1 and y == m-1:
            return ans

        now = ans % 2

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아닌 경우 그냥 가기
                if board[nx][ny] == 0 and not visited[nx][ny][wall_cnt]:
                    visited[nx][ny][wall_cnt] = True
                    q.append((nx, ny, wall_cnt, ans + 1))

                # 벽인 경우 아직 벽을 부술 수 있고 갈 수 있다면
                elif board[nx][ny] == 1 and wall_cnt < k and not visited[nx][ny][wall_cnt+1]:
                    # 낮이라면 부수고 가기
                    if now:
                        visited[nx][ny][wall_cnt+1] = True
                        q.append((nx, ny, wall_cnt + 1, ans + 1))
                    # 밤이고 주변에 벽이 있어서 기다릴 가치가 있을 때만 대기
                    else:
                        q.append((x, y, wall_cnt, ans + 1))

    return -1


n, m, k = map(int, input().split()) # k: 벽 부술 수 있는 횟수
board = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(solve())
