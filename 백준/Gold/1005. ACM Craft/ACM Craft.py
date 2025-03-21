import sys
from collections import deque
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    d = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    total_time = [0] * (n + 1)

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1

    w = int(input())

    q = deque()

    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
            total_time[i] = d[i]

    while q:
        current = q.popleft()

        if current == w:
            break

        for next_building in graph[current]:
            total_time[next_building] = max(total_time[next_building], total_time[current] + d[next_building])

            in_degree[next_building] -= 1
            if in_degree[next_building] == 0:
                q.append(next_building)

    print(total_time[w])