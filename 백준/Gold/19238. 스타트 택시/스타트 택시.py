import sys
from collections import deque

input = sys.stdin.readline


'''
M명의 승객을 태우는 것이 목표
'''


# 고객의 목적지에 데려다 주기
def go(start, end, N, board):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    sx, sy = start
    ex, ey = end

    q.append((sx, sy))
    visited[sx][sy] = 0

    while q:
        x, y = q.popleft()
        if (x, y) == (ex, ey):
            return visited[x][y]

        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and board[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return -1


# 출발지에서 목적지까지 최단거리 계산
def solve(start, tar, N, board):
    q = deque()
    # 거리 및 방문 여부 표시할 배열
    visited = [[-1] * N for _ in range(N)]
    sx, sy = start

    q.append((sx, sy))
    visited[sx][sy] = 0

    found = []
    while q:
        x, y = q.popleft()
        if (x, y) in tar:
            found.append((visited[x][y], x, y))
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and board[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    if found:
        found.sort()
        return found[0]

    return None


N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(int, input().split())
tx, ty = tx - 1, ty - 1

passengers = dict()
starts = set()

for _ in range(M):
    a, b, c, d, = map(int, input().split())
    passengers[(a - 1, b - 1)] = (c - 1, d - 1)
    starts.add((a - 1, b - 1))

for _ in range(M):
    # 갈 수 있는 최단거리 찾기(고객 태우러 가기)
    result = solve((tx, ty), starts, N, board)
    if not result:
        print(-1)
        sys.exit()

    dist, px, py = result

    # 연료 부족이면 갈 수 없음
    if dist > fuel:
        print(-1)
        sys.exit()

    fuel -= dist
    tx, ty = px, py
    starts.remove((px, py))

    # 고객을 목적지로 이동
    ex, ey = passengers[(px, py)]
    dist2 = go((tx, ty), (ex, ey), N, board)
    if dist2 == -1 or dist2 > fuel:
        print(-1)
        sys.exit()

    fuel -= dist2
    fuel += dist2 * 2
    tx, ty = ex, ey

print(fuel)
