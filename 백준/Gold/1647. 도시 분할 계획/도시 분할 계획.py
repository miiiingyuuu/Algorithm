import sys
import heapq
input = sys.stdin.readline


def solve():
    visited = [False] * (n+1)
    heap = [(0, 1)] # (가중치, 정점)

    edges = []
    total_cost = 0

    while heap and len(edges) < n-1:
        cost, node = heapq.heappop(heap)

        if visited[node]:
            continue

        visited[node] = True
        total_cost += cost

        if node != 1:
            edges.append(cost)

        for next_node, next_cost in graph[node]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_cost, next_node))

    edges.sort()

    return total_cost - edges[-1]


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(solve())