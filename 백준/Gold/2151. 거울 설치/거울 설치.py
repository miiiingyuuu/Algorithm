import sys
import heapq
input = sys.stdin.readline


def solve():
    INF = 1e99999999
    dist = [[[INF for _ in range(4)] for _ in range(n)] for _ in range(n)]

    doors = []

    for i in range(n):
        for j in range(n):
            if house[i][j] == '#':
                doors.append((i, j))

    start_r, start_c = doors[0]
    end_r, end_c = doors[1]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    q = []

    for d in range(4):
        dist[start_r][start_c][d] = 0
        heapq.heappush(q, (0, start_r, start_c, d))

    while q:
        mirrors, r, c, d = heapq.heappop(q)

        if dist[r][c][d] < mirrors:
            continue

        nr, nc = r, c
        while True:
            nr += dr[d]
            nc += dc[d]

            if nr < 0 or nr >= n or nc < 0 or nc >= n or house[nr][nc] == '*':
                break

            if nr == end_r and nc == end_c:
                return mirrors

            if house[nr][nc] == '!':
                if dist[nr][nc][d] > mirrors:
                    dist[nr][nc][d] = mirrors
                    heapq.heappush(q, (mirrors, nr, nc, d))

                if d in [0, 2]:
                    new_dirs = [1, 3]
                else:
                    new_dirs = [0, 2]

                for new_d in new_dirs:
                    if dist[nr][nc][new_d] > mirrors + 1:
                        dist[nr][nc][new_d] = mirrors + 1
                        heapq.heappush(q, (mirrors + 1, nr, nc, new_d))

                break

    return -1


n = int(input())
house = [list(input().strip()) for _ in range(n)]
print(solve())