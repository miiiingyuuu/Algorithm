import sys
from collections import deque
input = sys.stdin.readline


def solve():
    info = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for i in graph:
        for j in range(1, len(i) - 1):
            singer1, singer2 = i[j], i[j+1]
            info[singer1].append(singer2)
            in_degree[singer2] += 1

    q = deque()

    for k in range(1, n + 1):
        if in_degree[k] == 0:
            q.append(k)

    result = []
    while q:
        current = q.popleft()
        result.append(current)

        for l in info[current]:
            in_degree[l] -= 1
            if in_degree[l] == 0:
                q.append(l)

    if len(result) < n:
        return [0]

    return result


n, m = map(int, input().split())
graph = []

for _ in range(m):
    orders = list(map(int, input().split()))
    k = orders[0]
    graph.append(orders)

result = solve()
print(*result)