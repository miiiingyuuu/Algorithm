import sys
from collections import deque
input = sys.stdin.readline


def solve(maze):
    start_r, start_c = 0, 0
    for i in range(N):
        for j in range(M):
            if maze[i][j] == '0':
                start_r, start_c = i, j
                break

    q = deque([(start_r, start_c, 0, 0)])
    visited = set([(start_r, start_c, 0)])

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c, keys, ans = q.popleft()

        if maze[r][c] == '1':
            return ans

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < M:
                cell = maze[nr][nc]

                if cell == '#':
                    continue

                if 'A' <= cell <= 'F':
                    key_bit = ord(cell) - ord('A')
                    if not (keys & (1 << key_bit)):
                        continue

                new_keys = keys
                if 'a' <= cell <= 'f':
                    key_bit = ord(cell) - ord('a')
                    new_keys |= (1 << key_bit)

                now = (nr, nc, new_keys)
                if now not in visited:
                    visited.add(now)
                    q.append((nr, nc, new_keys, ans + 1))

    return -1


N, M = map(int, input().split())
maze = [input() for _ in range(N)]

print(solve(maze))