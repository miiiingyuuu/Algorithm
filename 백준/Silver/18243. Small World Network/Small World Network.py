import sys
from collections import deque

input = sys.stdin.readline


def solve(now):
    visited = set()
    q = deque()

    visited.add(now)
    q.append((now, 0))  # 현재, 거리

    while q:
        curr, dist = q.popleft()
        if dist > 6:
            return False

        for node in graph[curr]:
            if node not in visited:
                visited.add(node)
                q.append((node, dist + 1))

    if len(visited) == N:
        return True
    else:
        return False


N, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

possible = True
for i in range(1, N+1):
    if not solve(i):
        possible = False
        break

if possible:
    print("Small World!")
else:
    print("Big World!")
