import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline


def solve():
    distances = [float('inf')] * (n + 1)
    distances[1] = 0

    q = [(0, 1)]    # 비용, 노드

    while q:
        cur_distance, cur_node = heapq.heappop(q)

        if distances[cur_node] < cur_distance:
            continue

        for adj, cost in graph[cur_node]:
            distance = cur_distance + cost

            if distance < distances[adj]:
                distances[adj] = distance
                heapq.heappush(q, (distance, adj))

    return distances[n]


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(solve())