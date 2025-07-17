import sys
from collections import deque

input = sys.stdin.readline


def solve(start, end):
    x, y = start
    tx, ty = end

    visited = set()
    visited.add((x, y))

    q = deque()
    q.append((x, y, 0))    # 시작 위치, cnt

    while q:
        x, y, cnt = q.popleft()
        
        if x == tx and y == ty:
            return cnt

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, cnt + 1))

    return -1


dx = [-1, -2, -1, -2, 1, 2, 2, 1]
dy = [-2, -1, 2, 1, 2, 1, -1, -2]

t = int(input())
for tc in range(t):
    n = int(input())
    now = map(int, input().split())
    tar = map(int, input().split())
    print(solve(now, tar))
