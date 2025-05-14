import sys
from collections import deque
input = sys.stdin.readline


# bfs로 시작지점에서 cnt를 센 이후, bfs로 모두 연결되어 있는 빙산의 갯수를 셀 수 있음
def solve():
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0 and not visited[i][j]:
                cnt += 1
                q = deque()
                q.append((i, j))
                visited[i][j] = True

                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if iceberg[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))

    return cnt


# 하나의 (i, j)마다 계산을 할 수 없으므로 따로 녹을 melt 배열을 구해서 빼기
def melt():
    iceberg_melt = [[0] * m for _ in range(n)]

    # (i, j) 4방향의 0 갯수 세기
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0:
                zero_cnt = 0
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if 0 <= ni < n and 0 <= nj < m:
                        if iceberg[ni][nj] == 0:
                            zero_cnt += 1
                iceberg_melt[i][j] = zero_cnt

    # 0 갯수 만큼 해당 (i, j) 녹이기
    for i in range(n):
        for j in range(m):
            # 차가 음수가 되는 경우를 방지해서 음수일 경우에는 0
            iceberg[i][j] = max(0, iceberg[i][j] - iceberg_melt[i][j])


n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 두 덩이가 될때까지 빙산 갯수 세고 -> 녹이고 반복
ans = 0
while True:
    tmp = solve()
    if tmp == 0:
        print(0)
        break
    if tmp >= 2:
        print(ans)
        break
    melt()
    ans += 1