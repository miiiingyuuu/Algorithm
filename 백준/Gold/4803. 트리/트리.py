import sys
from collections import deque
input = sys.stdin.readline


def count_trees(n, graph):
    visited = [False] * (n+1)

    def count_vertices_and_edges(now):
        q = deque([now])
        visited[now] = True
        vertices = 1
        edges = 0

        while q:
            node = q.popleft()

            for neighbor in graph[node]:
                edges += 1
                if not visited[neighbor]:
                    visited[neighbor] = True
                    vertices += 1
                    q.append(neighbor)

        return vertices, edges // 2

    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            vertices, edges = count_vertices_and_edges(i)

            if edges == vertices - 1:
                cnt += 1

    return cnt


case = 1

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    trees = count_trees(n, graph)

    if trees == 0:
        print(f"Case {case}: No trees.")
    elif trees == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {trees} trees.")

    case += 1