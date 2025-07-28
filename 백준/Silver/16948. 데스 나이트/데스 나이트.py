import sys
from collections import deque

input = sys.stdin.readline


def solve():
    visited = set()

    q = deque()
    q.append((r1, c1, 0))   # r, c, cnt

    while q:
        r, c, cnt = q.popleft()

        if r == r2 and c == c2:
            return cnt

        for d in range(6):
            nr = r + directions[d][0]
            nc = c + directions[d][1]

            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, cnt + 1))

    return -1


n = int(input())
r1, c1, r2, c2 = map(int, input().split())

directions = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

print(solve())
