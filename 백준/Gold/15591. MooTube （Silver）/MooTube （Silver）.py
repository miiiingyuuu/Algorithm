import sys
from collections import deque
input = sys.stdin.readline


def solve(usado, k, start):
    visited = [False] * (n + 1)
    visited[start] = True

    cnt = 0

    q = deque([(start, float('inf'))])

    while q:
        node, min_val = q.popleft()

        for neighbor, usado_val in usado[node]:
            if not visited[neighbor]:
                new_min_val = min(min_val, usado_val)

                if new_min_val >= k:
                    visited[neighbor] = True
                    cnt += 1
                    q.append((neighbor, new_min_val))

    return cnt


n, m = map(int, input().split())
usado = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    p, q, r = (map(int, input().split()))
    usado[p].append((q, r))
    usado[q].append((p, r))

for _ in range(m):
    k, v = map(int, input().split())
    print(solve(usado, k, v))