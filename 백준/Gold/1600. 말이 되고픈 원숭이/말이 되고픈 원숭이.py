import sys
from collections import deque
input = sys.stdin.readline


def solve():
    visited = [[[False] * (k+1) for _ in range(w)] for _ in range(h)]
    q = deque()
    q.append((0, 0, 0, 0))  # x, y, horse_moves 횟수, 총 이동 횟수
    visited[0][0][0] = True # x, y 위치에 hore_moves k번을 채웠는가?

    while q:
        r, c, k_cnt, cnt = q.popleft()
        if r == h-1 and c == w-1:
            return cnt

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w:
                if graph[nr][nc] == 0 and not visited[nr][nc][k_cnt]:
                    visited[nr][nc][k_cnt] = True
                    q.append((nr, nc, k_cnt, cnt+1))

        if k_cnt < k:
            for dr, dc in horse_moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w:
                    if graph[nr][nc] == 0 and not visited[nr][nc][k_cnt+1]:
                        visited[nr][nc][k_cnt+1] = True
                        q.append((nr, nc, k_cnt+1, cnt+1))

    return -1


k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

horse_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print(solve())