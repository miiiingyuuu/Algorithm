import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
info = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    info[a].append(b)
    in_degree[b] += 1

result = []
q = deque()

for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    current = q.popleft()
    result.append(current)

    for i in info[current]:
        in_degree[i] -= 1

        if in_degree[i] == 0:
            q.append(i)

print(*result)